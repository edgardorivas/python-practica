from django.urls import path
from . import views

urlpatterns = [
    path('saludar/<str:nombre>',views.hello)    
]
