

from django.urls import path
from .views import UserRecordView
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
]