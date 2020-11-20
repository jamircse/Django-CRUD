from django.shortcuts import render,redirect
from student.models import Student
from student.forms import studentform
# Create your views here.
def index(request):
    # read operation
    context={'student':Student.objects.all()}
    return render(request,'student/student_list.html',context)

def insert_student(request):
    form=studentform()
    # insert operation
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        
    context={'form':form}
    return render(request,'student/student_form.html',context)


def update_student(request,id):
    form=studentform()
    st=Student.objects.get(pk=id)
    if request.method=="GET":
        form=studentform(instance=st)
    else:
        #update operation
        form=studentform(request.POST,instance=st)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    context={'form':form}
    return render(request,'student/student_form.html',context)

def delete_student(request,id):
    st_id=Student.objects.get(pk=id)
    st_id.delete()
    return redirect('student_list')
          
        
