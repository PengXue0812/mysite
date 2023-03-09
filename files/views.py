from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
import os

# Create your views here.


def index(request):
    return render(request, "files/index.html")


@csrf_exempt
def upload(request):
    # post request
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        # data = zip(request.POST, request.FILES['file'])
        # print(list(data))
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("files:index")
    # get request
    else:
        form = UploadFileForm()
    return render(request, "files/success.html", {"form": form})
