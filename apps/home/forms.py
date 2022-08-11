from django import forms 
from .models import UploadCaseFile


#DataFlair #File_Uploa

    

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Upload Case files', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadCaseFile
        fields = [
        'uploadfile','language'
        ]
    