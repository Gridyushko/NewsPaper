from django import forms
from .models import Post
from django.core.exceptions import ValidationError



class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'title',
           'categoryType'
       ]

   def clean(self):
       cleaned_data = super().clean()
       description = cleaned_data.get("description")
       if description is not None and len(description) < 20:
           raise ValidationError({
               "description": "Описание не может быть менее 20 символов."
           })

       name = cleaned_data.get("name")
       if name == description:
           raise ValidationError(
               "Описание не должно быть идентично названию."
           )

       return cleaned_data



