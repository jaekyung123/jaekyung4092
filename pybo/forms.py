from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'image']
        labels = {
            'subject':'제목',
            'content':'내용',
            'image':'이미지'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content', 'image']
        labels = {
            'content': '답변내용',
            'image':'이미지'
        }
