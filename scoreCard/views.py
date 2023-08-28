from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Golfer
from .models import BarPar
from .forms import ScoreForm


# Create your views here.
def index(request):
    golfers = Golfer.objects.all()
    return render(request, "cards/index.html", {"golfers": golfers})


def scorecards(request):
    golfers = Golfer.objects.all()
    return render(request, "cards/scoreSheet.html", {"golfers": golfers})


# Need to get the logged in users data to this page
def userscore(request):
    golfer = Golfer.objects.filter(user__id=request.user.id).first()
    bar_par = BarPar.objects.all().first()
    par = [bar_par.do_dodge, bar_par.elbow_room, bar_par.wigwam, bar_par.depot, bar_par.sports_page, bar_par.reboot, bar_par.mouse_trap, bar_par.clancys, bar_par.dooleys, bar_par.gi, bar_par.brothers, bar_par.pio, bar_par.pickle, bar_par.shenanns, bar_par.brat]
    form = ScoreForm(request.POST or None, instance=golfer)
    if form.is_valid():
        form.save()
        golfer = Golfer.objects.filter(user__id=request.user.id).first()
        golfer.total = golfer.do_dodge + golfer.elbow_room + golfer.wigwam + golfer.depot + golfer.sports_page + golfer.reboot + golfer.mouse_trap + golfer.clancys + golfer.dooleys + golfer.gi + golfer.brothers + golfer.pio + golfer.pickle + golfer.shenanns + golfer.brat
        golfer.save()
        messages.success(request, ("Your Score has been updated! Total: " + str(golfer.total)))
    return render(request, "cards/userScore.html", {'form': form, 'golfer': golfer, 'par': par})


def rules(request):
    tmp_text = "This is the rules page"
    return render(
        request,
        "cards/rules.html",
        {
            "tmp_text": tmp_text,
        },
    )

def reset_all(requst):
    if not requst.user.is_superuser:
        messages.success(requst, ("You must be an admin to reset all scores!"))
        return redirect("index")
    golfers = Golfer.objects.all()
    for golfer in golfers:
        golfer.do_dodge = 0
        golfer.elbow_room = 0
        golfer.wigwam = 0
        golfer.depot = 0
        golfer.sports_page = 0
        golfer.reboot = 0
        golfer.mouse_trap = 0
        golfer.clancys = 0
        golfer.dooleys = 0
        golfer.gi = 0
        golfer.brothers = 0
        golfer.pio = 0
        golfer.pickle = 0
        golfer.shenanns = 0
        golfer.brat = 0
        golfer.total = 0
        golfer.save()
    messages.success(requst, ("All Scores have been reset!"))
    return redirect("index")
