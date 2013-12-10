from django.forms import ModelForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, HTML
from crispy_forms.bootstrap import FormActions

from app.models.students import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'gender', 'roll_no', 'cclass', 'group')

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['password'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['roll_no'].required = True
        self.fields['cclass'].required = True

        instance = kwargs.pop('instance', None)
        if instance:
            self.fields['password'].required = False

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2 small'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Field('email', css_class='input-sm'),
            Field('password', css_class='input-sm', placeholder='Enter a new password'),
            Field('first_name', css_class='input-sm'),
            Field('last_name', css_class='input-sm'),
            Field('gender', css_class='input-sm'),
            Field('roll_no', css_class='input-sm'),
            Field('cclass', css_class='input-sm'),
            Field('group', css_class='input-sm'),
            FormActions(
                Submit('save_changes', 'Save changes', css_class='btn-primary btn-sm'),
                HTML('<input type="button" name="Cancel" value="Cancel" class="btn btn-default btn-sm" onclick="javascript:window.location='+ "'" +'/dashboard/teacher/'+ "'" +';" />')
            ),
        )

    def save(self, commit=True):
        instance = super(StudentForm, self).save(commit=False)

        instance.username = self.cleaned_data['email']
        instance.is_staff = False
        instance.is_active = True

        content_type = ContentType.objects.get_for_model(Student)
        permission = Permission.objects.get(content_type=content_type, codename='has_student_perms')

        if commit:
            if self.fields['password']:
                instance.set_password(self.cleaned_data['password'])
            instance.save()
            instance.user_permissions.add(permission)

        return instance
