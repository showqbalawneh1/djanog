from django.http import HttpResponse
from django.shortcuts import render,redirect
import logging
from .models import pressureSensor,sensorReading
from django.http import HttpResponse
from django.db.models import Sum,Avg
import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login ,logout ,authenticate
from django.contrib import messages
from sensor.forms import NewUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.
log = logging.getLogger(__name__)
count = 0


@login_required(login_url='/sensor/accounts/login/')

def reading_calc_f(request, *args , **kwargs ):
        global count 
        if (kwargs['since']>=kwargs['until']):
            val=0
            messages="since > until "
            return render(request,"main/sensorR.html",{"operation": operation ,"value":val, message:"message"})
        
        
        since = datetime.datetime.fromisoformat(kwargs['since'])
        until = datetime.datetime.fromisoformat(kwargs['until'])
        q=sensorReading.objects.filter(readingDate__range=[since, until])
        operation= kwargs['calculation']
        if operation == 'sum':
            value= q.aggregate(Sum('value'))
            val=value['value__sum']
        elif operation == 'avg':
            value = q.aggregate(Avg('value'))
            val=value['value__avg']
        else :
            val=0
        count = count+1 
        log.info("this is calc function"+str(count))
        return render(request,"main/sensorR.html",{"operation": operation ,"value":val})
    


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

    

# def logout_request(request):
#     logout(request)
#     messages.info(request, "logged out successfully!")
#     return redirect("sensor:home")

# def login_request(request):
#     if request.method=="POST":
#         u= AuthenticationForm(request, data=request.POST)
#         if u.is_valid():
#             username=u.cleaned_data.get('username')
#             password=u.cleaned_data.get('password')
#             user=authenticate(username=username,password=password)
#             if user is not None:
#                 login(request, user)  
#                 messages.info(request, f"success login {username}" )
#                 return redirect("sensor:home")
#             else:
#                 messages.error (request, "invalid username or password ")
#         else:
#             messages.error (request, "invalid username or password ")
           
#     form=AuthenticationForm    
#     return render(request=request, template_name="main/login.html",context={"form":form})


def home(request):
    return render(request, template_name='main/home.html')