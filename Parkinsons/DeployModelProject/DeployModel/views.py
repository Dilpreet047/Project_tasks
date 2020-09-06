from django.http import HttpResponse
from django.shortcuts import render
import joblib
import pandas as pd 
import numpy as np

def function1(request):
    return render(request, "first.html")

def function2(request):

    l = []
    l.append(request.GET['MDVP:Fo(Hz)'])
    l.append(request.GET['MDVP:Fhi(Hz)'])
    l.append(request.GET['MDVP:Flo(Hz)'])
    l.append(request.GET['MDVP:Jitter(%)'])
    l.append(request.GET['MDVP:Jitter(Abs)'])
    l.append(request.GET['MDVP:RAP'])
    l.append(request.GET['MDVP:PPQ'])
    l.append(request.GET['Jitter:DDP'])
    l.append(request.GET['MDVP:Shimmer'])
    l.append(request.GET['MDVP:Shimmer(dB)'])
    l.append(request.GET['Shimmer:APQ3'])
    l.append(request.GET['Shimmer:APQ5'])
    l.append(request.GET['MDVP:APQ'])
    l.append(request.GET['Shimmer:DDA'])
    l.append(request.GET['NHR'])
    l.append(request.GET['HNR'])
    l.append(request.GET['RPDE'])
    l.append(request.GET['DFA'])
    l.append(request.GET['spread1'])
    l.append(request.GET['spread2'])
    l.append(request.GET['D2'])
    l.append(request.GET['PPE'])
    
    l2 = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
       'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
       'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
       'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA',
       'spread1', 'spread2', 'D2', 'PPE']
    #d = pd.DataFrame.from_dict(dict(zip(l2,l)))
    print(len(l2))
    print(len(l))
    l1 = np.reshape(l, (22,1))
    print(l1)
    x=dict(zip(l2,l1))
    print(x)
    y = pd.DataFrame(x)
    y = y.astype(float)
    print(y)
    model = joblib.load('model.sav')
    status = model.predict(y)

    return render(request, "result.html", {'status':status})


