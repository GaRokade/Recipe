from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Create your models here.
class Receipe(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    receipe_name=models.CharField( max_length=100)
    receipe_descri=models.TextField()
    receipe_image=models.ImageField(upload_to="receipe/")
    
    
class Department(models.Model):
    department=models.CharField( max_length=100)
    
    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering=['department']
    

class StudentID(models.Model):
    student_id=models.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return self.student_id

class Subject(models.Model):
    subject_name=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.subject_name
    
    
 
class Student(models.Model):
    department=models.ForeignKey("Department",related_name="depart", on_delete=models.CASCADE)
    student_id=models.OneToOneField("StudentID",related_name="studentid", on_delete=models.CASCADE)
    student_name=models.CharField( max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()
    


class SubjectMarks(models.Model):
    student=models.ForeignKey("Student",related_name="student", on_delete=models.CASCADE)
    subject=models.ForeignKey("Subject",related_name="subject", on_delete=models.CASCADE)
    marks=models.IntegerField(default=0)
    
    
    class Meta:
        unique_together = ('student', 'subject')
    
    
    def __str__(self) -> str:
        return f"{self.student.student_name} {self.subject.subject_name}"
    
