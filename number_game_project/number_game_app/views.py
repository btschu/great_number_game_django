import re
from django.shortcuts import render, redirect
import random

def index(request):
    #Check to see if random is stored in session.  If not, then clear message and generate a random number between 1 and 100 to be stored in session.
    if 'randomNum' not in request.session:
        request.session['numTries']= 0
        request.session['guess']= -1
        request.session['randomNum'] = random.randrange(1,101)
        print(request.session['numTries'])
        print(request.session['randomNum'])
        print(request.session['guess'])
    return render(request,"index.html")

def guess(request):
    if 'numTries' in request.session:
        request.session['numTries'] += 1
    else:
        request.session['numTries'] = 0
    request.session['guess'] = int(request.POST['guess'])
    request.session['randomNum'] = int(request.session['randomNum'])
    return redirect("/")

def play_again(request):
    #Have route clear session. 
    del request.session['numTries']
    del request.session['randomNum']
    del request.session['guess']
    return redirect("/")