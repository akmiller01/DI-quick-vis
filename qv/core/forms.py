from django import forms

class UploadFileForm(forms.Form):
    dataset_name = forms.CharField(max_length=255,required=False,help_text="Not required.")
    file = forms.FileField()