from django.shortcuts import render,redirect
from .forms import UserProfileForm,LoginForm
from .models import UserProfile

# Create your views here.
def register_user(request):
    userprofileform = UserProfileForm(request.POST or None)
    if request.method=="POST":
        if userprofileform.is_valid():
            try:
                userprofileform.save()
                return redirect('/login')
            except:
                return redirect('/registeruser')
    context={'form':userprofileform}
    return render(request,'accounts/register_user.html',context)
def login(request):
    loginform=LoginForm(request.POST or None)
    if request.method=="POST":
        if loginform.is_valid():
            username=loginform.cleaned_data.get('username')
            password=loginform.cleaned_data.get('password')
            try:
                user=UserProfile.objects.get(email=username,password=password)
                return redirect('/dashboard')
            except:
                return redirect('/login')

    context  ={'form':loginform}
    return render(request,'accounts/login.html',context)
def dashboard(request):

    return render(request,'accounts/dashboard.html',)
def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/login')
def guest_register(request):
    return redirect('/login')