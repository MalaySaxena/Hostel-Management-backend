from django.db import models

# Create your models here.
class HostelAllocation(models.Model):
    hostel_name = models.CharField(max_length=2)
    hostel_gender = models.CharField(max_length=7)
    hostel_course = models.CharField(max_length=3)
    hostel_no_of_floor = models.IntegerField()
    hostel_no_of_room = models.IntegerField()
    hostel_no_of_room_available = models.IntegerField()
    hostel_warden = models.CharField(max_length=20)

    def __str__(self):
        return self.hostel_name


class Room(models.Model):
    type = [('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('P', 'Reserved for Research Scholars'),('B', 'Both Single and Double Occupancy')]
    luxury = ['AC','Non AC']

    room_no = models.CharField(max_length=5)
    room_type = models.CharField(choices=type, max_length=1, default=None)
    room_luxury = models.CharField(choices=luxury, max_length=10, default=None)
    is_room_vacant = models.BooleanField(default=False)
    hostel = models.ForeignKey(HostelAllocation,on_delete=models.CASCADE)

    def str(self):
        return self.room_no

class Student(models.Model):
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    year_choices = ['UG1', 'UG2', 'UG3', 'UG4', 'PG1', 'PG1']
    course_choices = ['CSE','IT','ECE','MECH','CIVIL','EE']
    student_name = models.CharField(max_length=200, null=True)
    student_mobile = models.CharField(max_length=11)
    enrollment_no = models.CharField(max_length=10, unique=True, null=True)
    student_gender = models.CharField(choices=gender_choices,max_length=1,default=None,null=True)
    student_year = models.CharField(choices=year_choices,max_length=1,default=None,null=True)
    student_course = models.CharField(choices=course_choices,max_length=8,default=None)
    student_room_no = models.ForeignKey(Room,on_delete=models.CASCADE)
    room_allotted = models.BooleanField(default=False)

    def str(self):
        return self.student_name