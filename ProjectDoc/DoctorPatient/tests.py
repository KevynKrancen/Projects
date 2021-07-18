from django.test import TestCase

# Create your tests here.
from django import urls
from django.db.models.fields import AutoField
from django.test import TestCase,SimpleTestCase
from django.urls import resolve, reverse
from DoctorPatient.views import *
from DoctorPatient.models import *
import unittest
from django.test.client import RequestFactory



class TestUrls(unittest.TestCase):

    def test_list_url_is_resolved(self):
        url=reverse('home')
        print("HOME PAGE TEST ++++++++++++++>")
        print(resolve(url))

class doctortest(TestCase):

    def test_doctorlogin(self):
       item=DoctorFormModel()
       item.ID=1
       item.name='kevyn123'
       item.DoctorID='332531235'
       item.password='101010'
       item.doctorName='Kevyn Krancenblum'
       item.save()
       record=DoctorFormModel.objects.get(ID=item.ID,DoctorID=item.DoctorID,password=item.password,name=item.name,doctorName=item.doctorName)
       self.assertEqual(record,item)

class Patienttest(TestCase):
    def test_patient_result(self):
        item=PatientsymptomesModel()
        item.ID=3
        item.name='keke'
        item.password='123456'
        item.taz='315199059'
        item.smoke="yes"
        item.age = "53"
        item.Origine = "Middle East"
        item.message = ''
        item.alk_phos = 100
        item.hdl = 29
        item.iron = 53
        item.creat =6.04
        item.hb = 59
        item.urea =9
        item.hct = 12
        item.rbc = 0.58
        item.lymph = 135
        item.neut =80
        item.wbc = 29
        item.gender = "male" 
        item.DoctorDescript = "nothing"
        item.testresult='nothing'
        item.Treatement=''
        item.save()
        symptomesformchecktest(item)
        result={
        'data': []
        }
        result['data'].append({
              'testresult':item.testresult,
            }) 
        print(result)  
