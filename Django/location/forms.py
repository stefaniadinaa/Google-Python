from django import forms

from location.models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'country']

    def __init__(self, pk, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.pk = pk
