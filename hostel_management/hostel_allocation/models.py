from django.db import models

# Create your models here.
class HostelAllocation(models.Model):
    hostel_name = models.CharField(max_length=2)
    hostel_gender = models.CharField(max_length=7)
    hostel_course = models.CharField(max_length=3)
    hostel_no_of_floor = models.IntegerField()
    hostel_no_of_room = models.IntegerField()
    rooms_type = models.CharField(max_length=1, default=None)
    hostel_no_of_room_available = models.IntegerField()
    hostel_warden = models.CharField(max_length=20)

    def __str__(self):
        return self.hostel_name


class Room(models.Model):
    room_no = models.IntegerField()
    room_luxury = models.CharField(max_length=10, default=None)
    is_room_vacant = models.IntegerField(default=True)
    hostel = models.ForeignKey(HostelAllocation,on_delete=models.CASCADE)

    def str(self):
        return self.room_no

class Student(models.Model):
    enrollment_no = models.CharField(max_length=10, unique=True, null=True)
    student_name = models.CharField(max_length=200, null=True)
    student_mobile = models.CharField(max_length=11)
    student_gender = models.CharField(max_length=1, default=None, null=True)
    student_gpa = models.FloatField()
    student_course = models.CharField(max_length=8, default=None)
    student_year = models.CharField(max_length=1,default=None,null=True)
    student_room_no = models.ForeignKey(Room, on_delete=models.CASCADE, default=0)
    physical_problem = models.BooleanField(default=False)
    room_allotted = models.BooleanField(default=False)

    def str(self):
        return self.student_name