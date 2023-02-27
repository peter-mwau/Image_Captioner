from django.shortcuts import render, redirect
# import requests, json, urllib
from django import forms
from .forms import  UserImage
from django.shortcuts import redirect, render  
# from .forms import UserImageForm
from .models import UploadImage
from django.views.decorators.csrf import csrf_exempt
import base64
from PIL import Image
from io import BytesIO
from .forms import UserImage

import json, requests, urllib

# Create your views here.

 
@csrf_exempt
def image_request(request):  
    if request.method == 'POST':  
        form = UserImage(request.POST, request.FILES)
        # img_url = ''
        if form.is_valid():   
            # get image url
            img_object = form.instance
            img_url =img_object.image.url
            encoded_image = base64.b64encode(img_object.image.read())
            # print(encoded_image)

            response = requests.post("https://elitecode-captioner.hf.space/run/predict", json={
            "data": [
                # userInput
                "data:image/jpg;base64," + encoded_image.decode('utf-8'),
            ]
            })
            # .json()
            
            # decoded_image = base64.b64decode(response["data"])
            # print(decoded_image)
  
            data = response.json()
            # print(data)
            # caption = data[0]
            # data = {'data': ['a close up of a dog wearing sunglasses . '], 'is_generating': False, 'duration': 54.236732721328735, 'average_duration': 71.11681790886638}

            # access the data key
            caption = data['data']
            # print(caption)

            # remove the brackets from the caption 
            caption = caption[0]
            # print(caption), 'img_url': img_url

            

            # data = response
            # print(caption)
            form.save()

            # return caption to the html page in the caption field
            # form = Caption(initial={'caption': caption})
            form = UserImage(initial={'caption': caption, 'image': img_url})

            # save to dbase
            # save = SaveData(Image=img_object.image, Caption=caption)
            # save.save()

              
            return render(request, 'index.html', {'form': form, 'caption': caption})
    else:  
        form = UserImage()  
  
    return render(request, 'index.html', {'form': form})









