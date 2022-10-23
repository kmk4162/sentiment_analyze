from django.shortcuts import render, redirect
from .models import Emotion
from .forms import EmotionForm

def index(request):
    import sys
    import requests
    import json
    client_id = "qaxffu4z5i"
    client_secret = "tzh2FdbETgDUPXoUXpy4NRabEnhdQ2c68ZaL0mto"
    url="https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Content-Type": "application/json"
    }
    content = Emotion.objects.order_by('-pk')[0].content
    # print(text)
    data = {
        "content": content,
    }
    print(json)
    print(json.dumps(data, indent=4, sort_keys=True))
    response = requests.post(url, data=json.dumps(data), headers=headers)
    rescode = response.status_code

    if(rescode == 200):
        print (response.text)
    else:
        print("Error : " + response.text)
    text = response.json()
    context = {
        'text' : text,
        'data' : data,
    }
    print(text)
    return render(request, 'emotions/index.html', context)

def create(request):
    if request.method == 'POST':
        emotion_form = EmotionForm(request.POST)
        if emotion_form.is_valid():
            emotion_form.save()
            return redirect('emotions:index')
    else:
        emotion_form = EmotionForm()
    context = {
        'emotion_form': emotion_form,
    }
    return render(request, 'emotions/create.html', context)