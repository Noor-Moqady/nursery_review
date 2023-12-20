from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from.models import *


def registration_form(request):
    if request.method == 'GET':
        return render(request,"login_registration.html")
    if request.method == 'POST':
# VALIDATION PART############################################################################################################################################################################################################################################################
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            if request.POST['birthday'] != '':
                user=User.objects.create(parent_name=request.POST['parent_name'], email=request.POST['email'],password=pw_hash, birthday=request.POST['birthday'],user_roles=Roles.objects.get(pk=2))
                request.session['logged_user_parentname']=user.parent_name
                request.session['logged_user_id']=user.id
            else:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                user=User.objects.create(parent_name=request.POST['parent_name'], email=request.POST['email'],password=pw_hash,user_roles=Roles.objects.get(pk=2))
                request.session['logged_user_parent_name']=user.parent_name
                request.session['logged_user_id']=user.id
                

        return redirect('/')
    


def welcome(request):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/register')
    else:
        context = {
       'allnurseries': Nursery.objects.all(),
       'specific_user': User.objects.get(id=request.session['logged_user_id'])
               }
    return render(request,"nurseries.html", context)
    

def login(request):
    if request.method == 'GET':
        return render(request,"login_registration.html")
    
    if request.method == 'POST':
        
        userlogged=User.objects.filter(email=request.POST['email'])
        if userlogged: 
            logged_user=userlogged[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['logged_user_parent_name']=logged_user.parent_name
                request.session['logged_user_id']=logged_user.id
                return redirect('/')
            else:
                messages.error(request,"Invalid Password")
                return redirect('/register')
        else:
            messages.error(request,"Invalid email address")
            return redirect('/register')    

def logout(request):
    request.session.flush()
    return redirect('/register')


def render_aboutus(request):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/register')
    else:
        return render (request, "about.html")

def render_contactus(request):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/register')
    else:
        return render (request, "contact.html")

def addnursery(request):
    print (request.POST.getlist('facilities'))
    specific_nursery = Nursery.objects.create(nursery_name= request.POST['nursery_name'], facilities= request.POST.getlist('facilities'),program_offered=request.POST.getlist('program_offered'), contact_number=request.POST['contact_number'], nursery_location=request.POST['nursery_location'])
    
    return redirect('/')

def specific_nursery(request, id):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/register')
    else:
        return render (request, "nursery.html")




   