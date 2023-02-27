from App.models import detail_dataBase
from django import forms


class Model_forms(forms.ModelForm):
    class Meta:
        model = detail_dataBase
        fields = ['No','Name', 'Address','Image', 'Links', 'Salary' ] # or
        # fields = '__all__' or
        # exclude = ['No']
