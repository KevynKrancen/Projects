from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    path('home2', views.home2, name='home2'),
    path('login', views.login, name='login'),
    path('patient_test', views.patient_test, name='patient_test'),
    path('loginPagePatient', views.loginPagePatient, name='loginPagePatient'),
    path('login_patient', views.login_patient, name='login_patient'),
    path('Patient_Blood_Result', views.Patient_Blood_Result, name='Patient_Blood_Result'),
    path('Doctor_tranfert', views.Doctor_tranfert, name='Doctor_tranfert'),   
    path('Patientfile', views.Patientfile, name='Patientfile'), 
    path('addnewPat', views.addnewPat, name='addnewPat'),
    path('addNewpat', views.addNewpat, name='addNewpat'), 
    path('patient_spec', views.patient_spec, name='patient_spec'), 
    
]