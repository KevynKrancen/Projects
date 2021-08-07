from random import random
import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import mysql.connector
from django.http import JsonResponse
import random
from dataProj.models import *
import pandas as pd
from dataProj.Functions import *
from dataProj.NaiveBayes import *
from dataProj.sklearnNaiveBayes import *
from dataProj.Id3 import *
from dataProj.Id3SKlearn import *
from dataProj.KNNClassifier import *
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# START PAGE WITH ANIMATION

def home(request):
        return render(request,'index.html')
def NaiveBayestests(request):
        return render(request,'naiveBa.html')
def MyNaiveBayesResult(request):
        return render(request,'MynaivBaresult.html') 

def id3tests(request):
        return render(request,'id3.html')
def Addfile(request):
        return render(request,'Addfile.html')
def NaiveNayesown(request):
      testFile="/Users/kevyn/Dataprojet/media/testdata.csv"  
      structFile="/Users/kevyn/OneDrive/Documents/datasets/Structure.txt" ## change 
      trainFile="/Users/kevyn/OneDrive/Documents/datasets/train.csv"  ## change 
      test = pd.read_csv(testFile)
      train = pd.read_csv(trainFile)
      Naiveresult = naiveBayes(test,train,structFile)
      print(Naiveresult)
      thisdict = {
              "result":Naiveresult
      }
      return render(request,'MynaivBaresult.html',{"thisdict":Naiveresult}) 

def NaiveBayesSklearn(request):
      testFile="/Users/kevyn/Dataprojet/media/testdata.csv"  
      structFile="/Users/kevyn/OneDrive/Documents/datasets/Structure.txt" ## change 
      trainFile="/Users/kevyn/OneDrive/Documents/datasets/train.csv"  ## change 
      test = pd.read_csv(testFile)
      train = pd.read_csv(trainFile)
      Naiveresult = sklearnNaiveBayes(test,train,structFile)
      print(Naiveresult)
      thisdict = {
              "result":Naiveresult
      }
      return render(request,'MynaivBaresult.html',thisdict) 

def MyID3(request):
      testFile="/Users/kevyn/Dataprojet/media/testdata.csv"  
      structFile="/Users/kevyn/OneDrive/Documents/datasets/Structure.txt" ## change 
      trainFile="/Users/kevyn/OneDrive/Documents/datasets/train.csv"  ## change 
      test = pd.read_csv(testFile)
      train = pd.read_csv(trainFile)
      Naiveresult = ID3_algorithm(train,test,structFile)
      print(Naiveresult)
      thisdict = {
              "result":Naiveresult
      }
      return render(request,'MynaivBaresult.html',thisdict) 

def SklearnID3(request):
      testFile="/Users/kevyn/Dataprojet/media/testdata.csv"  
      structFile="/Users/kevyn/OneDrive/Documents/datasets/Structure.txt" ## change 
      trainFile="/Users/kevyn/OneDrive/Documents/datasets/train.csv"  ## change 
      test = pd.read_csv(testFile)
      train = pd.read_csv(trainFile)
      Res = ID3_SKlearn(train,test,structFile)
      print(Res)
      thisdict = {
              "result":Res
      }
      return render(request,'MynaivBaresult.html',thisdict) 

def KNNCLASS(request): 
      testFile="/Users/kevyn/Dataprojet/media/testdata.csv"  
      structFile="/Users/kevyn/OneDrive/Documents/datasets/Structure.txt" ## change 
      trainFile="/Users/kevyn/OneDrive/Documents/datasets/train.csv"  ## change 
      test = pd.read_csv(testFile)
      train = pd.read_csv(trainFile)
      Res = KNNClassifier(train,structFile)
      print(Res)
      thisdict = {
              "result":Res
      }
      return render(request,'MynaivBaresult.html',thisdict)      

# def Datareceive(request): 
#     if request.method=='POST':

#                 form.file_name=request.POST.get('filecsv')
#                 instance = form.file_name
#                 form.save()
#                 filesend=pd.read_csv(form.file_name)
#                 print(filesend)
#                 train=pd.read_csv(request.POST.get('file'))
#                 structFile="/Users/kevyn/OneDrive/Documents/datasets/Structure.txt" ## change 
#                 testFile="/Users/kevyn/OneDrive/Documents/datasets/test.csv"  ## change
#                 print(train)
#                 test = pd.read_csv(testFile)
#                 Naiveresult = naiveBayes(test,train,structFile)
#                 print(Naiveresult)
#                 sklearnNaiveBayesResult = sklearnNaiveBayes(test,train,structFile)
#                 print(sklearnNaiveBayesResult)
#                 ID3_algorithm(train,test,structFile)
#                 ID3_SKlearn(train,test,structFile)
#                 KNNClassifier(train,structFile)
#                 return render(request,'index.html') 

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filesend=pd.read_csv(myfile)
        print(filesend)
        fs.save("testdata.csv", myfile)
        return render(request,'index.html')