from django.urls import path
from .views import UrlListView, UrlCreateView, UrlRedirectView, UrlCopyPathView

app_name = 'scissors'
urlpatterns = [
    path('', UrlListView.as_view(), name='list-url'),
    path('url/', UrlCreateView.as_view(), name='create-url'),
    path('s/<str:path>/', UrlRedirectView.as_view(), name='redirect-url'),
    path('<int:pk>/', UrlCopyPathView.as_view(), name='copy-url'),
]
