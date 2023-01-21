from typing import List
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .forms import StudentForm, ProfessorForm
from .models import Student, Professor
from django.forms import ModelForm
from os import environ
faculty = environ.get("FACULTY_NAME", default='PMF')


def index(request: HttpRequest) -> HttpResponse:
    context = {'ssluzba': faculty}
    return render(request, 'index.html', context)


def students(request: HttpRequest) -> HttpResponse:
    students = Student.objects.all()
    return _add_user(request=request,
                     model_form=StudentForm,
                     user_type='Studenti',
                     users=students)


def professors(request: HttpRequest) -> HttpResponse:
    users = Professor.objects.all()
    return _add_user(request=request,
                     model_form=ProfessorForm,
                     user_type='Profesori',
                     users=users)


def _add_user(request: HttpRequest, model_form: ModelForm, user_type: str, users: List) -> HttpResponse:
    context = {
        'ssluzba': faculty,
        'form': model_form,
        'user_type': user_type,
        'users': users
    }
    if request.method == 'POST':
        form = model_form(request.POST)
        if form.is_valid():
            # DODATI SLANJE ZAHTIJEVA NA UNS APLIKACIJU
            form.save()
    return render(request, 'users_page.html', context)
