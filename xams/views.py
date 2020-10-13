from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import xam


def home(request):
    return render(request,'home.html',{'title':'EGOV PROJECT'})    

def jee(request):
   
    return render(request,'jee.html',{'title':'APPLICATION'}) 
def year(request):
    return render(request,'year.html')  
def add1(request):
    
   name=request.POST['name']
   place=request.POST['place']
   adhar=request.POST['adhar']
   gender=request.POST['gender']
   religion=request.POST['religion']
   bd=request.POST['bd']
   mail=request.POST['mail']
   pic=request.FILES['pic']
   xaminfo=xam(name=name,place=place,adhar=adhar,gender=gender,religion=religion,bd=bd,mail=mail,pic=pic)
   xaminfo.save()
   return render(request,'success.html',{'title':'SUBMITTED!!'}) 
def home1(request):
    return redirect('home')   

def about1(request):
    return render(request,'about.html',{'title':'ABOUT US'})    
def vit(request):
    return render(request,'vit.html',{'title':'VIT APPLICATION'})    


# Create your views here.
