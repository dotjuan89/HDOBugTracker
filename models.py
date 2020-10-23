from django.db import models

# Create your models here.

class User(models.Model):
    userID = models.IntegerField(null=False, primary_key=True)
    userName = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, null=True)

    def __str__(self):
        return self.userid

class Skill(models.Model):
    skillID = models.IntegerField(null=False, primary_key=True)
    skillName = models.CharField(max_length=30, null=False)
    proficiency = models.IntegerField(null=False)

    def __str__(self):
        return self.skillName


class UserSkill(models.Model):
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)
    skillID = models.ForeignKey(to=Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.skillID

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


