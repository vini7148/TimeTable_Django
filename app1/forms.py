from django import forms
from .models import Class, Teacher

# create your forms here

class Class_in(forms.ModelForm):
    Number = forms.IntegerField()
    Section = forms.CharField(max_length=2)

    Monday_0 = forms.CharField(max_length=200, required=False)
    Monday_1 = forms.CharField(max_length=200, required=False)
    Monday_2 = forms.CharField(max_length=200, required=False)
    Monday_3 = forms.CharField(max_length=200, required=False)
    Monday_4 = forms.CharField(max_length=200, required=False)
    Monday_5 = forms.CharField(max_length=200, required=False)
    Monday_6 = forms.CharField(max_length=200, required=False)
    Monday_7 = forms.CharField(max_length=200, required=False)
    Monday_8 = forms.CharField(max_length=200, required=False)
    
    Tuesday_0 = forms.CharField(max_length=200, required=False)
    Tuesday_1 = forms.CharField(max_length=200, required=False)
    Tuesday_2 = forms.CharField(max_length=200, required=False)
    Tuesday_3 = forms.CharField(max_length=200, required=False)
    Tuesday_4 = forms.CharField(max_length=200, required=False)
    Tuesday_5 = forms.CharField(max_length=200, required=False)
    Tuesday_6 = forms.CharField(max_length=200, required=False)
    Tuesday_7 = forms.CharField(max_length=200, required=False)
    Tuesday_8 = forms.CharField(max_length=200, required=False)

    Wednesday_0 = forms.CharField(max_length=200, required=False)
    Wednesday_1 = forms.CharField(max_length=200, required=False)
    Wednesday_2 = forms.CharField(max_length=200, required=False)
    Wednesday_3 = forms.CharField(max_length=200, required=False)
    Wednesday_4 = forms.CharField(max_length=200, required=False)
    Wednesday_5 = forms.CharField(max_length=200, required=False)
    Wednesday_6 = forms.CharField(max_length=200, required=False)
    Wednesday_7 = forms.CharField(max_length=200, required=False)
    Wednesday_8 = forms.CharField(max_length=200, required=False)

    Thursday_0 = forms.CharField(max_length=200, required=False)
    Thursday_1 = forms.CharField(max_length=200, required=False)
    Thursday_2 = forms.CharField(max_length=200, required=False)
    Thursday_3 = forms.CharField(max_length=200, required=False)
    Thursday_4 = forms.CharField(max_length=200, required=False)
    Thursday_5 = forms.CharField(max_length=200, required=False)
    Thursday_6 = forms.CharField(max_length=200, required=False)
    Thursday_7 = forms.CharField(max_length=200, required=False)
    Thursday_8 = forms.CharField(max_length=200, required=False)

    Friday_0 = forms.CharField(max_length=200, required=False)
    Friday_1 = forms.CharField(max_length=200, required=False)
    Friday_2 = forms.CharField(max_length=200, required=False)
    Friday_3 = forms.CharField(max_length=200, required=False)
    Friday_4 = forms.CharField(max_length=200, required=False)
    Friday_5 = forms.CharField(max_length=200, required=False)
    Friday_6 = forms.CharField(max_length=200, required=False)
    Friday_7 = forms.CharField(max_length=200, required=False)
    Friday_8 = forms.CharField(max_length=200, required=False)

    Saturday_0 = forms.CharField(max_length=200, required=False)
    Saturday_1 = forms.CharField(max_length=200, required=False)
    Saturday_2 = forms.CharField(max_length=200, required=False)
    Saturday_3 = forms.CharField(max_length=200, required=False)
    Saturday_4 = forms.CharField(max_length=200, required=False)
    Saturday_5 = forms.CharField(max_length=200, required=False)
    Saturday_6 = forms.CharField(max_length=200, required=False)
    Saturday_7 = forms.CharField(max_length=200, required=False)
    Saturday_8 = forms.CharField(max_length=200, required=False)

    class Meta():
        model = Class
        exclude = ()

class Class_se(forms.Form):
    Number = forms.IntegerField()
    Section = forms.CharField(max_length=2)

class Teacher_in(forms.ModelForm):
    First_Name = forms.CharField(max_length=100)
    Last_Name = forms.CharField(max_length=100)
    Subject = forms.CharField(max_length=100)

    Monday_0 = forms.CharField(max_length=200, required=False)
    Monday_1 = forms.CharField(max_length=200, required=False)
    Monday_2 = forms.CharField(max_length=200, required=False)
    Monday_3 = forms.CharField(max_length=200, required=False)
    Monday_4 = forms.CharField(max_length=200, required=False)
    Monday_5 = forms.CharField(max_length=200, required=False)
    Monday_6 = forms.CharField(max_length=200, required=False)
    Monday_7 = forms.CharField(max_length=200, required=False)
    Monday_8 = forms.CharField(max_length=200, required=False)
    
    Tuesday_0 = forms.CharField(max_length=200, required=False)
    Tuesday_1 = forms.CharField(max_length=200, required=False)
    Tuesday_2 = forms.CharField(max_length=200, required=False)
    Tuesday_3 = forms.CharField(max_length=200, required=False)
    Tuesday_4 = forms.CharField(max_length=200, required=False)
    Tuesday_5 = forms.CharField(max_length=200, required=False)
    Tuesday_6 = forms.CharField(max_length=200, required=False)
    Tuesday_7 = forms.CharField(max_length=200, required=False)
    Tuesday_8 = forms.CharField(max_length=200, required=False)

    Wednesday_0 = forms.CharField(max_length=200, required=False)
    Wednesday_1 = forms.CharField(max_length=200, required=False)
    Wednesday_2 = forms.CharField(max_length=200, required=False)
    Wednesday_3 = forms.CharField(max_length=200, required=False)
    Wednesday_4 = forms.CharField(max_length=200, required=False)
    Wednesday_5 = forms.CharField(max_length=200, required=False)
    Wednesday_6 = forms.CharField(max_length=200, required=False)
    Wednesday_7 = forms.CharField(max_length=200, required=False)
    Wednesday_8 = forms.CharField(max_length=200, required=False)

    Thursday_0 = forms.CharField(max_length=200, required=False)
    Thursday_1 = forms.CharField(max_length=200, required=False)
    Thursday_2 = forms.CharField(max_length=200, required=False)
    Thursday_3 = forms.CharField(max_length=200, required=False)
    Thursday_4 = forms.CharField(max_length=200, required=False)
    Thursday_5 = forms.CharField(max_length=200, required=False)
    Thursday_6 = forms.CharField(max_length=200, required=False)
    Thursday_7 = forms.CharField(max_length=200, required=False)
    Thursday_8 = forms.CharField(max_length=200, required=False)

    Friday_0 = forms.CharField(max_length=200, required=False)
    Friday_1 = forms.CharField(max_length=200, required=False)
    Friday_2 = forms.CharField(max_length=200, required=False)
    Friday_3 = forms.CharField(max_length=200, required=False)
    Friday_4 = forms.CharField(max_length=200, required=False)
    Friday_5 = forms.CharField(max_length=200, required=False)
    Friday_6 = forms.CharField(max_length=200, required=False)
    Friday_7 = forms.CharField(max_length=200, required=False)
    Friday_8 = forms.CharField(max_length=200, required=False)

    Saturday_0 = forms.CharField(max_length=200, required=False)
    Saturday_1 = forms.CharField(max_length=200, required=False)
    Saturday_2 = forms.CharField(max_length=200, required=False)
    Saturday_3 = forms.CharField(max_length=200, required=False)
    Saturday_4 = forms.CharField(max_length=200, required=False)
    Saturday_5 = forms.CharField(max_length=200, required=False)
    Saturday_6 = forms.CharField(max_length=200, required=False)
    Saturday_7 = forms.CharField(max_length=200, required=False)
    Saturday_8 = forms.CharField(max_length=200, required=False)

    class Meta():
        model = Teacher
        # fields = ('First_Name', 'Last_Name', 'Subject')
        exclude = ()

class Teacher_se(forms.Form):
    First_Name = forms.CharField(max_length=100)
    Last_Name = forms.CharField(max_length=100)