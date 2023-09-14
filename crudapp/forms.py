from django import forms

from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model= Person
        fields=['name','details']
        #labels={'text':''}
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control',}),
            'details':forms.Textarea(attrs={'class':'form-control',})
        }

"""class DetailForm(forms.ModelForm):
    class Meta:
        model=Details
        fields=['text']
        labels={'text':''}       
        widgets={'tet':forms.Textarea(attrs={'cols': 80})}"""