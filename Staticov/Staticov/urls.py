from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('index', views.index, name='index'),
    path('indexcontact', views.indexcontact, name='indexcontact'),
    path('privacy', views.privacy, name='privacy'),
    path('rate', views.rate, name='rate'),
    path('AdminDash', views.CHANGE_MESSAGE_POPUP, name='AdminDash'),
    path('WorkerDash', views.WorkerDash, name='WorkerDash'),
    path('contact', views.contact, name='contact'),
    path('MainDashBoard', views.get_Main_dashboard, name='MainDashBoard'),
    path('registration_before_admin_approval', views.registration_before_admin_approval),
    path('login', views.login, name='login'),
    path('datapatient', views.datapatient, name='datapatient'),
    path('addpatient', views.addpatient,name='addpatient'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('change_password', views.CHANGE_PASSWORD, name='change_password'),
    path('changepassword',views.changepassword ,name='changepassword'),
    path('after_approuval_worker_insert', views.after_approuval_worker_insert),
    path('get_new_workers_table', views.get_new_workers_table),
    path('checksymptoms', views.check_symptomes),
    path('symptomesformcheck', views.symptomesformcheck),
    path('Deleteworker', views.Deleteworker),
    path('get_workers_table', views.get_workers_table),
    path('get_new_workers_table', views.get_new_workers_table),
    path('get_new_positiv_table', views.get_new_positiv_table),
    path('assign_patient', views.assign_patient),
    path('get_new_patient_table', views.get_new_patient_table),
    path('offer_shifts',views.offer_shifts),
    path('shift_offer',views.shift_offer),
    path('shift_offers',views.shift_offers),
    path('confirm_shift',views.confirm_shift),
    path('workerschedule',views.workerschedule),
    path('getcivilianlist',views.get_civilian_table),
]