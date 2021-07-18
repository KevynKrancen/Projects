from random import random
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from DoctorPatient.models import DoctorFormModel
from DoctorPatient.models import PatientsymptomesModel
import mysql.connector
from django.http import JsonResponse
import requests
import random


# Create your views here.

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database=" doctorpatient"
)
cursor = db_connection.cursor()
print(db_connection)

# START PAGE WITH ANIMATION
def home(request):
    return render(request,'loginPage.html')

def home2(request):
    return render(request,'home.html')

def loginPagePatient(request):
    return render(request,'loginPagePatient.html')

def Patient_Blood_Result(request):
    if request.method=='POST':
        Taz=request.POST.get('taz')
        print(Taz)
        Patient=PatientsymptomesModel.objects.filter(taz=Taz)
        print(Taz)
        return render(request,'PatientBloolResult.html',{"PatientsymptomesModel":Patient})
    else :
        return loginPagePatient(request)

def login_patient(request):
    cursor.execute("SELECT * FROM patientsymptomes")
    data = cursor.fetchall()
    if request.method=='POST':
        Taz=request.POST.get('taz')
        Patient=PatientsymptomesModel.objects.filter(taz=Taz)
        if not Patient:
            messages.error(request,'Wrong details ! try again')  
            return loginPagePatient(request)
        else:
            print(Taz)
            return render(request,'patientCrmform.html',{"PatientsymptomesModel":Patient})


def login(request):
    if request.method=='POST':
        Name=request.POST.get('name')
        DoctorID=request.POST.get('Doctorid')
        Password=request.POST.get('password')
        doctor=DoctorFormModel.objects.filter(DoctorID=DoctorID,password=Password,name=Name)
        print(doctor)
        if not doctor:
            messages.error(request,'Wrong details ! try again')   
            return home(request) 
        else:
            print("im here empty")
            return render(request,'dashboard.html', {"DoctorFormModel":doctor})
    else:
        messages.error(request,'Error ! try again')   
        return home(request)
        

def addnewPat(request):
    if request.method=='POST':
        Taz=request.POST.get('taz')
        doctor=DoctorFormModel.objects.filter(DoctorID=Taz)
        return render(request,'Addnewpatient.html',context={"DoctorFormModel":doctor})
    else :
        return home(request)

def Doctor_tranfert(request):
    if request.method=='POST':
        Taz=request.POST.get('taz')
        doctor=DoctorFormModel.objects.filter(DoctorID=Taz)
        print(doctor)
        allPat=PatientsymptomesModel.objects.all()
        print(allPat)
        return render(request,'patientList.html',context={"DoctorFormModel":doctor,"PatientsymptomesModel":allPat})
    else :
        return home(request)

def Patientfile(request):
     if request.method=='POST':
        Taz=request.POST.get('taz')
        patID=request.POST.get('name')
        print(Taz)
        print(patID)
        symptomesformcheck()
        doctor=DoctorFormModel.objects.filter(DoctorID=Taz)
        Pat=PatientsymptomesModel.objects.filter(name=patID)
        return render(request,'patientList2.html',{"DoctorFormModel":doctor,"PatientsymptomesModel":Pat})
     else :
        return home(request)

def patient_spec(request):
    if request.method=='POST':
        Doctorid=request.POST.get('Doctorid')
        print(Doctorid)
        doctor=DoctorFormModel.objects.filter(DoctorID=Doctorid)
        Taz=request.POST.get('taz')
        Pat=PatientsymptomesModel.objects.filter(taz=Taz)
        MESSAGE=request.POST.get('message')
        cursor.execute("SELECT * FROM patientsymptomes")
        data = cursor.fetchall()    
        for item in data:
            ID,taz,name,smoke,age,Origine,message,alk_phos,hdl,iron,creat,hb,urea,hct,rbc,lymph,neut,wbc,testResult,gender,DoctorDescript,Treatement=item
            if  taz==Taz:
                cursor.execute("UPDATE `patientsymptomes` SET `DoctorDescript` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(MESSAGE,ID))
                db_connection.commit()
                return render(request,'patientList2.html',{"DoctorFormModel":doctor,"PatientsymptomesModel":Pat})

def patient_test(request):
    if request.method=='POST':
        Taz=request.POST.get('taz')
        Pat=PatientsymptomesModel.objects.filter(taz=Taz)
        MESSAGE=request.POST.get('message')
        cursor.execute("SELECT * FROM patientsymptomes")
        data = cursor.fetchall()    
        for item in data:
            ID,taz,name,smoke,age,Origine,message,alk_phos,hdl,iron,creat,hb,urea,hct,rbc,lymph,neut,wbc,testResult,gender,DoctorDescript,Treatement=item
            if  taz==Taz:
                cursor.execute("UPDATE `patientsymptomes` SET `message` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(MESSAGE,ID))
                db_connection.commit()
                return render(request,'patientCrmform.html',{"PatientsymptomesModel":Pat})
    else :
        return loginPagePatient(request)

def addNewpat(request):
    if request.method=='POST':
        saverecord=PatientsymptomesModel()
        saverecord.taz=request.POST.get('taz')
        saverecord.name=request.POST.get('name')
        saverecord.age=request.POST.get('age')
        saverecord.smoke=request.POST.get('smoke')
        saverecord.Origine=request.POST.get('Origine')
        saverecord.DoctorDescript=request.POST.get('message')
        saverecord.gender=request.POST.get('gender')
        saverecord.alk_phos=random.uniform(30,160)
        saverecord.hdl=random.uniform(25,86)
        saverecord.iron=random.uniform(50,180)
        saverecord.creat=random.uniform(0,1)
        saverecord.hb=random.uniform(10,20)
        saverecord.urea=random.uniform(15,46)
        saverecord.hct=random.uniform(30,57)
        saverecord.rbc=random.uniform(4,7)
        saverecord.lymph=random.uniform(36,52)
        saverecord.neut=random.uniform(28,54)
        saverecord.wbc=random.uniform(4500,19000)
        saverecord.testresult="test"
        saverecord.save()
        messages.success(request,'הנתונים נשמרו בהצלחה!')
        return render(request,'dashboard.html')
    else :
        return home(request)
##Symptome Test function 

def symptomesformcheck():
        cursor.execute("SELECT * FROM patientsymptomes")
        data = cursor.fetchall()
        for item in data:
            ID,taz,name,smoke,age,Origine,message,alk_phos,hdl,iron,creat,hb,urea,hct,rbc,lymph,neut,wbc,testResult,gender,DoctorDescript,Treatement=item
            cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '  ' WHERE `patientsymptomes`.`ID` = '%s';"%(ID))
            db_connection.commit()
            if  age<18 and (wbc<4500 or wbc>11000):
                desease= "זיהום/מחלת דם/סרטן"
                treatment="אנטיביוטיקה ייעודית/שילוב של ציקלופוספאמיד וקורטיקוסרואידים/אנטרקטיניב"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if age>=18 and wbc<4500:
              desease=  "מחלה ויראלית/סרטן"
              treatment="לנוח בבית/אנטרקטיניב"
              if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
              cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
              cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
              db_connection.commit()
            if age>=18 and wbc>11000:
                desease =  "זיהום/מחלת דם/סרטן"
                treatment="אנטיביוטיקה ייעודית/שילוב של ציקלופוספאמיד וקורטיקוסרואידים/אנטרקטיניב"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (age>=4 and age<=17) and wbc<5500:
                desease = "מחלה ויראלית/סרטן"
                treatment="לנוח בבית/אנטרקטיניב"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (age>=4 and age<=17) and wbc>15500:
                desease = "זיהום/מחלת דם/סרטן"
                treatment="אנטיביוטיקה ייעודית/שילוב של ציקלופוספאמיד וקורטיקוסרואידים/אנטרקטיניב"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (age>=0 and age<=3) and wbc<6000:
                desease = "מחלה ויראלית/סרטן"
                treatment="לנוח בבית/אנטרקטיניב"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (age>=4 and age<=17) and wbc>17500:
                desease = "זיהום/מחלת דם/סרטן"   
                treatment="אנטיביוטיקה ייעודית/שילוב של ציקלופוספאמיד וקורטיקוסרואידים/אנטרקטיניב"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if neut<28:
                desease = "זיהום/הפרעה ביצירת הדם/סרטן"
                treatment="אנטיביוטיקה ייעודית/כדור 10 מיליגרם של בי 12 וכדור 5 מיליגרם של חומצה פולית ביום למשך חודש/אנטרקטיניב"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if neut>54:
                desease ="זיהום"
                treatment="אנטיביוטיקה ייעודית"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if lymph<36:
                desease = "הפרעה ביצירת הדם"
                treatment="כדור 10 מיליגרם של בי 12 וכדור 5 מיליגרם של חומצה פולית ביום למשך חודש"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if lymph>52:
                desease = "זיהום/סרטן"
                treatment="אנטיביוטיקה ייעודית/אנטרקטיניב"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if rbc<4.5:
                desease = "אנמיה/דימום"
                treatment="שני כדורי 10 מיליגרם של בי 12 ביום למשך חודש/להתפנות בדחיפות לבית החולים"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if rbc>6:
                desease = "הפרעה ביצירת הדם/מעשנים/מחלת ריאות"
                treatment="כדור 10 מיליגרם של בי 12 וכדור 5 מיליגרם של חומצה פולית ביום במשך חודש/להפסיק לעשן/הפנייה לצילום רנטגן של הריאות"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if hct<37 and gender=='male':
                desease = "אנמיה/דימום"
                treatment="שני כדורי 10 מיליגרם של בי 12 ביום למשך חודש/להתפנות בדחיפות לבית החולים"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if hct>54 and gender=='male':
                desease = "מעשנים"
                treatment="להפסיק לעשן"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if hct<33 and gender=='female':
                desease = "אנמיה/דימום"
                treatment="שני כדורי 10 מיליגרם של בי 12 ביום למשך חודש/להתפנות בדחיפות לבית החולים"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if hct>47 and gender=='female':
                desease = "מעשנים"
                treatment="להפסיק לעשן"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if  Origine=="South Africa" and urea > 47 :
                desease = testResult+ "מחלת כליה/ התייבשות /דיאטה עתירת חלבונים"
                treatment="איזון את רמות הסוכר בדם/מנוחה מוחלטת בשכיבה, החזרת נוזלים בשתייה/לתאם פגישה עם תזונאי"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if  Origine=="Middle East" and (urea > 47):
                desease = "מחלת כליה/ התייבשות /דיאטה עתירת חלבונים"
                treatment="איזון את רמות הסוכר בדם/מנוחה מוחלטת בשכיבה, החזרת נוזלים בשתייה/לתאם פגישה עם תזונאי"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (Origine=="South Africa") and (urea < 18):
                desease = "תת תזונה\דיאטה דלת חלבון\מחלת כבד"
                treatment="לתאם פגישה עם תזונאי/הפנייה לאבחנה ספציפית לצורך קביעת טיפול"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (Origine=="Middle East") and (urea < 18):
                desease = "תת תזונה\דיאטה דלת חלבון\מחלת כבד"
                treatment="לתאם פגישה עם תזונאי/הפנייה לאבחנה ספציפית לצורך קביעת טיפול"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if  (urea > 43):
                desease = "תת תזונה\דיאטה דלת חלבון\מחלת כבד"
                treatment="לתאם פגישה עם תזונאי/הפנייה לאבחנה ספציפית לצורך קביעת טיפול"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if  (urea > 17):
                desease = "תת תזונה\דיאטה דלת חלבון\מחלת כבד"
                treatment="לתאם פגישה עם תזונאי/הפנייה לאבחנה ספציפית לצורך קביעת טיפול"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (age >= 0 or age <= 17) and (hb < 11.5):
                desease = testResult+ "אנמיה"
                treatment="שני כדורי 10 מיליגרם של בי 12 ביום במשך חודש"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if  age >= 18 and hb < 12 :
                desease = "אנמיה"
                treatment="שני כדורי 10 מיליגרם של בי 12 ביום במשך חודש"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if iron > 120:
                desease = "הרעלת ברזל"
                treatment="להתפנות לבית החולים"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if iron < 48:
                desease = "דימום\תת תזונה\מחסור בברזל"
                treatment="להתפנות בדחיפות לבית החולים/לתאם פגישה עם תזונאי/שני כדורי 10 מיליגרם של בי 12 ביום במשך חודש"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if iron < 60:
                desease = "דימום\תת תזונה\מחסור בברזל"
                treatment="להתפנות בדחיפות לבית החולים/לתאם פגישה עם תזונאי/שני כדורי 10 מיליגרם של בי 12 ביום במשך חודש"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (age >= 0 or age <= 2) and (creat > 0.5):
                desease = "מחלת כליה\צריכה מוגברת של בשר"
                treatment="איזון את רמות הסוכר בדם/לתאם פגישה עם תזונאי"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (age >= 0 or age <= 2) and (creat < 0.2):
                desease = "תת תזונה"
                treatment= "לתאם פגישה עם תזונאי"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (age >= 3 or age <= 17) and (creat > 1):
                desease = "מחלת כליה\צריכה מוגברת של בשר"
                treatment="איזון את רמות הסוכר בדם/לתאם פגישה עם תזונאי"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()              
            if (age >= 3 or age <= 17) and (creat < 0.5):
                desease = "תת תזונה"
                treatment="לתאם פגישה עם תזונאי"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()  
            if (age >= 18 or age <= 59) and (creat > 1):
                desease = "מחלת כליה\צריכה מוגברת של בשר"
                treatment="איזון את רמות הסוכר בדם/לתאם פגישה עם תזונאי"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit() 
            if (age >= 18 or age <= 59) and (creat > 0.6) :
                desease = "תת תזונה"
                treatment="לתאם פגישה עם תזונאי"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (age >= 60) and (creat > 1.2):
                desease = "מחלת כליה\צריכה מוגברת של בשר"
                treatment="איזון את רמות הסוכר בדם/לתאם פגישה עם תזונאי"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()             
            if (age >= 60) and (creat < 0.6):
                desease = "תת תזונה"
                treatment="לתאם פגישה עם תזונאי"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (Origine=="Sout Africa") and ((hdl < 40.8) or (hdl < 34.8)):
                desease = "מחלות לב\היפרליפידמיה\סוכרת מבוגרים"
                treatment="לתאם פגישה עם תזונאי/כדור 5 מיליגרם של סימוביל ביום למשך שבוע/התאמת אינסולין למטופל"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()       
            if (hdl < 34) or (hdl < 29):
                desease = testResult+ "מחלות לב\היפרליפידמיה\סוכרת מבוגרים"
                treatment="לתאם פגישה עם תזונאי/כדור 5 מיליגרם של סימוביל ביום למשך שבוע/התאמת אינסולין למטופל"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (Origine=="North Africa") and (alk_phos > 120):
                desease = testResult+ "מחלות כבד\מחלות בדרכי המרה\פעילות יתר של בלוטת התריס\שימוש בתרופות שונות"
                treatment="הפנייה לאבחנה ספציפית לצורך קביעת טיפול/הפנייה לטיפול כירורגי/פרופילתיאוראסיל להקטנת פעילות בלוטת התריס/הפנייה לרופא המשפחה לצורך בדיקת התאמה בין התרופות"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if (Origine=="Middle East") and (alk_phos > 120):
                desease = "מחלות כבד\מחלות בדרכי המרה\פעילות יתר של בלוטת התריס\שימוש בתרופות שונות"
                treatment="הפנייה לאבחנה ספציפית לצורך קביעת טיפול/הפנייה לטיפול כירורגי/פרופילתיאוראסיל להקטנת פעילות בלוטת התריס/הפנייה לרופא המשפחה לצורך בדיקת התאמה בין התרופות"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit()
            if alk_phos > 90:
                desease = "מחלות כבד\מחלות בדרכי המרה\פעילות יתר של בלוטת התריס\שימוש בתרופות שונות"
                treatment="הפנייה לאבחנה ספציפית לצורך קביעת טיפול/הפנייה לטיפול כירורגי/פרופילתיאוראסיל להקטנת פעילות בלוטת התריס/הפנייה לרופא המשפחה לצורך בדיקת התאמה בין התרופות"
                if smoke== 'Yes': 
                    treatment += treatment + " stop smoking"
                cursor.execute("UPDATE `patientsymptomes` SET `testResult` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(desease,ID))
                cursor.execute("UPDATE `patientsymptomes` SET `Treatement` = '%s' WHERE `patientsymptomes`.`ID` = '%s';"%(treatment,ID))
                db_connection.commit() 

def symptomesformchecktest(item):
        if item.alk_phos > 90:
            desease = "מחלות כבד\מחלות בדרכי המרה\הריון\פעילות יתר של בלוטת התריס\שימוש בתרופות שונות"
            item.testresult=desease
           