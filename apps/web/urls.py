from django.urls import path

from apps.web.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
