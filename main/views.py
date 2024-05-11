
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseForbidden
from .models import Role, Appointment, Feedback, Collaboration, Profile, Service, Contract, Skill, Technician, ProjectDocument
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from datetime import datetime
from django.db.models import Q
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO


# Create your views here.
def index(request):
    return render(request, 'authorize/index.html')


def about(request):
    return render(request, 'authorize/about.html')



def technician(request):
    return render(request, 'authorize/technicians.html')

def portifolio(request):
    return render(request, 'authorize/portifolio.html')

#contact info
def contact(request):
    return render(request, 'authorize/contact.html')



def services(request):
    return render(request, 'authorize/services.html')


def signUp(request):
    if request.method == "POST":
        username = request.POST['userName']
        email = request.POST['email']
        Fname = request.POST['firstName']
        Lname = request.POST['lastName']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        typ = request.POST['role']
    

# let handle some of the validation from user
        if Role.objects.filter(username = username):
            messages.error(request,"Username exist try another one")
            return redirect("signUp") 
        
        if Role.objects.filter(email=email):
            messages.error(request,'email exist')
            return redirect('signUp')
        
        if pass1 != pass2 :
            messages.error(request,"Password are different")
            return redirect('signUp')
        
    # let save the data from the user and user to be directed in login page/ signIn page
    
        myUser = Role.objects.create_user(username=username, email=email, password=pass1, role=typ)
        myUser.first_name = Fname
        myUser.last_name = Lname

        myUser.save()
        messages.success(request, f"Hellow {myUser.first_name} your account has success created you can go to Email {username} for the confirmation")
        return redirect('signIn')
    
    return render(request, 'authorize/new-register.html')

def signIn(request):
    if request.method == 'POST':
        email = request.POST['Uname']
        pass1 = request.POST['pass1']

        user = authenticate( username = email, password = pass1)
        if user is not None and user.role == 'Technician':# it act as the session that will differentiate user accoding to the are priference
            login(request, user)
            fName = user.first_name
            UserId = user.id
            messages.success(request,"Successfull Login")
            print(UserId)
            return redirect('register_technician')
        
        elif user is not None and user.role=='Client':
            login(request, user)
            fName = user.first_name
            UserId = user.id
            messages.success(request,"Successfull Login")
            print(UserId)
            return redirect('Plumbing')
        
        else:
            messages.error(request, "Username OR password invalid")
            return redirect('signIn')
        
    return render(request, 'authorize/login.html')

def signOut(request):
    logout(request)
    messages.success(request,'Your successfull Sign out ')
    return redirect('index')

def Plumbing(request):
    return render(request,"base.html")


def Electrical(request):
    return render(request, 'base.html')



def base_view(request):
    return render(request, 'main/base.html')

def home(request):
    return render(request, 'main/home.html')



#search
def search_technicians(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        location = request.GET.get('location')
        skill = request.GET.get('skill')
        
        # Start with all technicians
        technicians = Technician.objects.all()
        
        # Filter technicians based on search criteria
        if query:
            technicians = technicians.filter(Q(name__icontains=query) | Q(services__icontains=query))
        if location:
            technicians = technicians.filter(location__icontains=location)
        if skill:
            technicians = technicians.filter(skills__name__icontains=skill)
        
        return render(request, 'main/search_technicians.html', {'technicians': technicians})
    
    return render(request, 'main/search_technicians.html', {'technicians': None})





#Profile

@login_required
def create_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return redirect('view_profile', pk=profile.pk)  # Redirect to view existing profile
    except Profile.DoesNotExist:
        if request.method == 'POST':
            bio = request.POST.get('bio')
            avatar = request.FILES.get('avatar')
            profile = Profile.objects.create(user=request.user, bio=bio, avatar=avatar)
            return redirect('view_profile', pk=profile.pk)
        return render(request, 'authorize/create_profile.html')
    except IntegrityError:
        # Handle other IntegrityError cases, if any
        pass



@login_required
def view_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'authorize/profile_detail.html', {'profile': profile})

@login_required
def edit_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        bio = request.POST.get('bio')
        avatar = request.FILES.get('avatar')
        profile.bio = bio
        profile.avatar = avatar
        profile.save()
        return redirect('view_profile', pk=pk)
    return render(request, 'authorize/edit_profile.html', {'profile': profile})

@login_required
def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('Electrical')  # Redirect to the home page or any other desired page
    return render(request, 'authorize/profile_delete.html', {'profile': profile})




def contract(request):
    return render(request, 'main/contract.html')


def chat(request):
    return render(request, 'main/chat.html')


def availabbleTechnician(request):
    return render(request, 'main/view-technician.html')


def feedbackPost(request):
    return render(request, 'main/post-feedbacks.html')


def feedbackView(request):
    return render(request, 'main/post-feedbacks.html')


#feedback
def feedback_list(request):
    feedback_items = Feedback.objects.all()
    return render(request, 'main/feedback_list.html', {'feedback_items': feedback_items})

@login_required
def create_feedback(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')
        created_at = datetime.now()

        # Create new feedback
        Feedback.objects.create(title=title, details=details, created_at=created_at)
        return redirect('feedback_list')

    return render(request, 'main/create_feedback.html')

 
def view_feedback(request, feedback_id):
    feedback_item = get_object_or_404(Feedback, pk=feedback_id)
    return render(request, 'main/view_feedback.html', {'feedback_item': feedback_item})


def post_answer(request, feedback_id):
    if request.method == 'POST':
        answer = request.POST.get('answer')

        # Update feedback with answer
        feedback_item = get_object_or_404(Feedback, pk=feedback_id)
        feedback_item.answer = answer
        feedback_item.save()
        return redirect('view_feedback', feedback_id=feedback_id)

    return render(request, 'main/post_answer.html')




#technician

def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'authorize/skill_list.html', {'skills': skills})

def skill_detail(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    return render(request, 'authorize/skill_detail.html', {'skill': skill})

def skill_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Skill.objects.create(name=name)
        return redirect('skill_list')
    return render(request, 'authorize/skill_create.html')


def register_technician(request):
    if request.method == 'POST':
        # Process registration form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        skill_id = request.POST.get('skills')   
        location = request.POST.get('location')
        
        # Retrieve the selected skill object
        skill = Skill.objects.get(id=skill_id)
        
        technician = Technician.objects.create(
            name=name,
            email=email,
            password=password,
            location=location
        )
        
        technician.skills.add(skill)
 
        return redirect('profile_upload')

    skills = Skill.objects.all()
    return render(request, 'authorize/register.html', {'skills': skills})

def profile_upload(request):
    if request.method == 'POST':
        # Process profile upload form data
        name = request.POST.get('name')
        services = request.POST.get('services')
        image = request.FILES.get('image')
        cv = request.FILES.get('cv')
        
        # Update existing Technician object
        technician = Technician.objects.get(name=name)
        technician.services = services
        technician.image = image
        technician.cv = cv
        technician.save()
        
        return redirect('technician_details', pk=technician.pk)
    
    return render(request, 'authorize/profile_upload.html')

def technician_details(request, pk):
    technician = Technician.objects.get(pk=pk)
    return render(request, 'authorize/technician_details.html', {'technician': technician})

def list_technicians(request):
    technicians = Technician.objects.all()
    return render(request, 'authorize/list_technicians.html', {'technicians': technicians})




def register(request):
    return render(request, 'main/technician/new-register.html')

def collaborate(request):
    return render(request, 'main/technician/collaborate.html')

 

def collaborate(request):
    return render(request, 'main/technician/collaborate.html')

def collaboration_list(request):
    collaborations = Collaboration.objects.all()
    return render(request, 'collaboration_list.html', {'collaborations': collaborations})



@login_required
def create_collaboration(request): 
    if request.method == 'POST':
        user_instance = request.user
        comment = request.POST.get('comment')
        comment_at = datetime.now()

        ucomment = Collaboration(uid=user_instance, description=comment, time=comment_at)
        ucomment.save()

        return redirect('create_collaboration')
    
    all_comment = Collaboration.objects.all()

    context = {'all_comment': all_comment}
    
    return render(request, 'main/create_collaboration.html', context)


def view_collaboration(request, collaboration_id):
    collaboration = get_object_or_404(Collaboration, id=collaboration_id)
    messages = collaboration.get_messages()
    return render(request, 'main/view_collaboration.html', {'collaboration': collaboration, 'messages': messages})


 
def reject(request):
    return render(request, 'main/technician/reject.html')
 
def contractTech(request):
    return render(request, 'main/technician/tech-contract.html')
 
def dashboardTech(request):
    return render(request, 'main/technician/tech-dashboard.html')
 
def uploadProfile(request):
    return render(request, 'main/technician/upload-profile.html')
   
def viewBooking(request):
    return render(request, 'main/technician/view-booking.html')

 
#client
def booking(request):
    return render(request, 'main/client/booking.html')


@login_required
def create_appointment(request):
    appointment_id = None  # Initialize appointment_id variable
    technicians = Technician.objects.all()   
    services = Service.objects.all()   
    
    if request.method == 'POST':
        # Retrieve form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        phone_number = request.POST.get('phone_number')
        technician_id = request.POST.get('technician_id')
        services = request.POST.getlist('services')

        # Validate technician_id
        technician = get_object_or_404(Technician, id=technician_id)

        # Create the appointment
        appointment = Appointment.objects.create(
            title=title,
            description=description,
            date=date,
            phone_number=phone_number,
            user=request.user,
            technical_staff=technician
        )

        appointment_id = appointment.booking_id  # Set appointment_id to the booking_id of the created appointment

        messages.success(request, 'Appointment created successfully.')
        return redirect('appointment_list')

    return render(request, 'main/client/create_appointment.html', {'appointment_id': appointment_id, 'technicians': technicians, 'services': services})



@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'main/client/appointment_list.html', {'appointments': appointments})

@login_required
def delete_appointment(request, booking_id):
    appointment = get_object_or_404(Appointment, booking_id=booking_id)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully.')
    return redirect('appointment_list')


#feedback
def create_feedback(request, booking_id):
    if request.method == 'POST':
        description = request.POST.get('description')
        appointment = get_object_or_404(Appointment, booking_id=booking_id)
        technician = appointment.technical_staff

        try:
            feedback = Feedback.objects.create(
                appointment=appointment,
                user=request.user,  # Assign the current user to the user field
                technician=technician,
                description=description
            )
            messages.success(request, 'Feedback submitted successfully.')
            return redirect('feedback_list')
        except IntegrityError:
            messages.error(request, 'Failed to submit feedback.')
            # Handle the error, possibly redirect to an error page or show an error message
            # You can also log the error for debugging purposes
            return redirect('feedback_list')  # Redirect to feedback list or another page
    else:
        appointment = get_object_or_404(Appointment, booking_id=booking_id)
        return render(request, 'main/client/create_feedback.html', {'appointment': appointment})




@login_required
def feedback_list(request):
    feedbacks = Feedback.objects.filter(appointment__user=request.user)
    return render(request, 'main/client/feedback_list.html', {'feedbacks': feedbacks})

@login_required
def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)

    if request.method == 'POST':
        feedback.delete()
        messages.success(request, 'Feedback deleted successfully.')
        return redirect('feedback_list')

    return render(request, 'main/client/delete_feedback.html', {'feedback': feedback})




def dashboard(request):
    return render(request, 'main/client/client-dashboard.html')


#services
@login_required
def create_service(request):
    # pylint: disable=no-member
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        created_by = request.user

        service = Service.objects.create(title=title, description=description, price=price, created_by=created_by)
        messages.success(request, 'Service created successfully.')
        return redirect('service_list')
    return render(request, 'main/service_create.html')

@login_required
def service_list(request):
    # pylint: disable=no-member
    services = Service.objects.all()
    return render(request, 'main/service_list.html', {'services': services})

@login_required
def update_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.user == service.created_by:
        if request.method == 'POST':
            service.title = request.POST.get('title')
            service.description = request.POST.get('description')
            service.price = request.POST.get('price')
            service.save()
            messages.success(request, 'Service updated successfully.')
            return redirect('service_list')
        return render(request, 'main/update_service.html', {'service': service})
    else:
        return HttpResponseForbidden("You do not have permission to update this service.")

@login_required
def delete_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.user == service.created_by:
        if request.method == 'POST':
            service.delete()
            messages.success(request, 'Service deleted successfully.')
            return redirect('service_list')
        return render(request, 'main/delete_service.html', {'service': service})
    else:
        return HttpResponseForbidden("You do not have permission to delete this service.")



#contract
def create_contract(request):
    if request.method == 'POST':
        # Extract data from the POST request
        service_id = request.POST.get('service')
        phone_number = request.POST.get('phone_number')
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        # Get the selected service object
        service = get_object_or_404(Service, pk=service_id)
        
        # Get the latest appointment associated with the user
        appointment = Appointment.objects.filter(user=request.user).last()
        
        # Get the technician name from the appointment
        technician_name = appointment.technical_staff.name if appointment else None
        
        # Ensure that the chosen title is one of the valid choices
        valid_titles = dict(Contract.CONTRACT_CHOICES).keys()
        if title not in valid_titles:
            return render(request, 'main/create_contract.html', {
                'services': Service.objects.all(),
                'contract_choices': Contract.CONTRACT_CHOICES,
                'error_message': 'Invalid contract title.'
            })
        
        # Create the contract object and save it to the database
        contract = Contract.objects.create(
            service=service,
            user=request.user,
            phone_number=phone_number,
            title=title,
            description=description,
            technician_name=technician_name  # Use technician_name field
        )
        
        # Redirect to the view contract page with the newly created contract's primary key
        return redirect('view_contract', pk=contract.pk)
    
    # If the request method is not POST, render the create contract form
    return render(request, 'main/create_contract.html', {'services': Service.objects.all(), 'contract_choices': Contract.CONTRACT_CHOICES})



def view_contract(request, pk):
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        raise Http404("Contract does not exist")
    
    return render(request, 'main/contract_detail.html', {'contract': contract})


def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'main/contract_list.html', {'contracts': contracts})


def download_contract(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    
    # Render HTML template with contract details
    html_content = render_to_string('main/contract_template.html', {'contract': contract})
    
    # Create PDF content from HTML
    pdf = BytesIO()
    pisa.CreatePDF(html_content, dest=pdf)
    
    # Get PDF content from buffer
    pdf_content = pdf.getvalue()
    
    # Close buffer
    pdf.close()
    
    # Create HTTP response with PDF content
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contract_{contract.pk}.pdf"'
    
    return response


# Project documentation
def documentation(request):
    document = ProjectDocument.objects.all()
    return render(request, 'main/document.html', {'document': document})
