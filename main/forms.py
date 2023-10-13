from django.forms import ModelForm
from main.models import Record

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ["name", "amount", "description", "genre", "price", "image"]
        # fields = ["name", "amount", "description", "genre", "price", "picture"]

    # def __init__(self, args, **kwargs):
    #         super(RecordForm, self).__init__(args, **kwargs)
    #         self.fields['picture'].required = False