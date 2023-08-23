from django.db import models

# Create your models here.

class Dept(models.Model):
    DEPTNO=models.IntegerField(max_length=20,primary_key=True)
    DNAME=models.CharField(max_length=50,null=False,unique=True)
    LOCATION=models.CharField(max_length=50,null=False)
    def __str__(self):
        return self.DNAME


class Emp(models.Model):
    EMPNO=models.IntegerField(max_length=20,primary_key=True)
    ENAME=models.CharField(max_length=50,null=False)
    JOB=models.CharField(max_length=25,null=False)
    HIREDATE=models.DateField(null=False)
    SALARY=models.IntegerField(null=False)
    COMM=models.IntegerField(null=True,blank=True,default=None)
    DEPTNO=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ENAME
