from .models import HostelAllocation,Room,Student

all_student = Student.objects.all()

def checkAC(wing,stud,type,ac):

    no_of_room = wing.hostel_no_of_room/wing.hostel_no_of_floor

    if type == "S" :
        acFloor = ((wing.hostel_no_of_floor - 1) * 0.25)  # convert to int
        subtract = wing.hostel_no_of_floor - acFloor
        rooms = Room.objects.filter(hostel=wing, is_room_vacant=0)
        if ac == "AC" :
            if stud.physical_problem == True :


                for r in rooms :
                    if r.room_no-101 < no_of_room/2:
                        stud.student_room_no = r.room_no
                        stud.room_allotted = True
                        r.is_room_vacant = 1
            else :
                low = subtract*100+1;
                high = wing.hostel_no_of_floor*100 + no_of_room
                for r in rooms :
                    if r.room_no > low and r. room_no < high:
                        stud.student_room_no = r.room_no
                        stud.room_allotted = True
                        r.is_room_vacant = False

        else :
            if stud.physical_problem == True :
                for r in rooms :
                    if r.room_no-100 > no_of_room/2 and r.room_no-100<101+no_of_room:
                        stud.student_room_no = r.room_no
                        stud.room_allotted = True
                        r.is_room_vacant = 1
            else :
                low = 2 * 100 + 1;
                high = subtract*100 + no_of_room
                for r in rooms:
                    if r.room_no > low and r.room_no < high:
                        stud.student_room_no = r.room_no
                        stud.room_allotted = True
                        r.is_room_vacant = 1


    else :
         stu = Student.objects.filter()
         max_gpa = max(stu.student_gpa)
         percentile_list = []
         for s in stu:
           percentile_list.append(s.student_gpa/max_gpa * 100)

         no_of_room = wing.hostel_no_of_room / wing.hostel_no_of_floor

         acFloor = ((wing.hostel_no_of_floor - 1) * 0.25)  # convert to int
         subtract = wing.hostel_no_of_floor - acFloor
         rooms = Room.objects.filter(hostel=wing, is_room_vacant=(0 or 1))
         if rooms.is_room_vacant==0:
             if ac == "AC":
                 if stud.physical_problem == True:
                     for r in rooms:
                         if r.room_no - 101 < no_of_room / 2:
                             stud.student_room_no = r.room_no
                             stud.room_allotted = True
                             r.is_room_vacant = 1
                 else:
                     low = subtract * 100 + 1;
                     high = wing.hostel_no_of_floor * 100 + no_of_room
                     for r in rooms:
                         if r.room_no > low and r.room_no < high:
                             stud.student_room_no = r.room_no
                             stud.room_allotted = True
                             r.is_room_vacant = False

             else:
                 if stud.physical_problem == True:
                     for r in rooms:
                         if r.room_no - 100 > no_of_room / 2 and r.room_no - 100 < 101 + no_of_room:
                             stud.student_room_no = r.room_no
                             stud.room_allotted = True
                             r.is_room_vacant = 1
                 else:
                     low = 2 * 100 + 1;
                     high = subtract * 100 + no_of_room
                     for r in rooms:
                         if r.room_no > low and r.room_no < high:
                             stud.student_room_no = r.room_no
                             stud.room_allotted = True
                             r.is_room_vacant = 1

         elif rooms.is_room_vacant==1:
             if ac == "AC":
                 if stud.physical_problem == True:
                     for r in rooms:
                         if r.room_no - 101 < no_of_room / 2:
                             stud.student_room_no = r.room_no
                             stud.room_allotted = True
                             r.is_room_vacant = 1
                 else:
                     low = subtract * 100 + 1;
                     high = wing.hostel_no_of_floor * 100 + no_of_room
                     for r in rooms:
                         if r.room_no > low and r.room_no < high:
                             stud.student_room_no = r.room_no
                             stud.room_allotted = True
                             r.is_room_vacant = False

             else:
                 if stud.physical_problem == True:
                     for r in rooms:
                         if r.room_no - 100 > no_of_room / 2 and r.room_no - 100 < 101 + no_of_room:
                             stud.student_room_no = r.room_no
                             stud.room_allotted = True
                             r.is_room_vacant = 1
                 else:
                     low = 2 * 100 + 1;
                     high = subtract * 100 + no_of_room
                     for r in rooms:
                         if r.room_no > low and r.room_no < high:
                             stud.student_room_no = r.room_no
                             stud.room_allotted = True
                             r.is_room_vacant = 1


def checkAvaibility(request, enroll, roomType, luxury):
    student = Student.objects.filter(enrollment_no=enroll)
    branch = student.student_course
    gender = student.student_gender
    hostel_matched = HostelAllocation.objects.filter(hostel_course=branch, hostel_gender=gender,rooms_type=roomType)

    checkAC(hostel_matched,student,roomType,luxury)
