from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, Field
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-register-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.label_class = 'col-lg-5'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            Fieldset(
                'Register',
                HTML("<hr>"),
                Field('first_name', label='name'),
                Field('username', label='Username'),
                Field('email', label='Email'),
                Field('password1', label='Password'),
                Field('password2', label='Confirm Password'),
            )
        )
        self.helper.add_input(Submit('submit', 'Sign Up'))
    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'first_name' : 'Name'
        }

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-login-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.label_class = 'col-lg-5'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            Fieldset(
                'Login',
                HTML("<hr>"),
                Field('username', label='Username'),
                Field('password', label='Password'),
            )
        )
        self.helper.add_input(Submit('submit', 'Login'))

    class Meta:
        model = User 
        fields = [
            'username',
            'password',
        ]