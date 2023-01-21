import django.forms as forms
from .models import Student, Professor


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = "__all__"
