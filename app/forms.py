from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=WebPage
        fields='__all__'
       # exclude=['name']
        labels={'topic_name':'TN','name':'N'}
        widgets={'name':forms.PasswordInput,'topic_name':forms.Textarea}

class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord 
        fields='__all__'