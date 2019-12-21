from django.db import models

# Create your models here.
class HostelAllocation(models.Model):
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    course_choices = ['CSE', 'ECE', 'MECH', 'CIVIL', 'EE']
    type = ['S', 'D']  # S-single occupancy D-double occupancy
    hostel_name = models.CharField(max_length=2)
    hostel_gender = models.CharField(max_length=7,choices=gender_choices)
    hostel_course = models.CharField(max_length=3,choices=course_choices)
    hostel_no_of_floor = models.IntegerField()
    hostel_no_of_room = models.IntegerField()
    rooms_type = models.CharField(choices=type, max_length=1, default=None)
    hostel_no_of_room_available = models.IntegerField()
    hostel_warden = models.CharField(max_length=20)

    def __str__(self):
        return self.hostel_name


class Room(models.Model):
    type = ['S', 'D'] #S-single occupancy D-double occupancy
    luxury = ['AC','Non AC']

    room_no = models.IntegerField()
    room_type = models.CharField(choices=type, max_length=1, default=None)
    room_luxury = models.CharField(choices=luxury, max_length=10, default=None)
    is_room_vacant = models.BooleanField(default=True)
    hostel = models.ForeignKey(HostelAllocation,on_delete=models.CASCADE)

    def str(self):
        return self.room_no

class Student(models.Model):
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    year_choices = ['UG1', 'UG2', 'UG3', 'UG4', 'PG1', 'PG1']
    course_choices = ['CSE','ECE','MECH','CIVIL','EE']
    student_name = models.CharField(max_length=200, null=True)
    student_mobile = models.CharField(max_length=11)
    enrollment_no = models.CharField(max_length=10, unique=True, null=True)
    student_gpa = models.FloatField()
    student_gender = models.CharField(choices=gender_choices,max_length=1,default=None,null=True)
    student_year = models.CharField(choices=year_choices,max_length=1,default=None,null=True)
    student_course = models.CharField(choices=course_choices,max_length=8,default=None)
    physical_problem = models.BooleanField(default=False)
    student_room_no = models.ForeignKey(Room,on_delete=models.CASCADE,default=0)
    room_allotted = models.BooleanField(default=False)

    def str(self):
        return self.student_name