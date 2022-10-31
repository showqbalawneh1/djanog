from django.urls import path , include 
from sensor import views

urlpatterns=[
    path('reading_calc_f/<str:since>/<str:until>/<str:calculation>',views.reading_calc_f,name="sensorRf"),
    path('home/' ,views.home , name ='home'),
    path("register/",views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),

]