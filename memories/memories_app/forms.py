from django import forms
from memories_app.models import People


class PeopleForm(forms.ModelForm):
    email=forms.EmailField(
        # required = True,
        widget = forms.EmailInput(
            attrs = {"placeholder":"Enter email",'class':'form-control input-jp','onfocus':"this.placeholder=''", 'onblur':"this.placeholder = 'Enter email'"}
            # attrs = {"placeholder":"Enter email here",'form-control','onfocus':"this.placeholder=''", 'onblur':"this.placeholder = 'Email'"}
        ),
    )

    class Meta:
        model = People
        fields = ('email',)