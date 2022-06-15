from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('argentino/', views.argentino, name="Argentino"),
    path('extranjero/', views.extranjero, name="Extranjero"),
    path('nacionalizado/', views.nacionalizado, name= "Nacionalizado"),
    path('argentinoFormulario/', views.argentinoFormulario, name="ArgentinoFormulario"),
    path('extranjeroFormulario/', views.extranjeroFormulario, name="ExtranjeroFormulario"),
    path('nacionalizadoFormulario/', views.nacionalizadoFormulario, name="NacionalizadoFormulario"),  
    path('busquedaArgentino/', views.busquedaArgentino, name="BusquedaArgentino"),
    path('busquedaExtranjero/', views.busquedaExtranjero, name="BusquedaExtranjero"),
    path('busquedaNacionalizado/', views.busquedaNacionalizado, name="BusquedaNacionalizado"),
    path('buscarArgentino/', views.buscarArgentino),
    path('buscarExtranjero/', views.buscarExtranjero),
    path('buscarNacionalizado/', views.buscarNacionalizado),
    ]