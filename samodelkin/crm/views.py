from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import Visits



def today(request):
    now = Visits.objects.all()
    return render(request, 'start.html', {'today': today})


def auth_admin(request):
    if request.method == 'POST':
        form = request.POST
        user = authenticate(username = form['email'], password = form['psw'])
        print(form)
        if user is not None:
            request.session['for_auth'] = 'log'
            return render(request, 'start.html')
        if user == None:
            return render(request, 'index.html')
    else:
        return render(request, 'authorization.html')



