from django.urls import path

from car.views import car_list, car_detail

urlpatterns = [
    path("cars/", car_list, name="car_list"),
    path("car/<int:pk>/", car_detail, name="car_detail"),
]

app_name = "car"
