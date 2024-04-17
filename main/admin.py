from django.contrib import admin
from .models import (User, Profile, Category, Skill, Service, Technician,
                     Appointment, Contract, Feedback, Collaboration, 
                     ContactInfo, ProjectDocument)



# Register your models here
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Technician)
admin.site.register(Appointment)
admin.site.register(Contract)
admin.site.register(Feedback)
admin.site.register(Collaboration)
admin.site.register(ContactInfo)
admin.site.register(ProjectDocument)
