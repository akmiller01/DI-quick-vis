from django import forms
from django.forms import ModelForm
from core.validators import validate_file_extension
from core.models import Dataset

class UploadFileForm(forms.Form):
    dataset_name = forms.CharField(max_length=255,required=False,help_text="Not required.")
    file = forms.FileField(validators=[validate_file_extension])
    
class ConfigDatasetForm(ModelForm):
    xVar = forms.CharField(widget=forms.Select(),required=False)
    yVar = forms.CharField(widget=forms.Select(),required=False)
    timeVar = forms.CharField(widget=forms.Select(),required=False)
    class Meta:
        model = Dataset
        exclude = ["slug","file_field","json"]