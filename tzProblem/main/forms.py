from django import forms
from main.models import Article


class ArticleForm(forms.ModelForm):
    pubDateTime = forms.DateTimeField(label='Publish date time', widget=forms.TextInput(attrs={'class':'datetimepicker', 'readonly':True}))
    
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        print('In form (8 hrs short):', self.instance.pubDateTime)
    
    class Meta:
        model = Article
        fields = '__all__'
