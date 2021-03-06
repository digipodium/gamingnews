from django.urls import path
from django.urls.conf import include
from users import views
urlpatterns = [
    path('', views.index, name='index'), # landing page 
    path('dashboard/',views.dashboard, name='dashboard'), # auth'd user dashboard
    path('register/',views.register, name='register'), # register a new user
    path('oauth/',include("social_django.urls")), 
    path('search/api/',views.search, name='search'), # search for a news
]