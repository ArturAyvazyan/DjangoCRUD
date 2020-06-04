"""naukaWelcome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf.urls import url
from srk import views


urlpatterns = [
    path('', views.home, name='home'),#нэйм - ссылка на название вью
    path('empl_list/', views.empl_list, name ='empl_list'),
    path('empl_upload/', views.empl_upload, name ='empl_upload'),
    path('<int:pk>/', views.delete_empl, name ='delete_empl'),
    url(r'^edit/(?P<pk>\d+)$', views.update_empl, name='empl_upload'),

    path('admin/', admin.site.urls),
]

#urlpatterns = [
#    url(r'^edit/(?P<pk>\d+)$', views.empl_upload, name='empl_upload'),]

if settings.DEBUG: #Специальное вью из джанго.конф для генерации ссылок на медиа-файлы
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

