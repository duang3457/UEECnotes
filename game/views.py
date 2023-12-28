from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required(login_url='/home/')
def game(request):
    User = request.user
    return render(request, "game/game.html")