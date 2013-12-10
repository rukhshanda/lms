from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, HTML
from crispy_forms.bootstrap import FormActions

from app.models.classes import Class


class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ('id', 'name', 'year', 'coordinator')

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)

        self.fields['name'].required = True
        self.fields['year'].required = True
        self.fields['coordinator'].required = True

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2 small'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Field('name', css_class='input-sm'),
            Field('year', css_class='input-sm'),
            Field('coordinator', css_class='input-sm'),
            FormActions(
                Submit('save_changes', 'Save changes', css_class='btn-primary btn-sm'),
                HTML('<input type="button" name="Cancel" value="Cancel" class="btn btn-default btn-sm" onclick="javascript:window.location='+ "'" +'/dashboard/class/'+ "'" +';" />')
            ),
        )
