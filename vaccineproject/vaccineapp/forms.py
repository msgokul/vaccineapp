from django import forms

from .models import People, Taluk


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'

        widgets ={
            'district':forms.Select(attrs={'class':'form-control'}),
            'taluk': forms.Select(attrs={'class': 'form-control'}),
            'vaccine': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control','type':'date'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['taluk'].queryset = Taluk.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['taluk'].queryset = Taluk.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['taluk'].queryset = self.instance.district.taluk_set.order_by('name')


