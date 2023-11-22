from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    if request.method=='POST':
        fnm=request.POST['firstname']
        lnm=request.POST['lastname']
        email=request.POST['email']
        adr=request.POST['address']
        mob=request.POST['mobile']
        dob=request.POST['DateofBirth']
        
        signupinfo.objects.create(firstname=fnm, lastname=lnm, email=email, address=adr, mobile=mob, DateofBirth=dob)
        print("Your data has been inserted !")
    else:
        print("Error! SOmething went wrong")

    return render(request,'index.html')

def showdata(request):
    data=signupinfo.objects.all()
    return render(request,'showdata.html',{'data':data})
    