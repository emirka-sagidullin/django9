from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

Users = {'User1': '12345678'}

def entry(request):
    entry = Entry()
    registration = Registration()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email in Users:
            if Users[email] == password:
                return HttpResponse('Поздравляю с успешным входом')
        if email not in Users or Users[email] != password:
            return HttpResponseRedirect('registration')
    return render(request, 'entry.html', {'entry': entry})

def registration(request):
    registration = Registration()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        Users[f'{email}'] = str(password)
        return HttpResponse(f'''{name}, поздравляю с регистрацией <br>Указанные вами данные: Имя - {name}, Email - {email}, Пароль - {password}''')
    return render(request, 'registration.html', {'form': registration})
    

