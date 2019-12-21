from django.contrib import admin
from .models import HostelAllocation, Room, Student

# Register your models here.
admin.site.register(HostelAllocation)
admin.site.register(Room)
admin.site.register(Student)