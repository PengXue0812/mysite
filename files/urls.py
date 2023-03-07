#myApp urls.py

from argparse import Namespace
from operator import index
from django.urls import path,re_path,include
from . import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("",views.index,name="index"),
    path("",views.upload,name="upload")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)