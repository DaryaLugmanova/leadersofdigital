from django.urls import path

from apps.hrv.views import HRVUploadView, HRVResultView

urlpatterns = [
    path('upload', HRVUploadView.as_view(), name='upload'),
    path('result', HRVResultView.as_view(), name='result'),
]
