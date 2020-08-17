from pyramid.response import Response
from pyramid.view import view_config

cars = [
  { "id": "0", "make": "Chevrolet", "model": "Onix" },
  { "id": "1", "make": "Volkswagen", "model": "Fox" },
  { "id": "2", "make": "Peugeot", "model": "306" }
]



@view_config(
  route_name='cars', 
  renderer='json', 
  request_method='GET'
)
def get_cars(request):
  return cars
