from django import forms
from bootstrap_datepicker.widgets import DatePicker

class UserForm(forms.Form):
    keyword = forms.CharField(max_length=180)
    twitter = forms.BooleanField(required=False)
    reddit = forms.BooleanField(required=False)
    startdate = forms.DateTimeField(
                                    widget=DatePicker(
                                        options = {
                                        "format": "mm/dd/yyyy",
                                        "autoclose": True
                                        }
                                    ) )
    enddate = forms.DateTimeField(
                                    widget=DatePicker(
                                        options = {
                                        "format": "mm/dd/yyyy",
                                        "autoclose": True
                                        }
                                    ) )


    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        keyword = cleaned_data.get('keyword')
        twitter = cleaned_data.get('twitter')
        reddit = cleaned_data.get('reddit')
        if not keyword:
            raise forms.ValidationError('You have to search something!')
