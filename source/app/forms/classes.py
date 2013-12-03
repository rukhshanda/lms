from django.forms import ModelForm

from app.models.classes import Class


class ClassForm(ModelForm):
    class Meta:
        model = Class
