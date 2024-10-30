from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:user_id>/<str:query>/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shortener/', views.generate, name='generate'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard'),
    path('dashboard/edit/<str:pk>/', views.edit, name='edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)