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

@view_config(
  route_name='cars',
  renderer='json',
  request_method='POST'
)
def create_car(request):
  body = request.json_body
  new_car = { 
    "id": str(len(cars)),
    "make": body['make'],
    "model": body['model']
   }
  cars.append(new_car)
  return cars

@view_config(
  route_name='car',
  renderer='json',
  request_method='PATCH'
)
def update_car(request):
  car_id = request.matchdict['id']

  car_found = None
  for i in range(len(cars)):
    if cars[i]['id'] == car_id:
      car_found = i
      break
  
  if car_found == None:
    status_code = 404
    body = { "success": False, "message": "Not found" }
  else:
    cars[i] = { 
      "id": cars[i]['id'],
      "make": request.json_body['make'],
      "model": request.json_body['model']
    }
    status_code = 200
    body = { "success": True, "message": "Car successfully updated", "data": cars[i] }

  return Response(status=status_code, json_body=body)
  