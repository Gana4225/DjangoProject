from django.urls import path
from . import views

urlpatterns = [
    path('', views.tt, name="index"),
    path('result/', views.base, name="lly"),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('profile/',views.profile,name='profile'),
    path('about/',views.about, name='about'),

]
