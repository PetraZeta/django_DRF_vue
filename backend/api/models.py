from django.db import models
    
class Work(models.Model):
    work_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    salary = models.IntegerField()
    
class Worker(models.Model):
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    name_first = models.CharField(max_length=100)
    name_last = models.CharField(max_length=100)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.username