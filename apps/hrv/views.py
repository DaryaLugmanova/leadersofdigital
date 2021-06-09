from django.views.generic import TemplateView


class HRVUploadView(TemplateView):
    template_name = 'hrv/upload.html'


class HRVResultView(TemplateView):
    template_name = 'hrv/result.html'
