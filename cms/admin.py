from multiprocessing.reduction import AbstractReducer
from django.contrib import admin
from .models import CollegeModel, CourseModel, Navbar, AbroadModel

# Register your models here.

admin.site.register(CollegeModel)
admin.site.register(CourseModel)
admin.site.register(Navbar)
admin.site.register(AbroadModel)