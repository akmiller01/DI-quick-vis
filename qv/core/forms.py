from django import forms
from core.validators import validate_file_extension

class UploadFileForm(forms.Form):
    dataset_name = forms.CharField(max_length=255,required=False,help_text="Not required.")
    file = forms.FileField(validators=[validate_file_extension])