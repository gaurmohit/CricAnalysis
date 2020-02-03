from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(label="username",
                             required = True,
                             max_length=20,
                            )

    email = forms.CharField(required = True,
                            label = 'Email',
                            max_length = 32,
                            )

    password=forms.CharField(label="password",
                             required = True,
                             max_length=20,
                             widget = forms.PasswordInput(),
                             )
# from django import forms

# class RegisterForm(forms.Form):
#     username=forms.CharField(label="username",
#                              required = True,
#                              max_length=20,
#                             )

#     email = forms.CharField(required = True,
#                             label = 'Email',
#                             max_length = 32,
#                             )

#     phno = forms.CharField(required = True,
#                            label = 'phno',
#                            max_length = 12,
#                             )
    
#     city = forms.CharField(label = 'city',
#                            max_length= 25,
#                            )

#     password=forms.CharField(label = "password",
#                              required = True,
#                              max_length = 20,
#                              widget = forms.PasswordInput(),
#                              )
