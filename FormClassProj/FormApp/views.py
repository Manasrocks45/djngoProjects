from django.shortcuts import render
from . import forms

# Create your views here.
def studentRegistrationForms(request):
    form=forms.StudentRegistration()#create object of form class and send that form object to html file.No extra Configuration nedded in settings.py file
    return render(request,'register.html',context={'form':form})


#form2
def welcomeView(request):
    return render(request,'welcome.html')#use another page in render otherwise same page will e display due to below return

def studentFeedbackForms(request):
    if request.method=='GET':
            form=forms.FeedbackForm()

    #after submit form(post) request is going to come on same page view because we did not define any action
#get data from form request Postif request.method=='POST':

    if request.method=='POST':
        form=forms.FeedbackForm(request.POST)#create new form object with coming data
        if form.is_valid():
            print('Form validation success and printing feedback info')
            print('student Name',form.cleaned_data['name'])#all our form data we get from prdefined dict var-cleaned_data==>{'name':form value}
            print('student Rollno',form.cleaned_data['rollno'])
            print('student Email',form.cleaned_data['email'])
            print('student Name',form.cleaned_data['feedback'])
            #return welcomeView(request)
    return render(request,'feedback.html',context={'form':form})
