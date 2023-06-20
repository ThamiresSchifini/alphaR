from django import forms

from alphaR.planet.models.planet import Planet


class PlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = '__all__'