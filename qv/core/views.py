from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.forms import UploadFileForm
from core.models import Dataset

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Dataset(file_field=request.FILES['file'],name=request.POST['dataset_name'])
            instance.save()
            #Success
            form = UploadFileForm()
            datasets = Dataset.objects.all()
            render(request, 'upload.html', {'form': form,'datasets':datasets})
    else:
        form = UploadFileForm()
        datasets = Dataset.objects.all()
    return render(request, 'upload.html', {'form': form,'datasets':datasets})

def data(request):
    return render(request,'base.html',{})