from django.shortcuts import render
from .models import HostelAllocation,Room,Student
'''
# Create your views here.
all_student = Student.objects.all()
def checkAvaibility(request, enroll, roomType, luxury):
    student = Student.objects.filter(enrollment_no=enroll)
    branch = student.student_course
    gender = student.student_gender
    hostell = HostelAllocation.objects.filter(hostel_course=branch, hostel_gender=gender)

    #checkRooms(roomtype,luxury,student,hostell)
    if (roomType == "S"):
        room_of_s = hostell.objetcs.filter(roomsType='S')
        no_of_room = room_of_s.no_of_room / room_of_s.no_of_floor
        if(luxury == "AC"):


            if student.physical_problem == True:
                rooms = Room.objects.order_by(room_no)
                for r in rooms:
                    if(r.room_no<no_of_room/2):

                        if(r.is_room_vacant):
                            student.student_room_no=r.room_no+101
                            student.room_allotted=True
                            r.is_room_vacant=False
                        else:
                            #need to complete
                            pass
                    else:
                        if (r.is_room_vacant):
                            student.student_room_no = r.room_no + 101
                            student.room_allotted = True
                            r.is_room_vacant = False
                        else:
                            # need to complete
                            pass
            else:
                rooms = Room.objects.order_by(-room_no)
                var = int((room_of_s.no_of_floor-1)*(0.25))
                for i in range(room_of_s.no_of_floor,room_of_s.no_of_floor-var):
                    if (r.is_room_vacant):
                        student.student_room_no = r.room_no + 100*i+1
                        student.room_allotted = True
                        r.is_room_vacant = False
                    else:
                        # need to complete
                        pass

    if (roomType == "D"):
        room_of_d = hostell.objetcs.filter(roomsType='D')
        no_of_room = room_of_d.no_of_room / room_of_d.no_of_floor
        if (luxury == "AC"):

            if student.physical_problem == True:
                rooms = Room.objects.order_by(room_no)
                for r in rooms:
                    if (r.room_no < no_of_room / 2):
                        if (r.is_room_vacant):
                            count = 0
                            temp_student = all_student.objects.filter(student_room_no=r.room_no)
                            for i in temp_student:
                                count = count+1

                            if count<2:
                                student.student_room_no = r.room_no + 101
                                student.room_allotted = True
                                r.is_room_vacant = False
                            else:
                                #
                                pass

                        else:
                            # need to complete
                            pass
                    else:
                        if (r.is_room_vacant):
                            count = 0
                            temp_student = all_student.objects.filter(student_room_no=r.room_no)
                            for i in temp_student:
                                count = count + 1

                            if count < 2:
                                student.student_room_no = r.room_no + 101
                                student.room_allotted = True
                                r.is_room_vacant = False
                            else:
                                #
                                pass

                        else:
                            # need to complete
                            pass
            else:
                rooms = Room.objects.order_by(-room_no)
                var = int((room_of_s.no_of_floor - 1) * (0.25))
                for i in range(room_of_s.no_of_floor, room_of_s.no_of_floor - var):
                    if (r.is_room_vacant):
                        student.student_room_no = r.room_no + 100*i+1
                        student.room_allotted = True
                        r.is_room_vacant = False
                    else:
                        # need to complete
                        pass

'''

    '''
    if student.physical_problem == True:
        student.student_room_no = 0
        student.student_room_no += 100
    '''