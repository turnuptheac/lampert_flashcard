from django.forms import ModelForm, TextInput, Textarea
from .models import Flashcard

class FlashcardForm(ModelForm):
  class Meta: 
    model = Flashcard
    fields = ['word', 'definition']
    widgets = {
      'word': TextInput(attrs={'placeholder': 'word'}),
      'definition': Textarea(attrs={
        'placeholder': "a single distinct meaningful element of speech or writing, used with others to form a sentence and typically shown with a space on either side when written or printed."
      })
    }