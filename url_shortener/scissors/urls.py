from django.urls import path
from .views import UrlListView, UrlCreateView

app_name = 'scissors'
urlpatterns = [
    path('', UrlListView.as_view(), name='list-url'),
    path('url/', UrlCreateView.as_view(), name='create-url'),

]
