from django.shortcuts import render
from .models import HostelAllocation,Room,Student

def checkAC(request,wing,stud,type,ac):

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
                        res = {'name': stud, 'wing': wing, 'room': r.room_no}
                        return render(request, 'index.html', context=res)

            else :
                low = subtract*100+1;
                high = wing.hostel_no_of_floor*100 + no_of_room
                for r in rooms :
                    if r.room_no > low and r. room_no < high:
                        stud.student_room_no = r.room_no
                        stud.room_allotted = True
                        r.is_room_vacant = 1
                        res = {'name': stud, 'wing': wing, 'room': r.room_no}
                        return render(request, 'index.html', context=res)

        else :
            if stud.physical_problem == True :
                for r in rooms :
                    if r.room_no-100 > no_of_room/2 and r.room_no-100<101+no_of_room:
                        stud.student_room_no = r.room_no
                        stud.room_allotted = True
                        r.is_room_vacant = 1
                        res = {'name': stud, 'wing': wing, 'room': r.room_no}
                        return render(request, 'index.html', context=res)

            else :
                low = 2 * 100 + 1;
                high = subtract*100 + no_of_room
                for r in rooms:
                    if r.room_no > low and r.room_no < high:
                        stud.student_room_no = r.room_no
                        stud.room_allotted = True
                        r.is_room_vacant = 1
                        res = {'name': stud, 'wing': wing, 'room': r.room_no}
                        return render(request, 'index.html', context=res)

    else :
        stu = Student.objects.filter(student_branch=stud.branch, student_gender = stud.gender)
        max_gpa = max(stu.student_gpa)
        percentile_list = {}
        for s in stu:
            percentile_list[s.enrollment_no]=(s.student_gpa/max_gpa * 100)

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
                            res = {'name': stud, 'wing': wing, 'room': r.room_no}
                            return render(request, 'index.html', context=res)

                else:
                    low = subtract * 100 + 1;
                    high = wing.hostel_no_of_floor * 100 + no_of_room
                    for r in rooms:
                        if r.room_no > low and r.room_no < high:
                            stud.student_room_no = r.room_no
                            stud.room_allotted = True
                            r.is_room_vacant = 1
                            res = {'name': stud, 'wing': wing, 'room': r.room_no}
                            return render(request, 'index.html', context=res)

            else:
                if stud.physical_problem == True:
                    for r in rooms:
                        if r.room_no - 100 > no_of_room / 2 and r.room_no - 100 < 101 + no_of_room:
                            stud.student_room_no = r.room_no
                            stud.room_allotted = True
                            r.is_room_vacant = 1
                            res = {'name': stud, 'wing': wing, 'room': r.room_no}
                            return render(request, 'index.html', context=res)
                else:
                    low = 2 * 100 + 1;
                    high = subtract * 100 + no_of_room
                    for r in rooms:
                        if r.room_no > low and r.room_no < high:
                            stud.student_room_no = r.room_no
                            stud.room_allotted = True
                            r.is_room_vacant = 1
                            res = {'name': stud, 'wing': wing, 'room': r.room_no}
                            return render(request, 'index.html', context=res)

        elif rooms.is_room_vacant==1:

            if ac == "AC":
                flag=0
                if stud.physical_problem == True:
                    for r in rooms:
                        s = stu.filter(student_room_no=r.room_no)
                        if r.room_no - 101 < no_of_room / 2:
                            if percentile_list[s.enrollment_no] - percentile_list[stud.enrollment_no] < 30:
                                flag = 0
                                stud.room_allotted = True
                                r.is_room_vacant = 2
                                res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                return render(request, 'index.html', context=res)
                            else:
                                flag=1

                    if flag == 1:
                        for r in rooms:
                            s = stu.filter(student_room_no=r.room_no)
                            if r.room_no - 101 < no_of_room / 2:
                                if percentile_list[s.enrollment_no] - percentile_list[stud.enrollment_no] < 40:
                                    flag = 0
                                    stud.room_allotted = True
                                    r.is_room_vacant = 2
                                    res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                    return render(request, 'index.html', context=res)
                                else:
                                    flag = 2
                    if flag == 2:
                        for r in (-rooms):
                            s = stu.filter(student_room_no=r.room_no)
                            if r.room_no - 101 < no_of_room / 2:
                                flag = 0
                                stud.room_allotted = True
                                r.is_room_vacant = 2
                                res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                return render(request, 'index.html', context=res)

                else:
                    flag=0
                    low = subtract * 100 + 1;
                    high = wing.hostel_no_of_floor * 100 + no_of_room
                    for r in rooms:
                        if r.room_no > low and r.room_no < high:
                            s = stu.filter(student_room_no=r.room_no)
                            if r.room_no - 101 < no_of_room / 2:
                                if percentile_list[s.enrollment_no] - percentile_list[stud.enrollment_no] < 30:
                                    flag = 0
                                    stud.room_allotted = True
                                    r.is_room_vacant = 2
                                    res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                    return render(request, 'index.html', context=res)
                                else:
                                    flag = 1

                    if flag == 1:
                        for r in rooms:
                            s = stu.filter(student_room_no=r.room_no)
                            if r.room_no - 101 < no_of_room / 2:
                                if percentile_list[s.enrollment_no] - percentile_list[stud.enrollment_no] < 40:
                                    flag = 0
                                    stud.room_allotted = True
                                    r.is_room_vacant = 2
                                    res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                    return render(request, 'index.html', context=res)
                                else:
                                    flag = 2
                    if flag == 2:
                        for r in (-rooms):
                            s = stu.filter(student_room_no=r.room_no)
                            if r.room_no - 101 < no_of_room / 2:
                                flag = 0
                                stud.room_allotted = True
                                r.is_room_vacant = 2
                                res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                return render(request, 'index.html', context=res)

            else:
                if stud.physical_problem == True:
                    flag = 0
                    if stud.physical_problem == True:
                        for r in rooms:
                            s = stu.filter(student_room_no=r.room_no)
                            if r.room_no - 101 < no_of_room / 2:
                                if percentile_list[s.enrollment_no] - percentile_list[stud.enrollment_no] < 30:
                                    flag = 0
                                    stud.room_allotted = True
                                    r.is_room_vacant = 2
                                    res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                    return render(request, 'index.html', context=res)
                                else:
                                    flag = 1

                        if flag == 1:
                            for r in rooms:
                                s = stu.filter(student_room_no=r.room_no)
                                if r.room_no - 101 < no_of_room / 2:
                                    if percentile_list[s.enrollment_no] - percentile_list[stud.enrollment_no] < 40:
                                        flag = 0
                                        stud.room_allotted = True
                                        r.is_room_vacant = 2
                                        res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                        return render(request, 'index.html', context=res)
                                    else:
                                        flag = 2
                        if flag == 2:
                            for r in (-rooms):
                                s = stu.filter(student_room_no=r.room_no)
                                if r.room_no - 101 < no_of_room / 2:
                                    flag = 0
                                    stud.room_allotted = True
                                    r.is_room_vacant = 2
                                    res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                    return render(request, 'index.html', context=res)

                else:
                    flag=0
                    low = 2 * 100 + 1;
                    high = subtract * 100 + no_of_room
                    for r in rooms:
                        if r.room_no > low and r.room_no < high:
                            s = stu.filter(student_room_no=r.room_no)
                            if r.room_no - 101 < no_of_room / 2:
                                if percentile_list[s.enrollment_no] - percentile_list[stud.enrollment_no] < 30:
                                    flag = 0
                                    stud.room_allotted = True
                                    r.is_room_vacant = 2
                                    res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                    return render(request, 'index.html', context=res)
                                else:
                                    flag = 1

                    if flag == 1:
                        for r in rooms:
                            s = stu.filter(student_room_no=r.room_no)
                            if r.room_no - 101 < no_of_room / 2:
                                if percentile_list[s.enrollment_no] - percentile_list[stud.enrollment_no] < 40:
                                    flag = 0
                                    stud.room_allotted = True
                                    r.is_room_vacant = 2
                                    res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                    return render(request, 'index.html', context=res)
                                else:
                                    flag = 2
                    if flag == 2:
                        for r in (-rooms):
                            s = stu.filter(student_room_no=r.room_no)
                            if r.room_no - 101 < no_of_room / 2:
                                flag = 0
                                stud.room_allotted = True
                                r.is_room_vacant = 2
                                res = {'name': stud, 'wing': wing, 'room': r.room_no}
                                return render(request, 'index.html', context=res)

def checkAvaibility(request, enroll, roomType, luxury):
    student = Student.objects.filter(enrollment_no=enroll)
    branch = student.student_course
    gender = student.student_gender
    hostel_matched = HostelAllocation.objects.filter(hostel_course=branch, hostel_gender=gender,rooms_type=roomType)

    checkAC(request,hostel_matched,student,roomType,luxury)