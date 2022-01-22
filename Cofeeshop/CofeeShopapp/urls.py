
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
urlpatterns = [

    # The home page
    path('home', views.homePage, name='home'),
    path('loginPage',views.loginPage, name='loginPage'),
    path('login',views.login, name='login'),
##    path('AdminDash', views.AdminDash, name='AdminDash'),
    path('Tableadministration', views.Tableadministration, name='tables'),
    path('Tableinformation', views.Tableinformation, name='table'),
    path('Menuinformation', views.Menuinformation, name='menu'),
    path('addCofee', views.addCofee, name='addCofee'),
    path('BarmaidTableList', views.BarmaidTableList, name='BarmaidTableList'),
    path('register', views.register, name='register'),
    path('viplogin', views.viplogin, name='viplogin'), 
    path('Loginvippage', views.Loginvippage, name='Loginvippage'),
    path('changetable', views.changetable, name='changetable'),
    path('payement', views.payement, name='payement'),
    path('changeMenu', views.changeMenu, name='changeMenu'), 
    path('addToOrderNotVip', views.addToOrderNotVip, name='addToOrderNotVip'), 
    path('Choosetable', views.Choosetable, name='Choosetable'), 
    path('RegularCustomer', views.RegularCustomer, name='RegularCustomer'), 
    path('payementPage', views.payementPage, name='payementPage'), 
    path('deletetable', views.deletetable, name='deletetable'), 
    path('byebye', views.byebye, name='byebye'),
    path('addtable', views.addtable, name='addtable'),
    path('addtablepage', views.addtablepage, name='addtablepage'),
    path('addmenunpage', views.addmenunpage, name='addmenunpage'),
    path('addmenu', views.addmenu, name='addmenu'),
    path('takeorderdm', views.takeorderdm, name='takeorderdm'),
    path('Addorder', views.Addorder, name='Addorder'),
    path('ChangeTable', views.ChangeTable, name='ChangeTable'),
    path('menuChange', views.menuChange, name='menuChange'),
    path('NewCustomers', views.NewCustomers, name='NewCustomers'),
    path('NeworderforVIP', views.NeworderforVIP, name='NeworderforVIP'),
    path('AddorderVIP', views.AddorderVIP, name='AddorderVIP'),
    path('payementBM', views.payementBM, name='payementBM'),
    path('PAYNOWVIP', views.PAYNOWVIP, name='PAYNOWVIP'),
    path('PAYNOWREGULAR', views.PAYNOWREGULAR, name='PAYNOWREGULAR'),
    path('paying', views.paying, name='paying'),
    path('makeviporder', views.makeviporder, name='makeviporder'),
    path('Viporder', views.Viporder, name='Viporder'),
    path('addViporder', views.addViporder, name='addViporder'),
    
]
