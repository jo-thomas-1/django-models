from django.shortcuts import render
from . models import Place, Team

# Create your views here.

def home(request):
	places = Place.objects.all()
	team = Team.objects.all()

	return render(request, 'index.html', {'places': places, 'team': team})