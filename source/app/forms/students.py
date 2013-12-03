from django.forms import ModelForm

from app.models.students import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
