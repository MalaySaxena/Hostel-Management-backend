from .models import HostelAllocation,Room,Student

all_student = Student.objects.all()
def checkAvaibility(request, enroll, roomType, luxury):
    student = Student.objects.filter(enrollment_no=enroll)
    branch = student.student_course
    gender = student.student_gender
    hostel_matched = HostelAllocation.objects.filter(hostel_course=branch, hostel_gender=gender)

    