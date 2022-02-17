from django.http import HttpResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from student.models import StudentData


def index(request):
    # context={
    #     "user":"小六"
    # }
    # return render(requests,"student/index.html",context)
    student_info=StudentData.objects.all()
    return render(request,'student/index.html',{'student_info':student_info})

# 增加手机信息
@csrf_exempt
def add(request):
    if request.method == "POST":
        # 获取用户浏览器中输入的数据
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        student_sex = request.POST.get("student_sex")
        student_addriess = request.POST.get("student_addriess")
        student_class = request.POST.get("student_class")
        # id = request.POST.get("id")

        # 将浏览器中的数据赋值至数据库
        # StudentData.objects.create(student_id=student_id, student_name=student_name, student_sex=student_sex,
        #                          student_addriess=student_addriess, phone_color=student_class, id=id)
        StudentData.objects.create(student_id=student_id, student_name=student_name, student_sex=student_sex,
                                   student_addriess=student_addriess, student_class=student_class)

        return redirect('/student/index/')
    else:
        return render(request, 'student/add.html')