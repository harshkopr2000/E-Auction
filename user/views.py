from django.shortcuts import render,redirect
from django.http import HttpResponse

from myadmin import models as myadmin_models
from mydjapp import models as mydjapp_models
from . import models

import time

#middleware to check session for user routes
def sessioncheckuser_middleware(get_response):
	def middleware(request):
		if request.path=='/user/' or request.path=='/user/funds/' :
			if request.session['sunm']==None or request.session['srole']!="user":
				response = redirect('/login/')
			else:
				response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware


# Create your views here.

def userhome(request):
 return render(request,"userhome.html",{"sunm":request.session["sunm"]})

def cpuser(request):
 if request.method=="GET":   
  return render(request,"cpuser.html",{"sunm":request.session["sunm"]})
 else:
  opassword=request.POST.get("opassword")
  npassword=request.POST.get("npassword")     
  cnpassword=request.POST.get("cnpassword")
  sunm=request.session["sunm"]
  
  userDetails=mydjapp_models.Register.objects.filter(email=sunm,password=opassword)
  
  if len(userDetails)>0:
   if npassword==cnpassword:
    mydjapp_models.Register.objects.filter(email=sunm).update(password=cnpassword)
    msg="Password changed successfully...."
   else:
    msg="New & Confirm new password mismatch"    
  else:	
   msg="Old password not matched"      
  return render(request,"cpuser.html",{"sunm":request.session["sunm"],"output":msg}) 	

def epuser(request):
 if request.method=="GET":
  userDetails=mydjapp_models.Register.objects.filter(email=request.session["sunm"])
  return render(request,"epuser.html",{"sunm":request.session["sunm"],"userDetails":userDetails[0]})     
 else:         
  #recieve data from ui
  name=request.POST.get("name")
  email=request.POST.get("email")
  mobile=request.POST.get("mobile")
  address=request.POST.get("address")
  city=request.POST.get("city")
  gender=request.POST.get("gender")
  
  #update record in database table
  mydjapp_models.Register.objects.filter(email=request.session["sunm"]).update(name=name,mobile=mobile,address=address,city=city,gender=gender)     
  return redirect("/user/epuser/")

def funds(request):
 paypalURL="https://www.sandbox.paypal.com/cgi-bin/webscr"    
 paypalID="sb-bggon26642575@business.example.com"
 amt=100
 #sb-gbfru26979850@personal.example.com
 return render(request,"funds.html",{"paypalURL":paypalURL,"paypalID":paypalID,"amt":amt,"sunm":request.session["sunm"]})

def payment(request):
 uid=request.GET.get("uid")
 amt=request.GET.get("amt")
 p=models.Payment(uid=uid,amt=int(amt),info=time.asctime())	
 p.save()
 return redirect("/user/success/")

def cancel(request):
 return render(request,"cancel.html",{"sunm":request.session["sunm"]})

def success(request):
 return render(request,"success.html",{"sunm":request.session["sunm"]})

def searchcat(request):
 clist=myadmin_models.Category.objects.all()  
 return render(request,"searchcat.html",{"clist":clist,"sunm":request.session["sunm"]})

def searchsubcat(request):
 catname=request.GET.get("catname")  
 clist=myadmin_models.Category.objects.all()
 sclist=myadmin_models.SubCategory.objects.filter(catname=catname)  
 return render(request,"searchsubcat.html",{"catname":catname,"clist":clist,"sclist":sclist,"sunm":request.session["sunm"]})

def searchproduct(request):
 scname=request.GET.get("scname") 
 plist=myadmin_models.Product.objects.filter(subcatname=scname)  
 return render(request,"searchproduct.html",{"plist":plist,"sunm":request.session["sunm"]})


def bidstatus(request):
 pid=int(request.GET.get("pid")) 
 pDetails=myadmin_models.Product.objects.filter(pid=pid)  
 dtime=time.time()-int(pDetails[0].info)
 return render(request,"searchproduct.html",{"plist":plist,"sunm":request.session["sunm"]})
