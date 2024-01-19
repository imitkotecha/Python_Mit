from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import *


# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method=='POST':
    user=signupForm(request.POST)
    if user.is_valid():
        user.save()
        print("Signup Sucessfully!")

        otp=random.randint(1111,9999)
        sub="Your One Time Password"
        msg=f"\nDear User\n\nThanks for registration with us.\n\nYour OTP is {otp}\n\n Thanks & Regards"
        from_id

        return redirect('otpverify')
    else:
        print(user.errors)
return render(request,'signup.html')