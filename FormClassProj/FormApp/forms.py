from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    """docstring forStudentRegistration."""
    name=forms.CharField()  #no need to given length here like models. it is optional
    marks=forms.IntegerField()





"""
def name_start_d(arg):
    if arg[0].lower()!='d':
        raise forms.ValidationError("Name should start with d")

        """


class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Pass(Repeat)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(5)])#Inbulit validation
    bot_kicker=forms.CharField(required=False,widget=forms.HiddenInput)#required=False so that  end-user will not provide its data to check bot access

    #All validations inside child clean method calling Parent class clean method in place of different cleaned method
    def clean(self):
        cleaned_data=super().clean()
        inputname=cleaned_data['name']
        inputrollno=cleaned_data['rollno']
        inputpwd=cleaned_data['password']
        rinputpwd=cleaned_data['rpassword']
        bot_kicker_value=cleaned_data['bot_kicker']

        print("Custom Validation")
        if len(inputname)<10:
            raise forms.ValidationError("Custom The Length of the name filled should>=10")

        if len(str(inputrollno))>4:
            raise forms.ValidationError("Custom The Length of the rollno filled should>=8")

        if inputpwd !=rinputpwd:
            raise forms.ValidationError("Password Not matched")

        if len(bot_kicker_value)>0:
            raise forms.ValidationError("Get Out Bot")
