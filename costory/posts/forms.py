from django import forms
from .models import Post
from .validators import validate_symbols
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm) :
    class Meta :
        model = Post
        fields = ['title', 'content'] # 모든 필드를 적용하기 위해서는 '__all__'
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'title', 'placeholder' : '제목을 입력하세요',}),
            'content' : forms.Textarea(attrs={'placeholder' : '내용을 입력하세요.'})
         }

    def clean_title(self) :
        title = self.cleaned_data['title']
        if '*' in self :
            raise ValidationError('"*"은 입력할 수 없습니다.')
        return title