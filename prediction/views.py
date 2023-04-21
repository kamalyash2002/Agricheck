from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from geeksforgeeks import settings
import requests

#code added by me
# Importing essential libraries and modules
import numpy as np
import pandas as pd
from utils.disease import disease_dic
from utils.fertilizer import fertilizer_dic
import config
import pickle
import io
import torch
from torchvision import transforms
from PIL import Image
from utils.model import ResNet9
# Create your views here.
# =======================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------
# Loading crop recommendation model

crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

# =========================================================================================

# Custom functions for calculations

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    # API key is yet to be to putted...
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None
    
    # ===============================================================================================

# RENDER PREDICTION PAGES

# render crop recommendation result page
def crop_prediction(request):
    title = 'Harvestify - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.POST.get('nitrogen'))
        P = int(request.POST.get('phosphorous'))
        K = int(request.POST.get('pottasium'))
        ph = float(request.POST.get('ph'))
        rainfall = float(request.POST.get('rainfall'))

        # state = request.form.get("stt")
        city = request.POST.get("city")

        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]
            context ={
                "prediction": final_prediction,
                "title" : title
            }
            return render(request,'crop_result.html',context)

        else:
            cxt ={
                "prediction": final_prediction,
                "title" : title
            }
            return render(request,'try_again.html', title=title)


# render fertilizer recommendation result page 

def fertilizer(request):
    return render(request,"fertilizer.html")

def fert_recommend(request):
    if request.method =="POST":
        title = 'Harvestify - Fertilizer Suggestion'
        crop_name =request.POST['cropname']
        N = int(request.POST['nitrogen'])
        P = int(request.POST['phosphorous'])
        K = int(request.POST['pottasium'])
        # ph = float(request.form['ph'])
        df = pd.read_csv('Data/fertilizer.csv')

        nr = df[df['Crop'] == crop_name]['N'].iloc[0]
        pr = df[df['Crop'] == crop_name]['P'].iloc[0]
        kr = df[df['Crop'] == crop_name]['K'].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        max_value = temp[max(temp.keys())]
        if max_value == "N":
            if n < 0:
                key = 'NHigh'
            else:
                key = "Nlow"
        elif max_value == "P":
            if p < 0:
                key = 'PHigh'
            else:
                key = "Plow"
        else:
            if k < 0:
                key = 'KHigh'
            else:
                key = "Klow"
        response = (fertilizer_dic[key])
        cxt = {
            "title": title,
            "recommendation":response
        }    
        return render(request,"fertilizer_result.html",cxt)
#simple functions for the rendering of webpages


def crop(request):
    return render(request,"crop.html")
