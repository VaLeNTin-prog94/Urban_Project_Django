from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'board'

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('advertisements/<int:pk>/like/', views.like_ad, name='like_ad'),
    path('advertisements/<int:pk>/dislike/', views.dislike_ad, name='dislike_ad'),
    path('add/', views.add_advertisement, name='add_advertisement'),
    path('edit/<int:pk>', views.edit_advertisement, name='edit_advertisement'),
    path('delete/<int:pk>', views.delete_advertisement, name='delete_advertisement'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)