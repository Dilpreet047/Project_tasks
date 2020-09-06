from django.http import HttpResponse
from django.shortcuts import render
import joblib

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
    print(l)

    return render(request, "result.html")


