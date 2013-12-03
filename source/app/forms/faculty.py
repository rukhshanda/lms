from django.forms import ModelForm

from app.models.faculty import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
