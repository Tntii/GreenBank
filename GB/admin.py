from django.contrib import admin

# Register your models here.
from GB.models import *

db = (TypeRate, EnergieRate, YearRate, DistRate, Bonus, TauxEmprunt)

for table in db:
    admin.site.register(table)