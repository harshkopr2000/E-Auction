from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import time
from mydjapp import models as mydjapp_models
from . import models

#middleware to check session for admin routes
def sessioncheckmyadmin_middleware(get_response):
	def middleware(request):
		if request.path=='/myadmin/' or request.path=='/myadmin/manageusers/' or request.path=='/myadmin/manageuserstatus/' :
			if request.session['sunm']==None or request.session['srole']!="admin":
				response = redirect('/login/')
			else:
				response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware

# Create your views here.
def adminhome(request):
 return render(request,"adminhome.html",{"sunm":request.session["sunm"]})

def manageusers(request):
 userDetails=mydjapp_models.Register.objects.filter(role="user")
 return render(request,"manageusers.html",{"userDetails":userDetails,"sunm":request.session["sunm"]})  

def manageuserstatus(request):
 regid=int(request.GET.get("regid"))    
 status=int(request.GET.get("status"))
 
 if status==1:
  mydjapp_models.Register.objects.filter(regid=regid).update(status=status)
 elif status==0:
  mydjapp_models.Register.objects.filter(regid=regid).update(status=status)
 else:
  mydjapp_models.Register.objects.filter(regid=regid).delete()      
 
 return redirect("/myadmin/manageusers/")       

def addcategory(request):
 if request.method=="GET":    
  return render(request,"addcategory.html",{"sunm":request.session["sunm"],"output":""})
 else:
  catname=request.POST.get("catname")
  caticon=request.FILES["caticon"]
  fs = FileSystemStorage()
  filename = fs.save(caticon.name,caticon)
  p=models.Category(catname=catname,caticonname=filename)
  p.save()   
  
  return render(request,"addcategory.html",{"sunm":request.session["sunm"],"output":"Category added successfully...."})
     
def addsubcategory(request):
 clist=models.Category.objects.all()  
 if request.method=="GET":    
  return render(request,"addsubcategory.html",{"sunm":request.session["sunm"],"output":"","clist":clist})
 else:
  catname=request.POST.get("catname")
  subcatname=request.POST.get("subcatname")
  subcaticon=request.FILES["subcaticon"]
  fs = FileSystemStorage()
  filename = fs.save(subcaticon.name,subcaticon)
  p=models.SubCategory(catname=catname,subcatname=subcatname,subcaticonname=filename)
  p.save()   
  
  return render(request,"addsubcategory.html",{"sunm":request.session["sunm"],"output":"SubCategory added successfully....","clist":clist})

def addproduct(request):
 sclist=models.SubCategory.objects.all()   
 if request.method=="GET":    
  return render(request,"addproduct.html",{"sunm":request.session["sunm"],"sclist":sclist,"output":""})
 else:
  ptitle=request.POST.get("ptitle")   
  subcatname=request.POST.get("subcatname")
  pdescription=request.POST.get("pdescription")
  pbprice=request.POST.get("pbprice")
 
  picon=request.FILES["picon"]
  fs = FileSystemStorage()
  filename = fs.save(picon.name,picon)
  p=models.Product(ptitle=ptitle,subcatname=subcatname,pdescription=pdescription,pbprice=pbprice,piconname=filename,info=time.time())
  p.save()   
  
  return render(request,"addproduct.html",{"sunm":request.session["sunm"],"sclist":sclist,"output":"Product added successfully...."})
