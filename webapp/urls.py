from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage),
    path('dashboard', views.dashboard),
    path('sign-in', views.sign_in, name='sign-in'),
    path('add-doctor', views.add_doctor),
    path('add-patient', views.add_patient),
    path('suggest-doctor', views.suggest_doctor),
    path('appointment', views.appointment),
    path('feedback', views.feedback)
]