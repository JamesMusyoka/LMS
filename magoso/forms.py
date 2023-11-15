from django import forms
from django.contrib.auth.models import User
from magoso.models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email','password1','password2')

        labels = {
            'password1' : 'Password',
            'password2' : 'Confirm Password'
        }


    class UserProfile(forms.ModelForm):
        bio = forms.CharField(required=False)
        instructor = 'instructor'
        student = 'student'
        admin = 'admin'
        user_types = [
            (instructor, 'instructor'),
            (student, 'student'),
            (admin, 'admin'),
        ]
        user_types = forms.ChoiceField(required=True, choices=user_types)
        
        fullstack = 'fullstack'
        frontend = 'frontend'
        backend = 'backend'
        grouping = [
            (fullstack, 'fullstack'),
            (frontend, 'frontend'),
            (backend, 'backend'),
        ]
        grouping = forms.ChoiceField(required=True, choices=grouping)

        cohort4 = 'cohort 4'
        cohort5 = 'cohort 5'
        cohort6 = 'cohort 6'
        cohort7 = 'cohort 7'
        cohort8 = 'cohort 8'
        cohort9 = 'cohort 9'
        cohort10 = 'cohort 10'
        cohort11 = 'cohort 11'
        cohort12 = 'cohort 12'
        cohort13 = 'cohort 13'
        cohort14 = 'cohort 14'
        cohort15 = 'cohort 15'
        cohort16 = 'cohort 16'
        cohort = [
            (cohort4, 'cohort 4'),
            (cohort5, 'cohort 5'),
            (cohort6, 'cohort 6'),
            (cohort7, 'cohort 7'),
            (cohort8, 'cohort 8'),
            (cohort9, 'cohort 9'),
            (cohort10, 'cohort 10'),
            (cohort11, 'cohort 11'),
            (cohort12, 'cohort 12'),
            (cohort13, 'cohort 13'),
            (cohort14, 'cohort 14'),
            (cohort15, 'cohort 15'),
            (cohort16, 'cohort 16'),
        ]
        cohort = forms.ChoiceField(required=True, choices=cohort)

        class Meta():
            model = UserProfile
            fields = ('bio', 'profile_pic', 'user_types', 'grouping', 'cohort')
