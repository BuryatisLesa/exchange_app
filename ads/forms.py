from django import forms
from .models import Ad, ExchangeProposal

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'image', 'category', 'condition']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Категория'}),
            'condition': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'category': 'Категория',
            'condition': 'Состояние',
            'image': 'Изображение',
        }

class ExchangeProposalForm(forms.ModelForm):
    class Meta:
        model = ExchangeProposal
        fields = ['ad_sender', 'ad_receiver', 'comment']
        widgets = {
            'ad_sender': forms.Select(attrs={'class': 'form-select'}),
            'ad_receiver': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['ad_sender'].queryset = Ad.objects.filter(user=user)
