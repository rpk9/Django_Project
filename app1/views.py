from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import SignUp
from . forms import SignUpForm, LogInForm, UpdateForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import logout as logouts



# Create your views here.
def func1(request):
    return HttpResponse("Welcome to Django")


def index(request):
    name = "Rohith"
    return render(request,'index.html', {'data':name}) #context passing

def register(request):
    if request.method == 'POST':
        form1 = SignUpForm(request.POST,request.FILES)
        if form1.is_valid():
            name = form1.cleaned_data['Name']
            age = form1.cleaned_data['Age']
            email = form1.cleaned_data['Email']
            password = form1.cleaned_data['Password']
            photo = form1.cleaned_data['Photo']
            confirmpassword = form1.cleaned_data['ConfirmPassword']
            user = SignUp.objects.filter(Email=email).exists()
            if user:
                messages.success(request,'Email already exists')
                return redirect('register/')
            
            elif password != confirmpassword:
                messages.success(request,'Password mismatch')
                return redirect('register/')
            
            else:
                table = SignUp(Name = name,Age = age, Email = email, Password = password,Photo = photo)
                table.save()
                messages.success(request, 'Registration Successfull')
                return redirect('/')            
                
                
        
    else:
        form1 = SignUpForm()    

    return render(request,'SignUp.html', {'form':form1})


def login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)    
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            usercheck= SignUp.objects.get(Email=email)
            if not usercheck:
                messages.success(request,'user doesnt exists')
                return redirect('/login')
            else:
                messages.success(request, 'Login Successfull')
                return redirect('/home/%s' % usercheck.id)
            
    else:
        form=LogInForm()
        
    return render(request, 'Login.html',{'form':form})    

def home(request, id):
    user = SignUp.objects.get(id=id)
    return render(request, 'Home.html', {'user': user})


def update(request, id):
    user = SignUp.objects.get(id=id)
    form = UpdateForm(request.POST or None,request.FILES or None, instance= user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated Successfully')
        return redirect('/home/%s' %user.id)
    return render(request,'update.html',{'user':user , 'form':form})

def changePassword(request, id):
    user = SignUp.objects.get(id=id)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword = form.cleaned_data['OldPassword']
            newpassword = form.cleaned_data['NewPassword']
            confirmpassword = form.cleaned_data['ConfirmNewPassword']
            if oldpassword != user.Password:
                messages.success(request, 'Enter the correct password')
                return redirect('/changePassword/%s' % user.id)
            
            elif newpassword != confirmpassword:
                messages.success(request,'Password mismatch')
                return redirect('/changePassword/%s' % user.id)
            
            else:
                user.Password = newpassword
                user.save()
                messages.success(request, 'Password updated successfully')
                return redirect('/home/%s' % user.id)
            
    else:
        form = ChangePasswordForm()
                
    return render(request,'changepassword.html',{'user': user, 'form': form} )       
            
        #form.save()
        #messages.success(request, 'Password Changed Successfully')
        
def logout(request):
    logouts(request)
    messages.success(request, 'Logout Successfull')
    return redirect('/')
            

            
            
            
    



