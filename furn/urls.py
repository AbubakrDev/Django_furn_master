from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'furn'

urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name='signup'),
    path('profile', profile, name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_redirect, name='logout-redirect'),
    path('logout-link', LogoutView.as_view(), name='logout-link'),
    path('<int:pk>/details/', arrivals_detail, name='arrival_detail'),
    path('rate/', rate, name='rate'),
    path('rate-image/', rate_image, name='rate-image'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
