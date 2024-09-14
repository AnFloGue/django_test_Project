from django import forms

class TeacherForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], label='Gender')