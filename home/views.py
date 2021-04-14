from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
from rest_framework import viewsets
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from . serializers import approvalsSerializers
from . models import covid
# 
import numpy as np
import pandas as pd
#from . import output
import os

from sklearn.ensemble import RandomForestClassifier

class ApprovalsView(viewsets.ModelViewSet):
	queryset = covid.objects.all()
	serializer_class = approvalsSerializers

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

@api_view(["POST"])    
def corona(request):
    os.system('output.py')
    '''
  
    # Reading training data set. 

    df = pd.read_csv('data/covid19.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1]
    print(X.shape, Y.shape)

  
    # Reading data from user. 
    
    value = ''
    if request.method == 'POST':

        sex = str(request.POST['sex'])
        age_group = str(request.POST['age_group'])
        ethnicity = str(request.POST['ethnicity'])
        medcond_yn = str(request.POST['medcond_yn'])
      
  
        # Creating our training model. 
        
        rf = RandomForestClassifier(
            n_estimators=16, criterion='entropy', max_depth=5)
        rf.fit(np.nan_to_num(X), Y)

        user_data = np.array(
            (sex,
             age_group,
             ethnicity,
             medcond_yn,
             )
        ).reshape(1, 5)

        predictions = rf.predict(user_data)
        print(predictions)

        if int(predictions[0]) == "Laboratory-confirmed case":
            value = 'have'
        elif int(predictions[0]) == "Probable Case":
            value = "don\'t have"
    
    return JsonResponse('Your Status is {}')
    '''