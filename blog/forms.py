from django import forms
from .models import *

class EditBlog(forms.ModelForm):
    class Meta():
        model = Blog 
        exclude =('author',)
    
    def __init__(self, *args, **kwargs):
        super(EditBlog,self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class']='form-control'
            
class CreatePost(forms.ModelForm):
    class Meta():
        model = Blog 
        exclude =('author',)
    
    def __init__(self, *args, **kwargs):
        super(CreatePost,self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class']='form-control'
        
        
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs 
        exclude =('user',)
        
    def __init__(self, *args, **kwargs):
        super(ContactUsForm,self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class']='form-control'