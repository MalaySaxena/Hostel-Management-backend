from .models import HostelAllocation, Room, Student

cseStudents = Student.objects.filter(student_course="cse").order_by(-student_gpa)
ecStudent = Student.objects.filter(student_course="ec").order_by(student_gpa)
mechStudents = Student.objects.filter(student_course="ec").order_by(student_gpa)
eeStudents = Student.objects.filter(student_course="ee").order_by(student_gpa)
civilStudents = Student.objects.filter(student_course="civil").order_by(student_gpa)



def checkAvaibility(request):
