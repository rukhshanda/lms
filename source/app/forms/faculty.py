from django.forms import ModelForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, HTML
from crispy_forms.bootstrap import FormActions

from app.models.faculty import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('id', 'email', 'first_name', 'last_name', 'gender', 'speciality')

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

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
            Field('speciality', css_class='input-sm'),
            FormActions(
                Submit('save_changes', 'Save changes', css_class='btn-primary btn-sm'),
                HTML('<input type="button" name="Cancel" value="Cancel" class="btn btn-default btn-sm" onclick="javascript:window.location='+ "'" +'/dashboard/teacher/'+ "'" +';" />')
            ),
        )

    def save(self, commit=True):
        instance = super(TeacherForm, self).save(commit=False)

        instance.username = self.cleaned_data['email']
        instance.is_staff = False
        instance.is_active = False  # Set to false because teachers can't login

        content_type = ContentType.objects.get_for_model(Teacher)
        permission = Permission.objects.get(content_type=content_type, codename='has_faculty_perms')

        if commit:
            instance.set_password('1234567890!')
            instance.save()
            instance.user_permissions.add(permission)

        return instance
