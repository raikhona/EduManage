from django.db import models
from django.contrib.auth.models import User

classes = [(1, '1 Grade'), (2, '2 Grade'), (3, '3 Grade'), (4, '4 Grade'), (5, '5 Grade'), (6, '6 Grade'), (7, '7 Grade'), (8, '8 Grade'), (9, '9 Grade'), (10, '10 Grade')]


class TeacherExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joindate = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name


class StudentExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=40, null=True)
    status = models.BooleanField(default=False)
    owned_teachers = models.ManyToManyField(TeacherExtra)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Notice(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=20,null=True,default='school')
    message = models.CharField(max_length=500)


class Mark(models.Model):
    student = models.ForeignKey(StudentExtra, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherExtra, on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateField(auto_now=True)
