from django.shortcuts import render,redirect,get_object_or_404
from .models import Department, Course, Enquiry
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    obj=Department.objects.all()
    return render(request,'department.html',{'result':obj})

def register(request):
    if request.method=='POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        confpass= request.POST['password1']
        if password==confpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken..")
                return redirect('college_app:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists..")
                return redirect('college_app:register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                print("user created")
                return redirect('college_app:login')

        else:
            messages.info(request,"password not matching")
            return redirect('college_app:register')
    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'userinfo.html') 
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'login.html')

    return render(request, 'login.html')

def user_logout(request):
    auth.logout(request)
    return redirect('/')

def enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phoneNumber = request.POST.get('phoneNumber')
        mailId = request.POST.get('mailId')
        address = request.POST.get('address')
        department_id = request.POST.get('department')
        course_id = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')

        # Save the enquiry to the database
        enquiry = Enquiry.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phoneNumber=phoneNumber,
            mailId=mailId,
            address=address,
            department_id=department_id,
            course_id=course_id,
            purpose=purpose,
        )
        enquiry.materials.set(materials)

        # Redirect to a success page
        return redirect('success')

    else:
        departments = Department.objects.all()
        courses = Course.objects.all()
        return render(request, 'enquiry.html', {'departments': departments, 'courses': courses})

def success(request):
    return render(request, 'success.html')

def dept_detail(request, d_slug):
    department = get_object_or_404(Department, slug=d_slug)
    enquiries = Enquiry.objects.filter(department=department)
    return render(request, 'desc.html', {'department': department, 'enquiries': enquiries})

@login_required
def user_info(request):
    return render(request, 'userinfo.html')