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
        'allfacilities': Facilities.objects.all(),
        'alloprograms' :Programs.objects.all(),
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
    # VALIDATION PART############################################################################################################################################################################################################################################################
            errors = Nursery.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                
                avatar = request.FILES.get('avatar', None)
                print(avatar)
                specific_nursery = Nursery.objects.create(nursery_name= request.POST['nursery_name'], contact_number=request.POST['contact_number'], nursery_location=request.POST['nursery_location'], avatar=avatar)
                specific_facilities= request.POST.getlist('facilities')
                specific_program= request.POST.getlist('program_offered')
                for fac in specific_facilities:
                    Facility= Facilities.objects.get(id=int(fac))
                    specific_nursery.facilities.add(Facility)

                for prog in specific_program:
                    program=Programs.objects.get(id=int(prog))
                    specific_nursery.program_offered.add(program)
    
            return redirect('/')

def addreview(request, id):
    # VALIDATION PART############################################################################################################################################################################################################################################################
            errors = Review.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                specific_review = Review.objects.create(review=request.POST['review'], uploaded_by=User.objects.get(id=request.session['logged_user_id']), nursery_review=Nursery.objects.get(id=int(id)))
            return redirect('/nursery/'+str(id))

def delete_review(request, id2):
    specific_review = Review.objects.get(id=int(id2)) 
    associated_nursery_id = specific_review.nursery_review.id 
    specific_review.delete() 
    return redirect('/nursery/'+str(associated_nursery_id))  

def specific_nursery(request, id):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/register')
    else:
        context={
            'specific_nursery': Nursery.objects.get(id=id),
            'specific_user': User.objects.get(id=request.session['logged_user_id'])

        }
        return render (request, "nursery.html", context)

def delete_nursery(request,id):
    specific_nursery=Nursery.objects.get(id=int(id))
    specific_nursery.delete()
    return redirect('/')


def update_review(request,id):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/')
    else:
        if request.method == 'GET':
            context={
            'specific_review': Review.objects.get(id=id)
        }
            return render(request,"update_review.html", context)
        if request.method == 'POST':
# VA    LIDATION PART############################################################################################################################################################################################################################################################
            errors = Review.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                specific_review=Review.objects.get(id=id)
                specific_review.review=request.POST['review']
                specific_review.save()
            return redirect('/')
        
def update_nursery(request,id):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/')
    else:
        if request.method == 'GET':
            context = {
            'allfacilities': Facilities.objects.all(),
            'alloprograms' :Programs.objects.all(),
            'allnurseries': Nursery.objects.all(),
            'specific_nursery':Nursery.objects.get(id=id),
            'specific_user': User.objects.get(id=request.session['logged_user_id'])
               }
            return render(request,"update_nursery.html", context)
        if request.method == 'POST':
# VA    LIDATION PART############################################################################################################################################################################################################################################################
            errors = Nursery.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                specific_nursery=Nursery.objects.get(id=id)
                specific_nursery.nursery_name=request.POST['nursery_name']
                specific_nursery.contact_number=request.POST['contact_number']
                specific_nursery.nursery_location=request.POST['nursery_location']
                specific_nursery.save()
            return redirect('/')
            

def reviews(request):
    if not 'logged_user_id' in request.session:
        messages.error(request,"You have to login first")
        return redirect('/register')
    else:
        context = {
       'allnurseries': Nursery.objects.all(),
       'specific_user': User.objects.get(id=request.session['logged_user_id']),
       'allreviews': Review.objects.all()
               }
    return render(request,"reviews.html", context)