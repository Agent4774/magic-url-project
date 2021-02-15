from django.urls import path, re_path
from .views import (
	login, 
	home, 
	visits,
)

urlpatterns = [
    path('', login, name='login'),
    path('home/', home),
    path('visits/', visits)
]