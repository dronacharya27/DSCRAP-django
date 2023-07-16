from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import contact
from .models import useraddress
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import cv2
import os
from os import listdir
from distutils.log import debug
from fileinput import filename
from django.core.files.storage import default_storage
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import docform
from django.core.files.storage import FileSystemStorage
from .obj import objd
from datetime import datetime
from django.conf import settings
import pandas as pd
import IPython
from IPython.display import HTML

# CONTACT

def index(request):
    return render(request,'index.html')

def contact2(request):
    if request.method == "POST":
        Name= request.POST.get('name','')
        Email= request.POST.get('email','')
        Subject = request.POST.get('subject','')
        Message= request.POST.get('message','')

    Contact = contact(Name,Email,Subject,Message)
    Contact.save()
    messages.success(request,"Your Message Has been sent successfully")
    return redirect('index')


# LOGIN

def handlelogin(request):
    
    if request.method == "POST":
        
        loginname = request.POST["loginname"]
        loginpass = request.POST.get('loginpass','')

        user = authenticate(username=loginname, password=loginpass)
        print(user)
        param = [user]

        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('index')

        else:
            messages.error(request,'Invalid Credentials, Please Try Again!')
            return redirect('index')
    else:
        return HttpResponse('404-Not Found')
    
def handlelogout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request,"Successfully Loged-Out")
        return redirect('index')

    return HttpResponse('handlelogout')


# SIGNUP

def handlesignup(request):

    if request.method == "POST":
        postdata = request.POST.copy()
        username = postdata.get('username', '')
        email = postdata.get('email', '')
        password = postdata.get('passw', '')
        
       
        create_new_user = User.objects.create_user(username=username,email= email,password= password)
        create_new_user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        if create_new_user is not None:
                if create_new_user.is_active:
                    messages.success(request,"USER CREATED SUCCESFULLY")
                    return redirect('index')
                else:
                    print("The password is valid, but the account has been disabled!")


    return  redirect('index')

# UPLOAD AND BACKEND

def trye(request):
 
    if request.method=="POST":
        form = docform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            date = datetime.now()
            name= date.strftime('%H%M')  
            path = "C:\\Users\\dron\\Downloads\\DSCRAP django\\dscrap\\media\\dscrap\\images\\"+"scrap"+name+".jpg" 
            # assert os.path.exists("dscrap\\images\\"+"scrap"+name+".jpg")
            print(path) 
            detect = objd(path)
            final = detect[1]
            options = detect[0]
            total = detect[2]
            no_items = detect[3]
            df = pd.DataFrame({"ITEMS":options,"PRICES":final})
            html = df.to_html(classes=["table-bordered", "table-primary", "table-hover","table-l"])
            
            text_file = open("C:\\Users\\dron\\Downloads\\DSCRAP django\\dscrap\\dscrap\\templates\\table.html", "w")
            text_file.write(html)
            text_file.close()
            print(df)   
            params={'final':final,'options':options,'total':total,'no_items':no_items}
            return render(request,'bill.html',params)
        else:
            context = {'form':form}
            messages.success(request,"Uploaded Successfully")
            return render(request,'scrapcalc.html', context)
        
    context = {'form':docform()}
    return render(request,'scrapcalc.html', context)

def address(request):
    if request.method=="POST":
        name = request.POST.get('aname','')
        address = request.POST.get('add','')
        address = useraddress(name,address)
    address.save()
    messages.success(request,"Pick-Up Set Successfully!")
    return redirect('index')
   




