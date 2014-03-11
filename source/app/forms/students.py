from django import forms
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, HTML
from crispy_forms.bootstrap import FormActions

from app.models.students import Student
from app.models.classes import Class
from app.models.groups import Group


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name', 'gender', 'roll_no', 'cclass', 'group')

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['roll_no'].required = True
        self.fields['cclass'].required = True
        self.fields['cclass'].label = 'Class'

        instance = kwargs.pop('instance', None)

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2 small'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Field('email', css_class='input-sm'),
            Field('first_name', css_class='input-sm'),
            Field('last_name', css_class='input-sm'),
            Field('gender', css_class='input-sm'),
            Field('roll_no', css_class='input-sm'),
            Field('cclass', css_class='input-sm'),
            Field('group', css_class='input-sm'),
            FormActions(
                Submit('save_changes', 'Save changes', css_class='btn-primary btn-sm'),
                HTML('<input type="button" name="Cancel" value="Cancel" class="btn btn-default btn-sm" onclick="javascript:window.location='+ "'" +'/dashboard/student/'+ "'" +';" />')
            ),
        )

    def save(self, commit=True):
        instance = super(StudentForm, self).save(commit=False)

        instance.username = self.cleaned_data['email']
        instance.is_staff = False
        instance.is_active = False  # Set to false because students can't login

        content_type = ContentType.objects.get_for_model(Student)
        permission = Permission.objects.get(content_type=content_type, codename='has_student_perms')

        if commit:
            instance.set_password('1234567890!')
            instance.save()
            instance.user_permissions.add(permission)

        return instance


class StudentImportForm(forms.Form):
    cclass = forms.ModelChoiceField(label='Class', empty_label='Select a class', queryset=Class.objects.all(), required=True)
    group = forms.ModelChoiceField(label='Group', empty_label='Select a group', queryset=Group.objects.all(), required=True)
    file = forms.FileField(label='CSV data file', help_text='<small><em>Please select a valid CSV file. See <a href="/static/csv/import_student.csv">this template</a> for reference.</em></small>')

    def __init__(self, *args, **kwargs):
        super(StudentImportForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 small'
        self.helper.field_class = 'col-md-7'
        self.helper.layout = Layout(
            Field('cclass', css_class='input-sm'),
            Field('group', css_class='input-sm'),
            Field('file', css_class='input-sm'),
            FormActions(
                Submit('save_changes', 'Save changes', css_class='btn-primary btn-sm'),
                HTML('<input type="button" name="Cancel" value="Cancel" class="btn btn-default btn-sm" onclick="javascript:window.location='+ "'" +'/dashboard/student/'+ "'" +';" />')
            ),
        )
