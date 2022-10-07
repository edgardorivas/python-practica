from django.urls import path
from . import views

urlpatterns = [
    path('saludar/<str:nombre>',views.hello), 
    path('tipos/',views.registros),
    path('tipos/<int:id>',views.unRegistro), 
    path('tipos/eliminar/<int:id>',views.eliminar), 

]
