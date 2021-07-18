from django import urls
from django.db.models.fields import AutoField
from django.test import TestCase,SimpleTestCase
from django.urls import resolve, reverse
from Staticov.views import *
from Staticov.models import *
import unittest
from django.test.client import RequestFactory



class TestUrls(unittest.TestCase):

    def test_list_url_is_resolved(self):
        url=reverse('home')
        url1=reverse('registration')
        url2=reverse('AdminDash')
        url3=reverse('index')
        url4=reverse('privacy')
        url5=reverse('rate')
        url6=reverse('AdminDash')
        url7=reverse('WorkerDash')
        url9=reverse('contact')
        url10=reverse('MainDashBoard')
        url12=reverse('login')
        url13=reverse('datapatient')
        url14=reverse('addpatient')
        url15=reverse('add_patient')
        url16=reverse('change_password')
        url17=reverse('changepassword')
        print(resolve(url))
        print(resolve(url1))
        print(resolve(url2))
        print(resolve(url3))
        print(resolve(url4))
        print(resolve(url5))
        print(resolve(url6))
        print(resolve(url7))
        print(resolve(url9))
        print(resolve(url10))
        print(resolve(url12))
        print(resolve(url13))
        print(resolve(url14))
        print(resolve(url15))
        print(resolve(url16))
        print(resolve(url17))

class workerstest(TestCase):

    def test_workers(self):
       item=WorkersModel()
       item.ID=1
       item.name='jean'
       item.taz='123456789'
       item.password='123456'
       item.Type='admin'
       item.save()
       record= WorkersModel.objects.get()
       print("WORKS")
       self.assertEqual(record,item)

    def test_workersslug(self):
       item=WorkersModel()
       item.ID=1
       item.name='jean'
       item.taz='123456789'
       item.password='123456'
       item.Type='admin'
       item.save()

       self.assertEqual(item.name, 'jean')

class registertest(TestCase):

    def test_register(self):
       item=RegisterFormModel()
       item.ID=1
       item.name='jean'
       item.taz='123456789'
       item.password='123456'
       item.Type='civilian'
       item.civiliantype='student'
       item.save()
       record= RegisterFormModel.objects.get()
       print("HERRE")
       self.assertEqual(record,item)

    def test_registrationslug(self):
       item=RegisterFormModel()
       item.ID=1
       item.name='jean'
       item.taz='123456789'
       item.password='123456'
       item.Type='admin'
       item.civiliantype='student'
       item.save()
       self.assertNotEquals(item.civiliantype, 'jean')

class Popup_test(TestCase):

    def test_Popup(self):
        item=Popup()
        item.mid=3
        item.popupmsg="TESTINGHERE"
        item.save()
        record = Popup.objects.get()
        self.assertEqual(item,record)

    def test_Popup_false(self):
        item=Popup()
        item.mid=3
        item.popupmsg="TESTINGHERE"
        item.save()
        self.assertNotEquals(item.popupmsg, 'jean')

class worker_register_test(TestCase):
    def test_worker_register(self):
        item=worker_register()
        item.ID=3
        item.name='keke'
        item.password='123456'
        item.userid='315199059'
        item.save()
        record=worker_register.objects.get()
        self.assertEqual(item,record)

    def test_worker_register_false(self):
        item=worker_register()
        item.ID=3
        item.name='keke'
        item.password='123456'
        item.userid='315199059'
        item.save()
        self.assertNotEquals(item.userid, '929292929')

class SymptomesFormModeltest(TestCase):
    def test_SymptomesFormModel(self):
        item=SymptomesFormModel()
        item.head="כן"
        item.hot="כן"
        item.hurts="כן"
        item.smell="כן"
        item.ID=3
        item.save()
        record=SymptomesFormModel.objects.get()
        self.assertEqual(item,record)

class emploiedutemp_test(TestCase):
    def test_emploiedutemp(self):
        item=emploiedutemp()
        item.ID=3
        item.startdate='2020/3/1'
        item.enddate='2020/3/2'
        item.workerid='315199059'
        item.confirmation='אשר'
        item.save()
        record=emploiedutemp.objects.get()
        self.assertEqual(item,record)
        
class CivilianModelTest(TestCase):
    def test_CivilianModel(self):
        item=CivilianModel()
        item.ID=3
        item.taz='315199059'
        item.age=26
        item.place='חיפה'
        item.date='2020-6-1'
        item.religion='חרדי'
        item.save()
        record=CivilianModel.objects.get()
        self.assertEqual(item,record)

class IndexFormModelTest(TestCase):
    def test_IndexFormModel(self):
        item=IndexFormModel()
        item.ID=3
        item.name='keke'
        item.taz='315199059'
        item.telephone='0524840194'
        item.symptomes='יש'
        item.age='120'
        item.workerid=20
        item.save()
        record=IndexFormModel.objects.get()
        self.assertEqual(item,record)