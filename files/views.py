from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
import os
import sys
import RobustSpot_master.main as main
# Create your views here.


def index(request):
    return render(request, "files/index.html")


@csrf_exempt
def upload(request):
    # post request
    if request.method == "POST":
        # 将timestamp和file_name写入到RobustSpot_master/config/anomaly.yaml中
        # print(request.POST)
        # print(request.POST.getlist('timestamp'))
        timestamp = request.POST.getlist('timestamp')
        print(timestamp)
        print('----------')
        print(request.FILES)
        files = request.FILES.getlist('file')
        print(files)
        file_name = []
        for file in files:
            file_name.append(file.name)
            # 将文件写入到RobustSpot-master/data/目录下，如果不存在则创建
            if not os.path.exists('RobustSpot_master/data/'):
                os.makedirs('RobustSpot_master/data/')
            # 如果文件不存在则创建，存在则覆盖写入
            with open('RobustSpot_master/data/' + file.name, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        print(file_name)
        # 将timestamp和file_name写入到RobustSpot-master/config/anomaly.yaml中
        # 如果文件不存在则创建，存在则覆盖写入
        with open('RobustSpot_master/config/anomaly.yaml', 'w') as f:
            for i in range(len(timestamp)):
                f.write('- data: ' + file_name[i] + '\n')
                f.write('  timestamp: ' + timestamp[i] + '\n')
        # 调用RobustSpot-master/main.py中的main函数
        main.main()
    return render(request, "files/success.html")
