from django.urls import path
from . import views
#from student.views import index,insert_student,update_student,delete_student

urlpatterns=[
     path('student_insert/',views.insert_student,name='student_insert'),
     path('',views.index,name='student_list'),
     path('student_update/<int:id>',views.update_student,name='student_update'),
     path('<int:id>/',views.delete_student,name='student_delete'),
    ]
