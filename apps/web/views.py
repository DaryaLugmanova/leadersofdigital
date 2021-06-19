from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib import messages

from apps.hrv.forms import HRVUploadForm


class IndexView(FormView):
    template_name = 'web/index.html'
    form_class = HRVUploadForm

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Ритмограмма успешно сохранена.')
        return redirect('index')
