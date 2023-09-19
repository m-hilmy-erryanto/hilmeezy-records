from django.forms import ModelForm
from main.models import Record

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ["name", "amount", "description", "genre", "price"]