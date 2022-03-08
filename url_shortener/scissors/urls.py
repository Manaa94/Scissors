from django.urls import path
from .views import UrlListView


urlpatterns = [
    path('', UrlListView.as_view(), name='list-url'),
]
