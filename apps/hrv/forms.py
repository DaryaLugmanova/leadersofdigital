from django.forms import ModelForm

from apps.hrv.models import HRV


class HRVUploadForm(ModelForm):
    class Meta:
        model = HRV
        fields = '__all__'
