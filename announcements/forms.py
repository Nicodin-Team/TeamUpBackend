from django import forms
from .models import AnnouncementApply, Announcement
from django.core.validators import FileExtensionValidator
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget






class AnnouncementApplyForm(forms.ModelForm):
    cv = forms.FileField(
        label='CV',
        widget=forms.ClearableFileInput(attrs={'accept': '.pdf'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'], message='Only PDF files are allowed.')]
    )
    class Meta:
        model = AnnouncementApply
        fields = ['username', 'email', 'linkedIn_url', 'githup_url', 'cv', 'cover_letter']
       

class AnnouncementForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Announcement
        fields = ['title', 'location', 'company', 'salary_start', 'salary_end', 'description', 'vacancy', 'job_type', 'experience', 'category']