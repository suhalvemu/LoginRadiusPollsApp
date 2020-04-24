from django.shortcuts import render
from django import forms
from django.http import  HttpResponseRedirect
from django.views.generic import  TemplateView
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import reverse


# Create your views here.
def logout_request(request):
    logout(request)
    return render(request,'home.html',{'message':'you are logged out successfully'})


class FormLogin(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ViewLogManual(TemplateView):

    def get(self, request, *args, **kwargs):
        form = FormLogin()
        return render(self.request,'login.html',{'form':form})

    def post(self,*args,**kwargs):
        form = FormLogin(self.request.POST)

        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                print(user.is_superuser)
                if user.is_active and not user.is_superuser:
                    print(self.request)
                    login(self.request,user)
                    return HttpResponseRedirect(reverse('votes'))
                else:
                    login(self.request, user)
                    return HttpResponseRedirect(reverse('results'))
            else:
                return  render(self.request,'login.html',{'error_message':'invalid credentials',
                                                          'form':form
                                                          })
        return render(self.request,'login.html',{})

