from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.db import transaction


from .models import *
from .forms import *
from .predict import *
from .utils import template_constants,activities
# from .utils import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.db.models import F, Value, IntegerField, Sum,Q,Max
from django.db.models.functions import Cast

from django.conf import settings
import os
import re

# Create your views here.
def index(request):
    return render(request,'index.html')

def logout(request):
    request.session.clear()
    return redirect('index')

def login_view(request,user_type):
    return render(request,'auth/login.html',{'user_type':user_type})

def register_view(request,user_type):
    return render(request,'auth/register.html',{'user_type':user_type})

def createAccount(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            response = {
                'status': True,
                'message': 'User Created Successfully'
            }
            return JsonResponse(response)
        else:
            # Form is not valid, extract error messages
            errors = form.errors
            print(errors)
            error_message = str(errors['contact'][0]) if 'contact' in errors else str(errors['email'][0]) if 'email' in errors  else 'Invalid form data'

            response = {
                'status': False,
                'message': error_message
            }
            return JsonResponse(response)
        
    return JsonResponse({ 'status':False, 'message':'Invalid Request Method!' })

def loginAccount(request):
    if request.method=='POST':
        response={
            'status':False,
            'message':'Invalid Request Method!'
        }
           
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user_type']
        
        user = User.objects.filter(email=email, password=password,is_active=1,user_type=user_type).first()

        if user is None:
            response={
                'status':False,
                'message':'Invalid User'
            }
        else:
            request.session['userId']=user.id
            request.session['user_type']=user.user_type
            
            response={
                'status':True,
                'message':'Successfully logged in'
            }
           
    return JsonResponse(response)


def home_view(request):
    return render(request,'home/home.html')

def upload(request):
    return render(request,'home/upload.html')


    

def upload_form(request):
    return render(request,'home/upload_form.html')

def predict_form(request):
    if request.method == 'POST':
        constants = template_constants(request)
        form_elements = constants['form_elements']

        # Access submitted values
        # submitted_data = {element['key']: request.POST.get(element['key']) for element in form_elements}
        x_test = [request.POST.get(element['key']) for element in form_elements]
        # Example: Print submitted data (or process it)
        mood=request.POST["mood"]
        x_test.append(mood)
        print("x_test : ", x_test)
       
        predict_data = predict(x_test)
       
        result = "Not Found"
        output_classes=['Cycling','Gym Workout','None','Running','Swimming','Walking','Yoga']
        result=output_classes[predict_data]

        acivityList=Activity.objects.filter(activity_id=predict_data)
        video_id = []
        for activity in acivityList:
            video_url=activity.video_path
            video_id.append(video_url)  # Extracted video ID
        
        print("Result : ",result)  
        print(video_id)
        
        return render(request, 'home/result.html', {'video_ids': video_id,'result':result})
        # return JsonResponse({ 'status':True, 'message':"Success","result":result})
    else:
        return JsonResponse({ 'status':False, 'message':'Invalid Request Method!' })
    
def Package(request):
    return render(request,'home/package.html')

def activity(request,type):
    return render(request,'home/activity/activity_list.html',{'type':type})

def activity_part(request,act_type,part):
    category = activities[act_type]
    _activity = next((item for item in category if item["category"] == part), None)
    return render(request,'home/activity/activity.html',{'activities':_activity})