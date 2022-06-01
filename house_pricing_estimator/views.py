from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Houses, Predictions
from .back import linear_model

def index(request):
  myHouses = Houses.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'myHouses': myHouses,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
	floor_number = int(request.POST['floor_number'])
	year_construction = int(request.POST['year_construction'])
	square_meters = float(request.POST['square_meters'])
	rooms_number = int(request.POST['rooms_number'])
	baths_number = int(request.POST['baths_number'])
	has_elevator = request.POST.get('has_elevator', False) == "on"

	house = Houses(
		floor_number=floor_number, 
		year_construction=year_construction,
		square_meters=square_meters,
		rooms_number=rooms_number,
		baths_number=baths_number,
		has_elevator=has_elevator
	)
	house.save()
	return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Houses.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  myHouse = Houses.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'myHouse': myHouse,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
	floor_number = request.POST['floor_number']
	year_construction = request.POST['year_construction']
	square_meters = request.POST['square_meters']
	rooms_number = request.POST['rooms_number']
	baths_number = request.POST['baths_number']
	has_elevator = request.POST.get('has_elevator', False) == "on"

	house = Houses.objects.get(id=id)
	house.floor_number = floor_number
	house.year_construction = year_construction
	house.square_meters = square_meters
	house.rooms_number = rooms_number
	house.baths_number = baths_number
	house.has_elevator = has_elevator
	house.save()
	return HttpResponseRedirect(reverse('index'))

def predictions(request, id):
  myHouse = Houses.objects.get(id=id)
  template = loader.get_template('predictions.html')
  context = {
    'myHouse': myHouse,
  }
  return HttpResponse(template.render(context, request))


def updatepredictions(request, id):
	floor_number = float(request.POST['floor_number'])
	year_construction = float(request.POST['year_construction'])
	square_meters = float(request.POST['square_meters'])
	rooms_number = float(request.POST['rooms_number'])
	baths_number = float(request.POST['baths_number'])
	has_elevator = boolean(request.POST['has_elevator'])

	price = linear_model(floor_number, year_construction, square_meters, rooms_number, baths_number)
	
	house = Houses.objects.get(id=id)
	Predictions.objects.filter(house=house).delete()

	predicitions_model = Predictions(id=None, model_name="Simple Linear Model", price=price, house=house)
	predicitions_model.save()	

	return HttpResponseRedirect(reverse("predictions", args=(id,)))