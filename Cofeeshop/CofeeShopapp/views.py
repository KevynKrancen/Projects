from random import random
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from CofeeShopapp.models import *
import mysql.connector
from django.http import JsonResponse
import random
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# Create your views here.

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database=" cofeeshop"
)
cursor = db_connection.cursor()
print(db_connection)

# START PAGE WITH ANIMATION


def homePage(request):
    allmenu = Menu.objects.all()
    return render(request, 'Restaurant/index.html', {"Menu": allmenu})


def Loginvippage(request):
    return render(request, 'Restaurant/viploginpage.html')


def loginPage(request):
    print("here")
    return render(request, 'loginpage.html')


def Choosetable(request):
    print("here")
    insidetable1 = insidetable.objects.all()
    return render(request, 'Restaurant/Choosetable.html', {"insidetable": insidetable1})
# def AdminDash(request):
# print("here")
# return render(request,'AdminDash/AdminDash.html')


def Tableadministration(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        admin1 = admin.objects.filter(ID=ID)
        insidetable1 = insidetable.objects.all()
        print(admin1)
        if admin1:
            return render(request, 'AdminDash/Tableadmin.html', {"admin": admin1, "insidetable": insidetable1})
        else:
            return render(request, 'loginpage.html')


def Tableinformation(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        TableID = request.POST.get('TableID')
        print(TableID)
        admin1 = admin.objects.filter(ID=ID)
        insidetable1 = insidetable.objects.filter(ID=TableID)
        print(admin1)
        if admin1:
            return render(request, 'AdminDash/Tableinformation.html', {"admin": admin1, "insidetable": insidetable1})
        else:
            return render(request, 'loginpage.html')


def Menuinformation(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        admin1 = admin.objects.filter(ID=ID)
        allmenu = Menu.objects.all()
        print(admin1)
        if admin1:
            return render(request, 'AdminDash/Menuinformation.html', {"admin": admin1, "Menu": allmenu})
    else:
        return render(request, 'loginpage.html')


def addCofee(request):
    print("here")
    return render(request, 'AdminDash/addCofee.html')


def login(request):
    # FOR ADMIN ONLY.
    if request.method == 'POST':
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        admins = admin.objects.filter(ID=ID, password=password)
        if admins:
            return render(request, 'AdminDash/AdminDash.html', {"admin": admins})
        barmaid1 = barmaid.objects.filter(ID=ID, password=password)
        if barmaid1:
            return render(request, 'BarmaidDash/BarmaidDash.html', {"barmaid": barmaid1})
        else:
            return render(request, 'loginpage.html')
    else:
        return render(request, 'loginpage.html')


def BarmaidTableList(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        barmaid1 = barmaid.objects.filter(ID=ID)
        allTables= insidetable.objects.all()
        allorder = order.objects.all()
        print(barmaid1)
        if barmaid1:
            return render(request, 'BarmaidDash/listoftables.html', {"barmaid": barmaid1, "insidetable": allTables , "order":allorder})
    else:
        return render(request, 'loginpage.html')


def register(request):
    if request.method == 'POST':
        saverecord = vipclient()
        saverecord.name = request.POST.get('name')
        saverecord.age = request.POST.get('age')
        saverecord.password = request.POST.get('password')
        saverecord.phone = request.POST.get('phone')
        saverecord.CN = 0
        saverecord.confirmation = 0
        saverecord.save()
        messages.success(request, 'הנתונים נשמרו בהצלחה!')
        return render(request, 'Restaurant/index.html')
    else:
        return homePage(request)


def viplogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        vipclient1 = vipclient.objects.filter(name=name, password=password)
        allMenu = Menu.objects.all() 
        MenuPrice=Menu.objects.all().order_by("price")
        MenuPopularity=Menu.objects.all().order_by("popularity")
        if vipclient1:
            return render(request, 'Restaurant/indexvip.html', {"vipclient": vipclient1, "Menu": allMenu})
        else:
            return homePage(request)


def changetable(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        TableID = request.POST.get('TableID')
        print(TableID)
        admin1 = admin.objects.filter(ID=ID)
        insidetable1 = insidetable.objects.filter(ID=TableID)
        print(admin1)
        if admin1:
            return render(request, 'AdminDash/ChangeTable.html', {"admin": admin1, "insidetable": insidetable1})


def changeMenu(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        menid = request.POST.get('menu')
        print(menid)
        admin1 = admin.objects.filter(ID=ID)
        Menu1 = Menu.objects.filter(ID=menid)
        if admin1:
            return render(request, 'AdminDash/ChangeMenu.html', {"admin": admin1, "Menu": Menu1})

def menuChange(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        avaibility = request.POST.get('avaibility')
        description = request.POST.get('description')
        ID = request.POST.get('ID')
        MID = request.POST.get('MID')   
        admin1 = admin.objects.filter(ID=ID)
        cursor.execute("UPDATE `menu` SET `price` = '%s' WHERE `menu`.`ID` = '%s';"%(price,MID))
        db_connection.commit()
        cursor.execute("UPDATE `menu` SET `avaibility` = '%s' WHERE `menu`.`ID` = '%s';"%(avaibility,MID))
        db_connection.commit()
        cursor.execute("UPDATE `menu` SET `description` = '%s' WHERE `menu`.`ID` = '%s';"%(description,MID))
        db_connection.commit()
        Menu1 = Menu.objects.all()
        if admin1:
            return render(request, 'AdminDash/Menuinformation.html', {"admin": admin1, "Menu": Menu1})

def payement(request):
    return render(request, 'Restaurant/payement.html')


def RegularCustomer(request):
    if request.method == 'POST':
        TID = request.POST.get('TID')
        cursor.execute("SELECT * FROM ` insidetable`")
        data = cursor.fetchall()  
        for item in data:
            ID,occupied,places,type=item
            if ID==ID:
                cursor.execute("UPDATE ` insidetable` SET `Occupied` = 'in order' WHERE ` insidetable`.`ID` = '%s';"%(TID))
                db_connection.commit()
        saverecord = order()
        saverecord.TABLE = request.POST.get('TID')
        saverecord.price = 0
        saverecord.vip = 'no'
        saverecord.save()
        allMenu = Menu.objects.all()
        MenuPrice=Menu.objects.all().order_by("price")
        MenuPopularity=Menu.objects.all().order_by("-popularity")
        insidetable1 = insidetable.objects.filter(ID=TID) 
        orderEnCour =  order.objects.filter(TABLE=TID)
        return render(request, 'Restaurant/RegularCustomer.html', {"insidetable": insidetable1, "Menu1": MenuPopularity, "Menu2": MenuPrice, "Menu3": allMenu,"order":orderEnCour })


def addToOrderNotVip(request): 
    if request.method == 'POST':
        tables=request.POST.get('tid')
        Menus=request.POST.get('MID')
        ArticlePrice=request.POST.get("Article")
        x=int(ArticlePrice)
        print(x)
        orderEnCour = order.objects.filter(TABLE=tables)
        insidetable1 = insidetable.objects.filter(ID=tables)
        print(insidetable1)
        allMenu = Menu.objects.all() 
        MenuPrice=Menu.objects.all().order_by("price")
        MenuPopularity=Menu.objects.all().order_by("popularity")
        if orderEnCour :
                cursor.execute("SELECT * FROM `order`")
                data = cursor.fetchall()
                for item in data:
                    OID,MID,TABLE,price,vip=item
                    if TABLE==TABLE:
                        MID = MID+","+Menus
                        cursor.execute("UPDATE `order` SET `MID` = '%s' WHERE `order`.`TABLE` = '%s';"%(MID,tables)) 
                        db_connection.commit()
                        y=int(price)
                        print(y)
                        newprice=y+x
                        cursor.execute("UPDATE `order` SET `price` = '%d' WHERE `order`.`TABLE` = '%s';"%(newprice,tables))
                        db_connection.commit()
                        cursor.execute("UPDATE ` insidetable` SET `Occupied` = 'occuper' WHERE ` insidetable`.`ID` = '%s';"%(TABLE))
                        db_connection.commit()
        return render(request, 'Restaurant/RegularCustomer.html', {"insidetable": insidetable1, "Menu1": MenuPopularity, "Menu2": MenuPrice, "Menu3": allMenu, "order":orderEnCour })

def payementPage(request):
    if request.method == 'POST':
        finishedOrder=request.POST.get("OID")
        print(finishedOrder)
        payement = order.objects.filter(OID=finishedOrder)
        allMenu = Menu.objects.all() 
        return render(request, 'Restaurant/payement.html',{"order":payement,"Menu":allMenu})


def deletetable(request):
    if request.method == 'POST':
        ID=request.POST.get("ID")
        admin1 = admin.objects.filter(ID=ID)
        insidetable1 = insidetable.objects.filter(occupied='Free')
        print(admin1)
        if admin1:
            return render(request, 'AdminDash/Deletetable.html', {"admin": admin1, "insidetable": insidetable1})


def byebye(request):
       if request.method == 'POST':
        ID=request.POST.get("ID")
        Tableid=request.POST.get("TableID")
        insidetable1 = insidetable.objects.filter(occupied='Free')
        admin1 = admin.objects.filter(ID=ID)
        cursor.execute("DELETE FROM ` insidetable` WHERE ` insidetable`.`ID` = %s"%(Tableid)) 
        db_connection.commit()
        return render(request, 'AdminDash/Deletetable.html', {"admin": admin1, "insidetable": insidetable1})

def addtablepage(request):
    if request.method == 'POST':
        ID=request.POST.get("ID")
        IDD=int(ID)
        admin1 = admin.objects.filter(ID=IDD)
        if admin1:
            return render(request, 'AdminDash/addtablepage.html', {"admin": admin1})

def addtable(request):
    if request.method == 'POST':
        print("HEre")
        places=request.POST.get("places")
        type=request.POST.get("type")
        ID=request.POST.get("ID")
        admin1 = admin.objects.filter(ID=ID)
        insidetable1 = insidetable.objects.all()
        saveobject=insidetable()
        saveobject.places=places
        saveobject.type=type
        saveobject.occupied='Free'
        saveobject.save()
        return render(request, 'AdminDash/AdminDash.html', {"admin": admin1, "insidetable": insidetable1})  

def addmenunpage(request):
    if request.method == 'POST':
        if request.method == 'POST':
            ID=request.POST.get("ID")
            admin1 = admin.objects.filter(ID=ID)
            if admin1:
                return render(request, 'AdminDash/addmenupage.html', {"admin": admin1})

def addmenu(request):
    if request.method == 'POST':
        saveobject=Menu()
        ID=request.POST.get("ID")
        saveobject.name=request.POST.get("name")
        saveobject.type=request.POST.get("type")
        saveobject.price=request.POST.get("price")
        saveobject.alcool=request.POST.get("alcool")
        saveobject.avaibility=1
        saveobject.popularity=0
        if saveobject.type == 'coffee':
            saveobject.photo='HomepageS/img/cafe.png'
        if saveobject.type == 'salad':
            saveobject.photo='HomepageS/img/salat.png'
        if saveobject.type == 'sandwich':
            saveobject.photo='HomepageS/img/sand.png'
        if saveobject.type == 'alcool':
            saveobject.photo='HomepageS/img/alc.png'
        saveobject.description=request.POST.get('description')
        saveobject.save()
        admin1 = admin.objects.filter(ID=ID)
        allMenu = Menu.objects.all() 
        if admin1:
            return render(request, 'AdminDash/Menuinformation.html', {"admin": admin1, "Menu": allMenu})
        
def takeorderdm(request):
    if request.method == 'POST':
        test=request.POST.get('TableID')
        testOrder=order.objects.filter(TABLE=test)
        cursor.execute("UPDATE ` insidetable` SET `Occupied` = 'in order' WHERE ` insidetable`.`ID` = '%s';"%(test))
        db_connection.commit()
        if not testOrder:
            saverecord = order()
            saverecord.TABLE = request.POST.get('TableID')
            saverecord.price = 0
            saverecord.vip = 'no'
            saverecord.save()
        orderencour=order.objects.filter(TABLE=test)
        ID=request.POST.get("ID")
        Tableid=request.POST.get("TableID")
        allMenu = Menu.objects.all()
        insidetable1 = insidetable.objects.filter(occupied='Free')
        barm = barmaid.objects.filter(ID=ID)
        print(barm)
        return render(request, 'BarmaidDash/takeorderbm.html', {"barmaid": barm, 'insidetable':insidetable1,'Menu':allMenu, 'order':orderencour })

def Addorder(request):
     if request.method == 'POST':
        tables=request.POST.get('tid')
        Menus=request.POST.get('MID')
        ArticlePrice=request.POST.get("Article")
        print(ArticlePrice)
        ID=request.POST.get("ID")
        barm = barmaid.objects.filter(ID=ID)
        x=int(ArticlePrice)
        print(x)
        orderEnCour = order.objects.filter(TABLE=tables)
        insidetable1 = insidetable.objects.filter(ID=tables)
        print(insidetable1)
        allMenu = Menu.objects.all() 
        if orderEnCour :
                cursor.execute("SELECT * FROM `order`")
                data = cursor.fetchall()
                for item in data:
                    OID,MID,TABLE,price,vip=item
                    if TABLE==TABLE:
                        MID = MID+","+Menus
                        cursor.execute("UPDATE `order` SET `MID` = '%s' WHERE `order`.`TABLE` = '%s';"%(MID,tables)) 
                        db_connection.commit()
                        y=int(price)
                        print(y)
                        newprice=y+x
                        cursor.execute("UPDATE `order` SET `price` = '%d' WHERE `order`.`TABLE` = '%s';"%(newprice,tables))
                        db_connection.commit()
                        cursor.execute("UPDATE ` insidetable` SET `Occupied` = 'occuper' WHERE ` insidetable`.`ID` = '%s';"%(TABLE))
                        db_connection.commit()
        return render(request, 'BarmaidDash/takeorderbm.html', {"insidetable": insidetable1, "barmaid": barm, "order":orderEnCour,'Menu':allMenu })

def ChangeTable(request):
     if request.method == 'POST':
        place=request.POST.get('place')
        type=request.POST.get('type')
        occupied=request.POST.get('occupied')
        TID=request.POST.get('TID')
        ID=request.POST.get('ID')
        print(place,type,occupied,TID,ID)  
        cursor.execute("UPDATE ` insidetable` SET `places` = '%s' WHERE ` insidetable`.`ID` = '%s';"%(place,TID))
        db_connection.commit()
        cursor.execute("UPDATE ` insidetable` SET `type`  = '%s' WHERE ` insidetable`.`ID` = '%s';"%(type,TID))
        db_connection.commit()
        cursor.execute("UPDATE ` insidetable` SET `occupied`  = '%s' WHERE ` insidetable`.`ID` = '%s';"%(occupied,TID))
        db_connection.commit()
        admin1 = admin.objects.filter(ID=ID)
        insidetable1 = insidetable.objects.all()
        return render(request, 'AdminDash/Tableadmin.html',{"admin": admin1, "insidetable": insidetable1})

def NewCustomers(request):
    if request.method == 'POST':
        ID=request.POST.get('ID')
        TableID=request.POST.get('TableID')
        barmaid1 = barmaid.objects.filter(ID=ID)
        table=insidetable.objects.filter(ID=TableID)
        return render(request, 'BarmaidDash/NewCustomer.html',{"barmaid": barmaid1,"Table": table})

def NeworderforVIP(request):
     if request.method == 'POST':
        test=request.POST.get('TableID')
        vipphone=request.POST.get('VIPPHONE')
        testOrder=order.objects.filter(TABLE=test)
        VIP=vipclient.objects.filter(phone=vipphone)
        cursor.execute("UPDATE ` insidetable` SET `Occupied` = 'in order' WHERE ` insidetable`.`ID` = '%s';"%(test))
        db_connection.commit()
        if not testOrder:
            saverecord = order()
            saverecord.TABLE = request.POST.get('TableID')
            saverecord.price = 0
            saverecord.vip = vipphone
            saverecord.save()
        orderencour=order.objects.filter(TABLE=test)
        ID=request.POST.get("ID")
        Tableid=request.POST.get("TableID")
        allMenu = Menu.objects.all()
        insidetable1 = insidetable.objects.filter(occupied='Free')
        barm = barmaid.objects.filter(ID=ID)
        print(barm)
        return render(request, 'BarmaidDash/OrderVIP.html', {"barmaid": barm, 'insidetable':insidetable1,'Menu':allMenu, 'order':orderencour, 'vip':VIP })

def AddorderVIP(request):
     if request.method == 'POST':
        tables=request.POST.get('tid')
        Menus=request.POST.get('MID')
        ArticlePrice=request.POST.get("Article")
        Vipphone=request.POST.get("Vi")
        Menutype=request.POST.get("type")
        VIP=vipclient.objects.filter(phone=Vipphone).first()
        CN=VIP.CN
        if Menutype == 'coffee':
            cursor.execute("UPDATE ` vipclient` SET `CN` = '%d' WHERE ` vipclient`.`phone` = '%s';"%(CN+1,Vipphone)) 
            db_connection.commit()
        print(ArticlePrice)
        ID=request.POST.get("ID")
        barm = barmaid.objects.filter(ID=ID)
        x=int(ArticlePrice)
        print(x)
        orderEnCour = order.objects.filter(TABLE=tables)
        insidetable1 = insidetable.objects.filter(ID=tables)
        VIP=vipclient.objects.filter(phone=Vipphone)
        print(insidetable1)
        allMenu = Menu.objects.all() 
        if orderEnCour :
                cursor.execute("SELECT * FROM `order`")
                data = cursor.fetchall()
                for item in data:
                    OID,MID,TABLE,price,vip=item
                    if TABLE==TABLE:
                        MID = MID+","+Menus
                        cursor.execute("UPDATE `order` SET `MID` = '%s' WHERE `order`.`TABLE` = '%s';"%(MID,tables)) 
                        db_connection.commit()
                        y=int(price)
                        print(y)
                        newprice=y+x
                        cursor.execute("UPDATE `order` SET `price` = '%d' WHERE `order`.`TABLE` = '%s';"%(newprice,tables))
                        db_connection.commit()
                        cursor.execute("UPDATE ` insidetable` SET `Occupied` = 'occuper' WHERE ` insidetable`.`ID` = '%s';"%(TABLE))
                        db_connection.commit()
        return render(request, 'BarmaidDash/OrderVIP.html', {"barmaid": barm, 'insidetable':insidetable1,'Menu':allMenu, 'order':orderEnCour, 'vip':VIP })


def payementBM(request):
    if request.method == 'POST':
        BID=request.POST.get('ID')
        tables=request.POST.get('TableID')
        OID=request.POST.get("OID")
        VIP=order.objects.filter(OID=OID).first()
        orderEnCour=order.objects.filter(OID=OID)
        barm=barmaid.objects.filter(ID=BID)
        allMenu = Menu.objects.all() 
        insidetable1 = insidetable.objects.filter(ID=tables)
        vipc=VIP.vip
        VIP=vipclient.objects.filter(phone=vipc)
        print(VIP)
        if vipc != 'no':
            return render(request, 'BarmaidDash/OrderVIP.html', {"barmaid": barm, 'insidetable':insidetable1,'Menu':allMenu, 'order':orderEnCour, 'vip':VIP })
        else :
            return render(request, 'BarmaidDash/takeorderbm.html', {"barmaid": barm, 'insidetable':insidetable1,'Menu':allMenu, 'order':orderEnCour})


def PAYNOWVIP(request):
    if request.method == 'POST':
        OID=request.POST.get('OID')
        Viphone=order.objects.filter(OID=OID).first()
        Vipphone=Viphone.vip
        orderEnCour=order.objects.filter(OID=OID)
        VIP=vipclient.objects.filter(phone=Vipphone)
        VIPreduct=order.objects.filter(OID=OID).first()
        VIPreduction=VIPreduct.price
        FINALPRICE=VIPreduction*0.85
        final = { FINALPRICE: 1 }
        return render(request, 'Restaurant/payementvip.html',{"order":orderEnCour,"vip":VIP , "lastprice":final })


def PAYNOWREGULAR(request):
    if request.method == 'POST':
        OID=request.POST.get('OID')
        VIPreduct=order.objects.filter(OID=OID).first()
        VIPreduction=VIPreduct.price
        FINALPRICE=VIPreduction*1.15
        final = { FINALPRICE: 1 }
        orderEnCour=order.objects.filter(OID=OID)
        print(orderEnCour)
        return render(request, 'Restaurant/payementregular.html',{"order":orderEnCour,"lastprice":final})


def paying(request):
    if request.method == 'POST':
        OID=request.POST.get('OID')
        table=order.objects.filter(OID=OID).first()
        table=table.TABLE
        cursor.execute("UPDATE ` insidetable` SET `occupied` = 'Free' WHERE ` insidetable`.`ID` = '%s';"%(table))
        db_connection.commit()
        cursor.execute("DELETE FROM `order` WHERE `order`.`OID` = '%s';"%(OID))
        db_connection.commit()
        return render(request, 'Restaurant/index.html')

def makeviporder(request):
    if request.method == 'POST':
        ID=request.POST.get('ID')
        vip = vipclient.objects.filter(ID=ID)
        insidetable1 = insidetable.objects.all()
        return render(request, 'Restaurant/Choosetablevip.html', {"insidetable": insidetable1 , "VIP":vip })

def Viporder(request):
    if request.method == 'POST':
        TID=request.POST.get('TID')
        CID=request.POST.get('CID')
        clients=vipclient.objects.filter(ID=CID).first()
        clientphone=clients.phone
        testOrder=order.objects.filter(TABLE=TID)
        cursor.execute("UPDATE ` insidetable` SET `Occupied` = 'in order' WHERE ` insidetable`.`ID` = '%s';"%(TID))
        if not testOrder:
            saverecord = order()
            saverecord.TABLE = request.POST.get('TID')
            saverecord.price = 0
            saverecord.vip = clientphone
            saverecord.save()
        allMenu = Menu.objects.all() 
        MenuPrice=Menu.objects.all().order_by("price")
        MenuPopularity=Menu.objects.all().order_by("popularity")
        vip = vipclient.objects.filter(ID=CID)
        orderEnCour=order.objects.filter(TABLE=TID)
        return render(request, 'Restaurant/viporders.html', {"Menu1": MenuPopularity, "Menu2": MenuPrice, "Menu3": allMenu,"order":orderEnCour, "vipclient":vip })

def addViporder(request):
    if request.method == 'POST':
        Menus=request.POST.get('MID')
        orders=request.POST.get('OID')
        MenuArt=Menu.objects.filter(ID=Menus).first()
        orders1=order.objects.filter(OID=orders).first()
        vipclient1=orders1.vip
        orderTable=orders1.TABLE
        orderMID=orders1.MID+","+Menus
        orderPrice=orders1.price
        price=MenuArt.price+orderPrice
        cursor.execute("UPDATE ` insidetable` SET `Occupied` = 'occuper' WHERE ` insidetable`.`ID` = '%s';"%(orderTable))
        db_connection.commit()
        cursor.execute("UPDATE `order` SET `MID` = '%s' WHERE `order`.`TABLE` = '%s';"%(orderMID,orderTable)) 
        db_connection.commit()
        cursor.execute("UPDATE `order` SET `price` = '%s' WHERE `order`.`TABLE` = '%s';"%(price,orderTable)) 
        db_connection.commit()
        allMenu = Menu.objects.all() 
        MenuPrice=Menu.objects.all().order_by("price")
        MenuPopularity=Menu.objects.all().order_by("popularity")
        vip = vipclient.objects.filter(phone=vipclient1)
        orderEnCour=order.objects.filter(OID=orders)
        print(vip)
        print(orderEnCour)
        return render(request, 'Restaurant/viporders.html', {"Menu1": MenuPopularity, "Menu2": MenuPrice, "Menu3": allMenu,"order":orderEnCour, "vipclient":vip })