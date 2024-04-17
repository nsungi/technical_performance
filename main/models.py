from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.contrib.auth import get_user_model


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CLIENT = "CLIENT", 'Client'
        TECHNICIAN = "TECHNICIAN", 'Technician'

    role = models.CharField(max_length=50, choices=Role.choices)
    objects = UserManager()

class RoleManager(UserManager):
    def clients(self):
        return self.filter(role=User.Role.CLIENT)

class Role(User):
    objects = RoleManager()
    class Meta:
        proxy = True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager() 
    



class Category(models.Model):
    STATUS = [("staff", "Staff"), ("non_staff", "Non_staff")]
    current_status = models.CharField(max_length=10, choices=STATUS, default="staff")
    

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["title"]

    def __str__(self):
        return self.title  

    
 
class Technician(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill, related_name='technicians')
    location = models.CharField(max_length=100)
    services = models.ManyToManyField(Service, related_name='technicians')
    image = models.ImageField(upload_to='technician_images/', blank=True)
    cv = models.FileField(upload_to='technician_cvs/', blank=True)

    def __str__(self):
        return self.name



class Appointment(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, related_name='appointments')
    technical_staff = models.ForeignKey(Technician, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Appointment #{self.booking_id}"


    
class Contract(models.Model):
    CONTRACT_CHOICES = (
        ('IT Support', 'IT Support contract'),
        ('Network Maintenance', 'Network Maintenance contract'),
        ('Electrical Maintenance', 'Electrical Maintenance contract'),
        ('Plumbing Maintenance', 'Plumbing Maintenance contract'),
    )

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    title = models.CharField(max_length=100, choices=CONTRACT_CHOICES)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, blank=True, null=True)  # Optional ForeignKey
    technician_name = models.CharField(max_length=100, blank=True, null=True) 

    def __str__(self):
        return f"Contract: {self.title}"
    
    
class Feedback(models.Model):
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ACCEPT = 'accepted'
    REJECT = 'rejected'
    MESSAGE_CHOICES = [
        (ACCEPT, 'Accepted'),
        (REJECT, 'Rejected'),
    ]
    message = models.CharField(max_length=10, choices=MESSAGE_CHOICES, default=ACCEPT)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for Appointment #{self.appointment.booking_id}"

 
# Conversation
class Collaboration(models.Model):
    uid = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField()
    time = models.DateTimeField()


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 




class ProjectDocument(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='project/', blank=True)

    def __str__(self):
        return self.name


