"""devSearchProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import projects.urls

from django.http import HttpResponse

from django.conf.urls.static import static
from django.conf import settings

def helloHandler(httpRequest):
    httpResponse = HttpResponse("<h1>Hello, World!</h1>")
    return httpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', helloHandler), # for introduction
    path('',include(projects.urls)) # need to know my project that we have paths in other file
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
