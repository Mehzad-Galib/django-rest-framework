from django.db import models


# Create your models here.
class Studentdata(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    roll = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(
        Studentdata, on_delete=models.CASCADE, related_name='course')
    name = models.CharField(max_length=20)
    credit = models.IntegerField()

    def __str__(self) -> str:
        return self.name
