from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home,contact,about,news,Service
urlpatterns = [
    path('',home , name='Home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('service/', Service, name='service'),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
