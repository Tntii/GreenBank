from django.shortcuts import render
from GB.script import error, interval
from GB.models import *


# Create your views here.
def index(request):

    types = TypeRate.objects.order_by("type")
    energies = EnergieRate.objects.order_by("energie")

    context={"types": types, "energies": energies}
    return render(request, "index.html", context=context)


def add_car(request):
    have_error = False
    car_type = request.POST.get("car-type")

    car_year = request.POST.get("car-year")
    if error.int_error(car_year):
        have_error = True
        car_year = "error"

    car_energie = request.POST.get("car-energie")

    car_passager = request.POST.get("car-passager")
    if error.int_error(car_passager):
        have_error = True
        car_passager = "error"

    car_km = request.POST.get("dist")
    if error.int_error(car_km):
        have_error = True
        car_km = "error"

    if not have_error:
        try:
            car_year = int(car_year)
            car_km = int(car_km)

            vh_rate = TypeRate.objects.get(type=car_type).rate
            en_rate = EnergieRate.objects.get(energie=car_energie).rate
            y_rate = interval.interval(YearRate.objects.all(), car_year)
            Km_rate = interval.interval(DistRate.objects.all(), car_km)
            bonus = Bonus.objects.get(passager=car_passager).bonus
            total = vh_rate + en_rate + y_rate + Km_rate
            rate = interval.interval(TauxEmprunt.objects.all(), total) + bonus

            context = {"type": vh_rate, "year": y_rate, "energie": en_rate,
                       "bonus": bonus, "dist": Km_rate, "total": total, "rate": rate}
            return render(request, "emprunt.html", context=context)
        except:
            return render(request, "Error.html")

    context = {"type": car_type, "year": car_year, "energie": car_energie,
               "passager": car_passager,
               "dist": car_km}
    return render(request, "Error.html", context=context)
