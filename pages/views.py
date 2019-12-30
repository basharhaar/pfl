from django.shortcuts import render
from .models import Registration

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def fixtures(request):
    return render(request, 'pages/fixtures.html')

def rules(request):
    return render(request, 'pages/rules.html')

def live_matches(request):
    return render(request, 'pages/live_matches.html')


def ranking(request):
    return render(request, 'pages/ranking.html')

def venue(request):
    return render(request, 'pages/venue.html')

def registration(request):
    return render(request, 'pages/registration.html')

def save_reg(request):
      if request.method == 'POST':
        team_name =request.POST["team_name"]
        player_names = request.POST["player_names"]
        city = request.POST["city"]
        team_manager = request.POST["team_manager"]
        team_manager_phonenumber = request.POST["team_manager_phonenumber"]
        team_manager_cnic = request.POST["team_manager_cnic"]
        team_captain = request.POST["team_captain"]
        team_captain_phonenumber = request.POST["team_captain_phonenumber"]
        extra_remarks = request.POST["extra_remarks"]
        

        save_reg = Registration(team_name=team_name, player_names=player_names, city=city, 
                                team_manager=team_manager, team_manager_phonenumber=team_manager_phonenumber, 
                                team_manager_cnic=team_manager_cnic, team_captain=team_captain, 
                                team_captain_phonenumber=team_captain_phonenumber, extra_remarks=extra_remarks)
        save_reg.save()


        

      return render(request, 'pages/registration.html')