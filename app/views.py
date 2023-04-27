from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def student(request):
    sof=Studentform()
    d={'sof':sof}
    if request.method=='POST':
        sfd=Studentform(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))
        else:
            return HttpResponse('DATA IS INVALID')

    return render(request,'student.html',d)