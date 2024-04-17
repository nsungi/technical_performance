
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signUp/', views.signUp, name='signUp'),
    path('signIn/', views.signIn, name='signIn'),
    path('signOut/', views.signOut, name='signOut'),
    path('Electrical/', views.Electrical, name='Electrical'),
    path('Plumbing/', views.Plumbing, name='Plumbing'),
    path('about/', views.about, name='about'),
    path('portifolio/', views.portifolio, name='portifolio'),
    path('services/', views.services, name='services'),
    
    #search
    path('search_technicians/', views.search_technicians, name='search_technicians'),
    
    
    #contact info
    path('contact/', views.contact, name='contact'),
    path('contact_form/', views.contact_form, name='contact_form'),
    path('success/', views.success, name='success'),
    path('view-messages/', views.view_messages, name='view_messages'), 
   
    
    path('contract/', views.contract, name='contract'),
    path('chat/', views.chat, name='chat'),
    path('availabbleTechnician/', views.availabbleTechnician, name='availabbleTechnician'),
    path('feedbackPost/', views.feedbackPost, name='feedbackPost'),
    path('feedbackView/', views.feedbackView, name='feedbackView'),
    
    #feedback
    #path('create_feedback/', views.create_feedback, name='create_feedback'),
    path('feedback_list/', views.feedback_list, name='feedback_list'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    path('post_answer/', views.post_answer, name='post_answer'),
    
    path('feedback_list/', views.feedback_list, name='feedback_list'),
    #path('accept_feedback/<int:pk>/', views.accept_feedback, name='accept_feedback'),
    #path('reject_feedback/<int:pk>/', views.reject_feedback, name='reject_feedback'),
    
    
    #testing
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('delete_appointment/<int:booking_id>/', views.delete_appointment, name='delete_appointment'),
    path('create_feedback/<int:booking_id>/', views.create_feedback, name='create_feedback'),
    path('feedback_list/', views.feedback_list, name='feedback_list'),
    path('delete_feedback/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
     
    path('create_profile/', views.create_profile, name='create_profile'),
    path('view_profile/<int:pk>/', views.view_profile, name='view_profile'),
    path('edit_profile/<int:pk>/', views.edit_profile, name='edit_profile'),
    path('delete_profile/<int:pk>/', views.delete_profile, name='delete_profile'),
    
    #contract
    path('create_contract/', views.create_contract, name='create_contract'),
    path('view_contract/<int:pk>/', views.view_contract, name='view_contract'),
    path('contract_list/', views.contract_list, name='contract_list'),
    path('download_contract/<int:pk>/', views.download_contract, name='download_contract'),
    
    #Services
    path('create_service/', views.create_service, name='create_service'),
    path('list/', views.service_list, name='service_list'),
    path('update/<int:pk>/', views.update_service, name='update_service'),
    path('delete/<int:pk>/', views.delete_service, name='delete_service'),
    
    #collaborate
    path('create_collaboration/', views.create_collaboration, name='create_collaboration'),
    path('view_collaboration/', views.view_collaboration, name='view_collaboration'),
    #path('send_message/', views.send_message, name='send_message'),
    #path('conversation/<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
    
    
    #technician
    path('register/', views.register, name='register'),
    path('collaborate/', views.collaborate, name='collaborate'),
    path('reject/', views.reject, name='reject'),
    path('reject/', views.contractTech, name='contractTech'),
    path('dashboardTech/', views.dashboardTech, name='dashboardTech'),
    path('uploadProfile/', views.uploadProfile, name='uploadProfile'),
    path('viewBooking/', views.viewBooking, name='viewBooking'),
    
    
    path('skill_list/', views.skill_list, name='skill_list'),
    path('skill_detail/<int:pk>/', views.skill_detail, name='skill_detail'),
    path('skill_create/', views.skill_create, name='skill_create'),
    
    path('register_technician/', views.register_technician, name='register_technician'),
    path('profile_upload/', views.profile_upload, name='profile_upload'),
    path('technician_details/<int:pk>/', views.technician_details, name='technician_details'),
    path('list_technicians/', views.list_technicians, name='list_technicians'),
    
    
    #client
    path('booking/', views.booking, name='booking'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('delete_appointment/<int:booking_id>/', views.delete_appointment, name='delete_appointment'),
    
    #path('feedback/<int:booking_id>/', views.feedback, name='feedback'),
    path('feedback_list/', views.feedback_list, name='feedback_list'),
    
    
    
    #admin
    path('dashboardAdmin/', views.dashboardAdmin, name='dashboardAdmin'),
    path('profileApproved/', views.profileApproved, name='profileApproved'),
    path('users/', views.users, name='users'),
    path('categoryRole/', views.categoryRole, name='categoryRole'),
    path('userAction/', views.userAction, name='userAction'),
    path('viewUsers/', views.viewUsers, name='viewUsers'),
   
   #documentntation
   path('documention/', views.documentation, name='documentation'),
   
    
]