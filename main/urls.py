from django.urls import path
from .views import index  #из этой же папки импорт index()

app_name = 'main'

urlpatterns = [
    path('', index, name = 'index')
]