from django.contrib import admin
from .models import Department, Enquiry, Course
# Register your models here.
admin.site.register(Department)
admin.site.register(Enquiry)
admin.site.register(Course)