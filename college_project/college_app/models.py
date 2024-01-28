from django.db import models
from django.urls import reverse

class Department(models.Model):
    name=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='dept',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'
    
    def get_url(self):
        return reverse('college_app:department',args=[str(self.slug)])

    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name='course'
        verbose_name_plural='courses'

    def __str__(self):
        return '{}'.format(self.name)
    
class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=15)
    mailId = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=255)
    materials = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)
