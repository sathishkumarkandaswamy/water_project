from django.forms import ModelForm
from water_app.models import WaterParameter


class WaterParameterForm(ModelForm):
    class Meta:
        model = WaterParameter
        fields = '__all__'
