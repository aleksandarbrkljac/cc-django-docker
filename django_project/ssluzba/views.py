from typing import List
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .forms import StudentForm, ProfessorForm
from .models import Student, Professor
from django.forms import ModelForm
from os import getenv
import requests
faculty_name = getenv("FACULTY_NAME", default='PMF')
uns_sluzba_api = getenv("UNS_API", default="http://localhost:3000/users/")


def index(request: HttpRequest) -> HttpResponse:
    context = {'ssluzba': faculty_name}
    return render(request, 'index.html', context)


def students(request: HttpRequest) -> HttpResponse:
    students = Student.objects.all()
    return _add_user(request=request,
                     model_form=StudentForm,
                     user_type='Studenti',
                     users=students,
                     uns_api_endpoint='students')


def professors(request: HttpRequest) -> HttpResponse:
    users = Professor.objects.all()
    return _add_user(request=request,
                     model_form=ProfessorForm,
                     user_type='Profesori',
                     users=users,
                     uns_api_endpoint='professors')


def _add_user(request: HttpRequest,
              model_form: ModelForm,
              users: List,
              user_type: str,
              uns_api_endpoint: str) -> HttpResponse:
    context = {
        'ssluzba': faculty_name,
        'form': model_form,
        'user_type': user_type,
        'users': users
    }
    uns_sluzba_api = getenv("UNS_API", default="http://localhost:3000/users/")
    print(f'UNS SLUZBA API {uns_sluzba_api}')
    if request.method == 'POST':
        form = model_form(request.POST)
        if form.is_valid():
            response = requests.post(f'{uns_sluzba_api}{uns_api_endpoint}', json={
                "jmbg": request.POST['jmbg'],
                "name": request.POST['first_name'] + ' ' + request.POST['last_name']
            }, verify=False)
            response_message = response.content.decode()
            context['message'] = response_message
            if response.status_code == 201:
                form.save()
        else:
            context['message'] = "KORISNIK VEC POSTOJI!"

    return render(request, 'users_page.html', context)
