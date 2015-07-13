from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from core.forms import UploadFileForm
from core.models import Dataset
import csv

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Dataset(file_field=request.FILES['file'],name=request.POST['dataset_name'])
            instance.save()
            #Success
    else:
        form = UploadFileForm()
    datasets = Dataset.objects.all()
    for dataset in datasets:
        dataset.data = [row for row in csv.reader(dataset.file_field.read().splitlines())][0]
    return render(request, 'upload.html', {'form': form,'datasets':datasets})

def data(request,slug):
    dataset = get_object_or_404(Dataset,slug=slug)
    dataset.data = [row for row in csv.reader(dataset.file_field.read().splitlines())]
    return render(request,'data.html',{'dataset':dataset})