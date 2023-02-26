from django import forms


class detail_dataBase_Froms (forms.Form):
    No = forms.IntegerField(required=False)
    Name = forms.CharField(required=False)
    Address = forms.Textarea()
    Image = forms.ImageField(required=False)
    Links = forms.URLField(required=False )
    Salary = forms.FloatField(required=False)