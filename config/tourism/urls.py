
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('popular/', popular, name='popular'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('bystate/', bystate, name='bystate'),
    path('bytype/', bytype, name='bytype'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)