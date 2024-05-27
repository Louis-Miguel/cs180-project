import sys
from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home(request):
    return render(request, "home.html")

def result(request):
    model = joblib.load("model.sav")

    vect = joblib.load("vect.sav")
    message = request.GET.get("message", "")
    transformed_message  = vect.transform([request.GET["message"]])
    ans = model.predict(transformed_message)
    
    return render(request, "result.html", {"message": message,"ans": "Scam" if ans == [1] else "Regular Text"})