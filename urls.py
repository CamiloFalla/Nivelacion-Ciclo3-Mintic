from django.urls import path

from gestionServicios import views

urlpatterns = [ 
    path('', views.home, name="home"),
    path('ServiciosEPS', views.ServiciosEPS, name="ServiciosEPS"),
    path('EPS', views.EPS, name="EPS"),
    path('User', views.User, name="User"),
    path('MovimientosEPS', views.MovimientosEPS, name="MovimientosEPS"),
    path('Empleado', views.Empleado, name="Empleado"),
]