from django.forms import ModelForm
from water_app.models import WaterParameter


class WaterParameterForm(ModelForm):
    class Meta:
        model = WaterParameter
        fields = '__all__'
        labels = {
            'title': 'Title',
            'description': 'Description',
            'coliform_bacteria': 'Coliform Bacteria',
            'nitrate': 'Nitrate',
            'ph': 'pH',
            'sodium': 'Sodium',
            'chloride': 'Chloride',
            'fluride': 'Fluride',
            'sulphate': 'Sulphate',
            'iron': 'Iron',
        }
