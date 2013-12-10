from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, HTML
from crispy_forms.bootstrap import FormActions

from app.models.groups import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('id', 'name', 'start_date', 'end_date', 'cclass', 'representative')

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

        self.fields['name'].required = True
        self.fields['start_date'].required = True
        self.fields['end_date'].required = True
        self.fields['cclass'].required = True
        self.fields['representative'].required = False

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2 small'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Field('name', css_class='input-sm'),
            Field('start_date', css_class='input-sm', placeholder='yyyy-mm-dd'),
            Field('end_date', css_class='input-sm', placeholder='yyyy-mm-dd'),
            Field('cclass', css_class='input-sm'),
            Field('representative', css_class='input-sm'),
            FormActions(
                Submit('save_changes', 'Save changes', css_class='btn-primary btn-sm'),
                HTML('<input type="button" name="Cancel" value="Cancel" class="btn btn-default btn-sm" onclick="javascript:window.location='+ "'" +'/dashboard/class/'+ "'" +';" />')
            ),
        )
