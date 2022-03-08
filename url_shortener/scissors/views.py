from django.views.generic import list
from .models import Url


class UrlListView(list.ListView):
    model = Url
    template_name = 'index.html'
    queryset = Url.objects.all()
