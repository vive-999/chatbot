import chatterbot
from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests
from requests.api import request



bot = ChatBot('vivebot',read_only = False, logic_adapters= ['chatterbot.logic.BestMatch'])
list_traiiner = ListTrainer(bot)

list_of_responses =[
    "What is your name?",
    "I am a chat bot",
    "What is your age?",
    "I am lifeless",
    "what do you do for living?",
    "I develop applicatioons",
    "you are a?",
    "I am a Mechanical engineer"
]
list_traiiner.train(list_of_responses)


# Create your views here.

def home(request):
    return render(request, "myapp/index.html")

def getResponse(request):
    
    userMessage = request.GET.get('userMessage')
    response = bot.get_response(userMessage)
    return HttpResponse(response)

def getNews(request):
    return HttpResponse("It's under development yet!")





def getWeather(request):
    lat_ = request.GET.get('lat')
    lon_ = request.GET.get('long')
    API_key= "4ab94d34eafe3bd329f1145033e7895c"
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat_}&lon={lon_}&units=metric&appid={API_key}")
    JsonWResponse = response.json()
    name = JsonWResponse['name']
    country = JsonWResponse['sys']['country']
    desc = JsonWResponse['weather'][0]['description']
    temp = JsonWResponse['main']['temp']

    print("Name", name)
    print("country", country)
    print("desc", desc)
    print("temperature", temp)
    return JsonResponse(JsonWResponse)




