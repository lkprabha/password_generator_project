from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):

    charactors=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charactors.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Special Charactors'):
        charactors.extend(list('!@#%$&'))

    if request.GET.get('Numbers'):
        charactors.extend(list('0123456789'))

    length= int(request.GET.get('length',12))
    thepassword=''

    for x in range(length):
        thepassword += random.choice(charactors)

    return render(request,'generator/password.html',{'password': thepassword})
