from django.db import models

# Create your models here.
class StudentData(models.Model):
    student_name=models.CharField(max_length=20)
    student_sex=models.CharField(max_length=20)
    student_id=models.CharField(max_length=20,null=True)
    student_addriess=models.CharField(max_length=20)
    student_class=models.CharField(max_length=20)
    # id=models.CharField(max_length=20)
