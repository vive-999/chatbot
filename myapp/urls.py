from django.urls import path
from . import views

urlpatterns =[
    path("", views.home, name="home"),
    path("getResponse", views.getResponse, name="getResponse"),
    path("getWeather", views.getWeather, name="getWeather"),
    # path('blog/', views.blog, name = "blog"),
    # path('article/<int:article_id>', views.article, name ="article"),
]