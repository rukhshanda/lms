from django.forms import ModelForm

from app.models.groups import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
