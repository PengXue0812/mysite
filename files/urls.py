#myApp urls.py

from argparse import Namespace
from operator import index
from django.urls import path,re_path,include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("",views.index,name="index"),
    # path("download/file1",views.download1,name="download1"),
    # path("download/file2",views.download2,name="download2"),
    # path("download/file3",views.download3,name="download3"),
    path("upload",views.upload,name="uploaded")

]

#配置全局404页面
# handler404 = "files.views.page_not_found"

# 配置全局500页面
# handler500 = "files.views.page_error"