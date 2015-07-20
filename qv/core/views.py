from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from core.forms import UploadFileForm
from core.models import Dataset
from core.utils import num
import csv
from operator import itemgetter

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
    dataArr = [row for row in csv.reader(dataset.file_field.read().splitlines())]
    headers = dataArr[0]
    dataDict = []
    maxYear = 0
    for row in dataArr[1:]:
        rowDict = {}
        for i in range(len(headers)):
            header = headers[i]
            cell = num(row[i])
            if header=="year" and cell>maxYear:
                maxYear=cell
            rowDict[header] = cell
        dataDict.append(rowDict)
    dataDict.sort(key=itemgetter("value"),reverse=True)
    dataset.data = dataDict
    data = {
        'dataset':dataset
    }
    return render(request,'data.html',data)