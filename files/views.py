from django.shortcuts import render
from django.http import HttpResponse
from .models import UploadFileForm

import os

# Create your views here.

def index(request):
    return render(request,"files/index.html")


def upload(request):
    if request.method == 'POST':
        print(("+++++++++++++"))
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = UploadFileForm()
            uploaded_file.title = form.cleaned_data['title']
            uploaded_file.file = form.cleaned_data['file']
            uploaded_file.save()
            handle_uploaded_file(uploaded_file.file)
            return HttpResponse('File uploaded successfully')
    else:
        print("---------------")
        form = UploadFileForm()
    return render(request, 'files/index.html', {'form': form})
