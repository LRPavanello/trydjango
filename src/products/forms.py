from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    email       = forms.EmailField()
    comment     = forms.CharField()
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={"class": "new-class-name",
                   "placeholder": "Your Description",    
                   "id": "my-id-for-textarea", 
                   "row": 20, 
                   "cols":120
                }))
    price       = forms.DecimalField(initial=0)  
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "LRP" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")
        
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("This is not a valid email")        
        return email
    
    def clean_comment(self, *args, **kwargs):
        comment = self.cleaned_data.get("comment")
        if len(comment) < 0:
            raise forms.ValidationError("This is not a valid Comment")        
        return comment    
    
class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"})) 
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={"class": "new-class-name",
                   "placeholder": "Your Description",    
                   "id": "my-id-for-textarea", 
                   "row": 20, 
                   "cols":120
                }))
    price       = forms.DecimalField(initial=200) 