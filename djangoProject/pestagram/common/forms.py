from django import forms

from common.models import Comment


class CommentForm(forms.Form):
    comment = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={
                                      'class': 'form-control rounded-2'
                                  }
                              ))


