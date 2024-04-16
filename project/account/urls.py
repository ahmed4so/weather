from django.urls import path
from .views import login_user,registration,logout_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login',login_user,name='login'),
    path('register', registration, name='register'),
    path('logout', logout_view, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
