from django.contrib.auth.forms import UserCreationForm

class EmailedUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email','first_name', 'last_name')

#This is a forms file
#This is a new-feature comment