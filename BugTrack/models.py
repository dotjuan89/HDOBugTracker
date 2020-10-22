from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    role = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=True)
    

class Ticket(models.Model):
    title = models.CharField(max_length=50, null=True)
    category = models.IntegerField(null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)



class Status(models.Model):
    priority_color = models.IntegerField(null=False)
    severity_color = models.IntegerField(null=False)


class Statusticket(models.Model):
     status = models.ForeignKey(to=Status, on_delete=models.CASCADE)
     ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)


class Comments(models.Model):
    content = models.CharField(max_length=500, null=True)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)



class Image(models.Model):
   image_path = models.CharField(max_length=255, null=True)
   comments = models.ForeignKey(to=Comments, on_delete=models.CASCADE)
    
   
