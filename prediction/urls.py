from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('crop',views.crop, name="crop"),
    path('crop_result',views.crop_prediction,name ="crop_result"),
    path('fertilizer',views.fertilizer,name = "fertilizer"),
    path('fert_prediction',views.fert_recommend, name ="fert_prediction")
]
