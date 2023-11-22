from django.shortcuts import render
import random
# Create your views here.
num=1
def index(request):
    name='Mit'
    global num
    num+=1
    return render(request,'index.html',{'Name' :name, 'Number' :num})
def about(request):
    return render(request,'about.html')
def contact(request):
    global num
    num-=1
    return render(request,'contact.html',{'Number' :num})