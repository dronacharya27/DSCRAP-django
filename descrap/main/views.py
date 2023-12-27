from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from .models import Useraddress
from .models import MyUser
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import docform
from .obj import objd
from datetime import datetime
import pandas as pd
from django.conf import settings
import os

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

    Contact = Contact(Name,Email,Subject,Message)
    Contact.save()
    messages.success(request,"Your Message Has been sent successfully")
    return redirect('index')


# LOGIN

def handlelogin(request):
    
    if request.method == "POST":
        postdata = request.POST.copy()
        loginemail = postdata.get('email',None)
        loginpass = postdata.get('loginpass',None)

        user = authenticate(email=loginemail, password=loginpass)
        print(user)
        print(user.check_password(raw_password=loginpass))
        login(request,user)
        if user is not None:
            
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
        
       
        create_new_user = MyUser.objects.create_user(email= email,password= password)
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
            
            path = settings.DETECT_ROOT+"/scrap"+name+".jpg" 
            # assert os.path.exists("dscrap\\images\\"+"scrap"+name+".jpg")
            print(path) 
            detect = objd(path)
            final = detect[1]
            options = detect[0]
            total = detect[2]
            no_items = detect[3]
            df = pd.DataFrame({"ITEMS":options,"PRICES":final})
            html = df.to_html(classes=["table-bordered", "table-primary", "table-hover","table-l"])
            
            text_file = open("./main/templates/table.html", "w")
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
        address = Useraddress(name,address)
    address.save()
    messages.success(request,"Pick-Up Set Successfully!")
    return redirect('index')
   




