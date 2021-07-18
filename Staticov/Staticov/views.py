from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from Staticov.models import CivilianModel
from Staticov.models import IndexFormModel
from Staticov.models import RegisterFormModel
from Staticov.models import WorkersModel
from Staticov.models import emploiedutemp
from django.contrib import messages
from Staticov.models import Popup
import mysql.connector
# Create your views here.

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database="civilian"
)
cursor = db_connection.cursor()
print(db_connection)

# START PAGE WITH ANIMATION
def home(request):
    return render(request,'home.html')
# MAIN PAGE HOME WITH ALL INFORMATION
def index(request):
    return render(request,'index.html')
# RATING PAGE 
def rate(request):
    return render(request,'rating.html')
# ADMINDASHBORD AFTER CONNEXTION
def AdminDash(request):
    return render(request,'AdminDashBoard/index.html')
def WorkerDash(request):
# WORKERDASHBOARD AFTER CONNEXTION
    return render(request,'WorkerDashBoard/index.html')
def contact(request):
    return render(request,'AdminDashBoard/contact.html')
# MAINDASHBOARD WITH ALL STATISTICS
def MainDashBoard(request):
    return render('MainDashBoard/dashboardindex.html')
def offer_shifts(request):
    return render(request,'schedule.html')
#--------------------------------------------------------------------#   
def registration(request):
    #regular registration before 
    return render(request,'registrationform.html')
def add_patient(request):
    #worker page -> to insert new patient to the form_civilian_db
    return render(request,'WorkerDashBoard/addpatient.html')
def privacy(request):
    return render(request,'privacy_policy.html')
def changepassword(request):
    #page to change password to all users
    return render(request, 'changepassword.html')
def check_symptomes(request):
    return render(request,'Symptoms_Questionnaire.html')


#----------------------------USERS FUNCTIONS (REGISTRATIONS, ADD ,SUPP ) ! ---------------------------#

def registration_before_admin_approval(request): 
    if request.method=='POST':
        saverecord=RegisterFormModel()
        saverecord.taz=request.POST.get('taz')
        saverecord.name=request.POST.get('name')
        saverecord.password=request.POST.get('password')
        saverecord.Type=request.POST.get('Type')
        saverecord.civiliantype=request.POST.get('civiliantype')
        saverecord.save()
        if saverecord.Type == 'אזרח':
            messages.success(request,'הנתונים נשמרו בהצלחה!')
            return index(request)
        elif saverecord.Type == 'מנהל' or saverecord.Type == 'עובד מדינה':
            messages.success(request,'הנתונים נשמרו בהצלחה ! נא לחכות לאישור מנהל ')
            return index(request)
        else:
           return registration(request)
    else:
        return registration(request)

def after_approuval_worker_insert(request):
    if request.method=='POST':
        saverecord=WorkersModel()
        saverecord.taz=request.POST.get('taz')
        saverecord.name=request.POST.get('name')
        saverecord.password=request.POST.get('password')
        saverecord.Type=request.POST.get('Type')
        saverecord.save()
        cursor.execute("SELECT * FROM `registerform`")
        data = cursor.fetchall()    
        for item in data:
            ID,name,taz,password,Type,civiliantype = item
            if saverecord.taz==taz:
                cursor.execute("DELETE FROM `registerform` WHERE `registerform`.`ID` = '%s';"%(ID))
                db_connection.commit()
                messages.success(request,'הנתונים נשמרו בהצלחה!')
                return get_new_workers_table(request)          
    else:
        return get_new_workers_table(request)

def get_new_workers_table(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM registerform")
    data = cursor.fetchall()
    for item in data:
        ID,name,taz,password,type,civiliantype = item
        if type == 'מנהל' or type == 'עובד מדינה':
         result['data'].append({
            'id':ID,
            'name':name,
            'taz':taz,
            'password':password,
            'type':type,
        })
        print(result)
    return render(request,'AdminDashBoard/addworker.html', result)

def get_workers_table(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM workers")
    data = cursor.fetchall()
    for item in data:
        ID,name,taz,password,type = item
        result['data'].append({
            'id':ID,
            'name':name,
            'taz':taz,
            'password':password,
            'type':type,
        })
        print(result)
    return render(request,'deleteuser.html', result)

def get_civilian_table(request):
    result={
        'data': [],
        'counter': []
    }
    studentcount=0
    doctorcount=0
    scientificcount=0
    normal=0
    cursor.execute("SELECT * FROM registerform")
    data = cursor.fetchall()
    for item in data:
        ID,name,taz,password,type,civiliantype = item
        if civiliantype == 'סטודנט':
            studentcount += 1
        elif civiliantype == 'רופא':
            doctorcount += 1
        elif civiliantype == 'מדעי':
            scientificcount += 1
        elif civiliantype == 'רגיל':
            normal += 1
        if type == 'אזרח':
                result['data'].append({
                    'name':name,
                    'taz':taz,
                    'civiliantype':civiliantype,
                })
    print(result)
    result['counter'].append({
            'studentcount':studentcount,
            'doctorcount':doctorcount,
            'scientificcount':scientificcount,
            'normal':normal,
        })
        
    return render(request,'civilianlist.html', result)

def login(request):
    result = []
    cursor.execute("SELECT * FROM workers")
    data = cursor.fetchall()
    if request.method=='POST':
         useridtest=request.POST.get('taz')
         passwordtest=request.POST.get('password')
    for item in data:
        ID,name,taz,password,type= item
        if useridtest==taz and passwordtest == password and type == 'מנהל':
             return AdminDash(request)
        elif useridtest==taz and passwordtest == password and type == 'עובד מדינה':
             return WorkerDash(request)
    cursor.execute("SELECT * FROM registerform")
    data = cursor.fetchall()
    for item in data:
        ID,name,taz,password,type,civiliantype = item
        if useridtest==taz and passwordtest == password and type == 'אזרח':
             return index(request) 
    else :
        messages.error(request,' הפרטים שהוזנו לא נמצאים במערכת נא לחכות לאישור אם הפרטים נכונים')   
        return registration(request) 

def CHANGE_PASSWORD(request):
    if request.method=='POST':
        useridtest=request.POST.get('taz')
        passwordcurrentpassword=request.POST.get('current_password')
        passwordtest=request.POST.get('password')
        cursor.execute("SELECT * FROM workers")
        data = cursor.fetchall()    
        flag=0
        for item in data:
            ID,name,taz,password,type = item
            if  taz==useridtest and password == passwordcurrentpassword and (type == 'מנהל' or type == 'עובד מדינה'):
                cursor.execute("UPDATE `workers` SET `password` = '%s' WHERE `workers`.`ID` = '%s';"%(passwordtest,ID))
                db_connection.commit()
                flag = 1
        if flag == 1 :
            messages.success(request,'סיסמא הוחלפה בהצלחה')
            return registration(request)
        if flag == 0 :   
            cursor.execute("SELECT * FROM registerform")
            data = cursor.fetchall()    
            for item in data:
                ID,name,taz,password,type,civiliantype = item
                if taz==useridtest and password == passwordcurrentpassword and type == 'אזרח':
                    cursor.execute("UPDATE `registerform` SET `password` = '%s' WHERE `registerform`.`ID` = '%s';"%(passwordtest,ID))
                    db_connection.commit()
                    messages.success(request,'סיסמא הוחלפה בהצלחה')
                    return registration(request)  

        messages.error(request,'! הפרטים שהוזנו לא נמצאים במערכת')   
        return changepassword(request)


def Deleteworker(request):
    if request.method=='POST':
        useridworker=request.POST.get('taz')
        workername=request.POST.get('name')
        result = []
        cursor.execute("SELECT * FROM workers")
        data = cursor.fetchall()    
        for item in data:
            ID,name,taz,password,type = item
            if taz==useridworker and name == workername :
                cursor.execute("DELETE FROM `workers` WHERE `workers`.`ID` = '%s';"%(ID))
                db_connection.commit()
                messages.success(request,'עובד הוסר מהמערכת ')
                return get_workers_table(request)
    else: messages.success(request,'עובד לא נמצא במערכת ')
    return index(request)
#-----------------------------------PATIENT FUNCTIONS ! -------------------#

#==========function for admin add patient to worker----------------------#
def get_new_positiv_table(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM indexform")
    data = cursor.fetchall()
    for item in data:
        ID,name,taz,telephone,symptomes,age,workerid = item
        result['data'].append({
            'id':ID,
            'name':name,
            'taz':taz,
            'telephone':telephone,
            'symptomes':symptomes,
            'age':age,
            'workerid':workerid,
            
        })
        print(result)
    return render(request,'AdminDashBoard/patienttoworker.html', result)

def get_Main_dashboard(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM popup")
    data = cursor.fetchall()
    for item in data:
        MID,popupmsg= item
        result['data'].append({
            'MID':MID,
            'popupmsg':	popupmsg,
        })
        print(result)
    return render(request,'MainDashBoard/dashboardindex.html', result)

popupmessagetext = Popup.objects.all()
#==========function for worker list of patient worker assigned----------------------#

def get_new_patient_table(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM indexform")
    data = cursor.fetchall()
    for item in data:
        ID,name,taz,telephone,symptomes,age,workerid = item
        result['data'].append({
            'id':ID,
            'name':name,
            'taz':taz,
            'telephone':telephone,
            'symptomes':symptomes,
            'age':age,
            'workerid':workerid,
            
        })
        print(result)
    return render(request,'WorkerDashBoard/patientlist.html', result)

#==========INDEX FORM FUNCTION----------------------#
def indexcontact(request):
 if request.method=='POST':
     saverecord=IndexFormModel()
     saverecord.name=request.POST.get('name')
     saverecord.taz=request.POST.get('taz')
     saverecord.telephone=request.POST.get('telephone')
     saverecord.symptomes=request.POST.get('symptomes')
     saverecord.age=request.POST.get('age')
     saverecord.workerid=0
     saverecord.save()
     messages.success(request,'Record Saved Successfully...!')
     return index(request)
 else:
     return index(request)

#==========ASSIGN PATIENT TO WORKER FUNCTION==========#

def assign_patient(request):
    if request.method=='POST':
        currenttelephone=request.POST.get('telephone')
        currenttaz=request.POST.get('taz')
        currentworkerid=request.POST.get('workerid')
    result = []
    cursor.execute("SELECT * FROM indexform")
    data = cursor.fetchall()    
    for item in data:
        ID,name,taz,telephone,symptomes,age,workerid = item
        if taz==currenttaz and telephone == currenttelephone :
            cursor.execute("UPDATE `indexform` SET `workerid` = '%s' WHERE `indexform`.`ID` = '%s';"%(currentworkerid,ID))
            db_connection.commit()
            return AdminDash(request)
    else:
        messages.error(request,'הפרטים שהוזנו לא נמצאים במערכת')   
        return changepassword(request)
    


def get_data_test(request):
    result = []
    cursor.execute("SELECT * FROM `worker-register`")
    data = cursor.fetchall()
    if request.method=='POST':
         useridtest=request.POST.get('userid')
         passwordtest=request.POST.get('password')
    for item in data:
        print(item)
        print(useridtest)
        print(passwordtest)
        ID,userid,name,password = item
        result.append({
            'userid': userid,
            'name': name,
            'password': password,
            'useridtest' : useridtest,
            'passwordtest' : passwordtest,     

        })
        if useridtest==userid and passwordtest == password:
                print('lalalalal')
    return HttpResponse(JSON.dumps(result), content_type="application/json")

def datapatient(request):
    if request.method == 'GET':
        cursor.execute("SELECT * FROM formcivilian")
        data = cursor.fetchall()
        data_list = list(data)
        return JsonResponse(data_list, safe=False)

#==========ASSIGN PATIENT TO FORMCIVILIAN DB and DELETE ID FROM indexform DB ==========#

def addpatient(request):
    if request.method=='POST':
        saverecord=CivilianModel()
        saverecord.taz=request.POST.get('taz')
        saverecord.age=request.POST.get('age')
        saverecord.place=request.POST.get('place')
        saverecord.date=request.POST.get('date')
        saverecord.religion=request.POST.get('religion')
        saverecord.save()
        cursor.execute("SELECT * FROM indexform")
        data = cursor.fetchall()    
        for item in data:
            ID,name,userid,telephone,symptomes,age,workerid = item
            if saverecord.taz==userid :
                cursor.execute("DELETE FROM `indexform` WHERE `indexform`.`ID` = '%s';"%(ID))
                db_connection.commit()
                messages.success(request,'הפרטים נרשמו בהצלחה ! ')
                return WorkerDash(request)
        else:
            cursor.execute("SELECT * FROM formcivilian")
            data = cursor.fetchall()    
            for item in data:
                ID,taz,age,place,date,religion = item
                if saverecord.taz==taz :
                    cursor.execute("DELETE FROM `formcivilian` WHERE `formcivilian`.`ID` = '%s';"%(ID))
                    db_connection.commit()
                    messages.success(request,'הפרטים לא נמצאים במערכת !')
                    return add_patient(request)
    messages.success(request,'הפרטים לא נמצאים במערכת !')
    return WorkerDash(request)


def symptomesformcheck(request):
    if request.method=='POST':
         headtest=request.POST.get('head')
         hottest=request.POST.get('hot')
         smelltest=request.POST.get('smell')
         hurtstest=request.POST.get('hurts')
    if  headtest=='כן' and hottest=='כן' and smelltest =='כן' and hurtstest == 'כן':
         messages.success(request,'ממולץ לבצע בדיקה לנגיף הקורונה')
         return index(request)
    elif headtest=='כן' and hottest=='כן' and smelltest =='לא' and hurtstest == 'כן':
         messages.success(request,'מומלץ לבצע בדיקה לנגיף הקורונה')
         return index(request)
    elif headtest=='כן' and hottest=='כן' and smelltest =='כן' and hurtstest == 'לא':
         messages.success(request,'מומלץ לבצע בדיקה לנגיף הקורונה')
         return index(request)
    elif headtest=='לא' and hottest=='כן' and smelltest =='כן' and hurtstest == 'כן':
         messages.success(request,'מומלץ לבצע בדיקה לנגיף הקורונה')
         return index(request)
    elif headtest=='לא' and hottest=='לא' and smelltest =='לא' and hurtstest == 'לא':
         messages.success(request,'במידה ואין שום תסמינים אין צורך לבצע בדיקה לנגיף הקורונה')
         return index(request)
    elif headtest=='לא' and hottest=='כן' and smelltest =='כן' and hurtstest == 'כן':
         messages.success(request,'מומלץ לבצע בדיקה לנגיף הקורונה')
         return index(request)
    elif headtest=='כן' and hottest=='כן' and smelltest =='לא' and hurtstest == 'לא':
         messages.success(request,'מומלץ לבצע בדיקה לנגיף הקורונה')
         return index(request)
    elif headtest=='לא' and hottest=='כן' and smelltest =='כן' and hurtstest == 'לא':
         messages.success(request,'מומלץ לבצע בדיקה לנגיף הקורונה')
         return index(request)
    elif headtest=='כן' and hottest=='לא' and smelltest =='לא' and hurtstest == 'כן':
         messages.success(request,'מומלץ לבצע בדיקה לנגיף הקורונה')
         return index(request)
    else:
         messages.success(request,'מידה ואין שום תסמינים אין צורך לבצע בדיקה לנגיף הקורונה')
         return index(request)


#=================POPUP================#


def CHANGE_MESSAGE_POPUP(request):
    if request.method=='POST':
        msgpp=request.POST.get('popup-msg')
        result = []
        cursor.execute("SELECT * FROM `popup`")
        data = cursor.fetchall()    
        for item in data:
            MID,popupmsg = item
            cursor.execute("UPDATE `popup` SET `popupmsg` = '%s' WHERE `popup`.`MID` = '%s';"%(msgpp,1))
            db_connection.commit()
            messages.success(request,'הודעתך נקלטה בהצלחה')
        return AdminDash(request)
    else:  
        return AdminDash(request)

#==================SCHEDULE=========================#

def shift_offers(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM emploiedutemp")
    data = cursor.fetchall()
    for item in data:
        ID,start,end,workerid,confirmation = item
        result['data'].append({
            'id':ID,
            'start':start,
            'end':end,
            'workerid':workerid,
            'confirmation':confirmation
        })
        print(result)
    return render(request,'schedule2.html', result)

def workerschedule(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM emploiedutemp")
    data = cursor.fetchall()
    for item in data:
        ID,start,end,workerid,confirmation = item
        result['data'].append({
            'id':ID,
            'start':start,
            'end':end,
            'workerid':workerid,
            'confirmation':confirmation
        })
        print(result)
    return render(request,'workerschedule.html', result)

def shift_offer(request):
    if request.method=='POST':
        saverecord=emploiedutemp()
        saverecord.startdate=request.POST.get('start')
        saverecord.enddate=request.POST.get('end')
        saverecord.workerid=request.POST.get('workerid')
        saverecord.confirmation='ממתין לאישור'
        saverecord.save()
        messages.success(request,'הפרטים נרשמו בהצלחה  ! ')
        return WorkerDash(request)
    else:
        return index(request)


def confirm_shift(request):
    if request.method=='POST':
        starttest=request.POST.get('start')
        endtest=request.POST.get('end')
        currentworkerid=request.POST.get('workerid')
        confirmed=request.POST.get('confirmation')
    result = []
    cursor.execute("SELECT * FROM `emploiedutemp`")
    data = cursor.fetchall()    
    for item in data:
            ID,startdate,enddate,workerid,confirmation = item
            if startdate==starttest and enddate == endtest and workerid == currentworkerid and confirmed=='אשר':
                cursor.execute("UPDATE `emploiedutemp` SET `confirmation` = '%s' WHERE `emploiedutemp`.`ID` = '%s';"%(confirmed,ID))
                db_connection.commit()
                return AdminDash(request)
            elif startdate==starttest and enddate == endtest and workerid == currentworkerid and confirmed=='דחה':
                    cursor.execute("DELETE FROM `emploiedutemp` WHERE `emploiedutemp`.`ID` = '%s';"%(ID))
                    db_connection.commit()
                    return AdminDash(request)
    else:
            messages.error(request,'הפרטים שהוזנו לא נמצאים במערכת')   
            return AdminDash(request)