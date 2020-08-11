from django import forms
from .models import Bbs_data


class Bbs_dataForm(forms.ModelForm):
    class Meta:
        model = Bbs_data
        fields = ('posttitle', 'post', 'writer', 'createdtime', 'nowtime')
