from django import forms

from .models import Tags, Note


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NoteForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Note
        fields = ['pinned', 'color', 'title', 'tag', 'description']


class TagForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Tags
        fields = '__all__'