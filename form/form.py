from django import forms
from bootstrap_datepicker.widgets import DatePicker

import datetime

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
        ##print(cleaned_data)
        keyword = cleaned_data.get('keyword')
        twitter = cleaned_data.get('twitter')
        reddit = cleaned_data.get('reddit')
        start_date = cleaned_data.get('startdate')
        ##print(start_date)
        end_date = cleaned_data.get('enddate')
        ##print(end_date)
        if not keyword:
            raise forms.ValidationError('Please Enter a Keyword.')
        if not start_date:
            raise forms.ValidationError('Please enter a start date.')
        if not start_date:
            raise forms.ValidationError('Please enter an end date.')
        
        if not twitter and not reddit:
            raise forms.ValidationError('Please select a platform.')
        elif twitter and reddit:
            raise forms.ValidationError('You can only select one platform.')
        else:
            ##print('else')
            if twitter and not reddit:
                onewk = datetime.datetime.now() - datetime.timedelta(days=7)
                ##print(onewk)
                if end_date.date() < onewk.date():
                    raise forms.ValidationError('Twitter can only get results from 7 days ago. You have selected a date that is over 7 days ago.')

