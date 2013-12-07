from django.forms import ModelForm, widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, Button, HTML
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

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
