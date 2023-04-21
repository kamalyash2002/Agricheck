from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home',views.home, name= 'homepage'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('services',views.services,name="services"),
    path('contactus',views.contactus,name="contactus"),
    path('contactsubmit',views.message,name="contactsubmit"),
    path('agricheck',views.agricheck,name="agricheck"),
    path('agridata',views.agridata,name="agridata"),
    path('expert_advice',views.expert_advice,name = "expert_advice"),
    path('expert_funct',views.expert_funct,name = "expert_funct")
]
