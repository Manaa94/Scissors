from django.views.generic import list, edit
from django.urls import reverse
from .models import Url
from .forms import UrlForm


class UrlListView(list.ListView):
    model = Url
    template_name = 'index.html'
    queryset = Url.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UrlForm
        return context


class UrlCreateView(edit.CreateView):
    form_class = UrlForm
    template_name = 'index.html'

    def get_success_url(self):
        return reverse('scissors:list-url')
