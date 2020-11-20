from django.forms import ModelForm
from student.models import Student

class studentform(ModelForm):
      class Meta:
          model=Student
          fields='__all__'
