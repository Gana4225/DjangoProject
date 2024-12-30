from django.db import models

class branch(models.Model):
    branch = models.CharField(max_length=10)

    def __str__(self):
        return self.branch
class reg(models.Model):
    reg = models.CharField(max_length=10)
    def __str__(self):
        return self.reg

class student(models.Model):
    name = models.CharField(max_length=250)
    rn = models.CharField(max_length=250)
    marks = models.IntegerField(default=0)
    phone = models.CharField(max_length=15)
    branch = models.ForeignKey(branch,on_delete=models.CASCADE)
    reg = models.ForeignKey(reg,on_delete=models.CASCADE)
    pas = models.BooleanField(default=False)


    def __str__(self):
        return self.name



class Login(models.Model):
    username = models.CharField(max_length=150)
    passw = models.CharField(max_length=30)

    def __str__(self):
        return self.username

