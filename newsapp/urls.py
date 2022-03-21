from django.contrib import admin
from django.urls import path, include
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', index, name=("index")),
    path('', home, name=("home")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
