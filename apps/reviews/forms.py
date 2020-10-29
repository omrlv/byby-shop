from django.forms import ModelForm
from .models import Review

class FormReview(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
