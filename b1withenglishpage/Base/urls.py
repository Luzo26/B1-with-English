from cgitb import handler
from django.urls import path
from django.views import View
from . import views

app_name = 'Base'

urlpatterns = [
    path('', views.home, name="home"),
    path('cursos/', views.cursos, name="Cursos"),
    path('contacto/', views.contacto, name="Contacto"),
    path('apuntarse/', views.apuntarse, name="apuntarse"),
    path('blog/',views.post_list,name="post_list"),
    path('<slug:post>/',views.post_detail,name="post_detail"),
    
]

handler404="Base.views.handle_not_found"