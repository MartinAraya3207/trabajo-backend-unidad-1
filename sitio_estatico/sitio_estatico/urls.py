from django.contrib import admin
from django.urls import path

from mi_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/<int:id>/', views.detalle_servicio, name='detalle_servicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('admin/', admin.site.urls),
]
