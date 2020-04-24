from django.shortcuts import render
from django import forms
from django import views
from .models import *
from django.contrib.auth.models import  User

# Create your views here.

def home(request):
    msg='welcome to the polls, visitor'
    return render(request,'home.html',{'message':msg});


class DisplayPolls(views.View):


    def get(self,request):
        if User.is_authenticated:
            polls = Contestant.objects.values()
            return render(request, "votes.html", {"polls": polls})

    def post(self,request):
        if request.method=='POST' and not request.user.is_superuser:
            selected_option = request.POST['poll']
            try:
                polls = Contestant.objects.get(id=selected_option)
                print(polls.votes)
                polls.votes +=1
                print(polls,polls.votes)
                polls.save()
                return render(request, 'home.html', {'message': 'you casted your vote successfully'})
            except Contestant.DoesNotExist:
                return render(request, 'error.html', {'message': 'Contestant does not exits'})




class PollResults(views.View):

    def get(self,request):
        try:
            print('User:', User.is_superuser)
            if request.user.is_superuser and User.is_authenticated:
                dict_consts = Contestant.objects.values()
                results = dict()
                total_votes = 0
                for val in dict_consts:
                    results[val['contestant_name']] = val['votes']
                    total_votes += val['votes']
                return render(request, 'results.html', {'results': results, 'total_votes': total_votes})
            else:
                return render(request, 'results.html', {'error_message': 'you are not authoried to view this'})
        except Exception as e:
            print('Exception:',str(e))
            return render(request, 'error.html', {'error_message': 'you are not authoried to view this'})