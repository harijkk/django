from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name='home'),
    path('templates/jee.html',views.jee,name='jee'),
    path('templates/year.html',views.year,name='year'),
    path('templates/add1',views.add1,name='add'),
    path('templates/home1',views.home1),
    path('templates/about.html',views.about1,name='about'),
    path('templates/vit.html',views.vit,name='vit')

    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)