from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    jmbg = models.CharField(max_length=13, primary_key=True)
    image = models.ImageField(upload_to='images')

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Student(User):
    short_major = models.CharField(max_length=2)
    index_number = models.CharField(max_length=4)
    year_of_enrollment = models.CharField(max_length=4)

    def __str__(self) -> str:
        return f'{self.short_major} {self.index_number}/{self.year_of_enrollment} {super().__str__()} '


class Professor(User):
    subject_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{super().__str__()} - {self.subject_name}'
