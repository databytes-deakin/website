from django.db import models as md

class Project (md.Model):
    def __str__(self):
        return self.ProjectName
    ProjectID = md.BigAutoField(primary_key=True)
    ProjectName = md.CharField(max_length=64)
    ProjectDescription = md.TextField(max_length=2048)
    ProjectLeader = md.CharField(max_length=64)
    LeaderEmail = md.EmailField(max_length=64)

class Job (md.Model):
    def __str__(self):
        return self.JobName
    JobID = md.AutoField(primary_key=True)
    JobName = md.CharField(max_length=64)
    JobDescription = md.TextField(max_length=1024)
    JobCategory = md.CharField(max_length=64, default='')
    PubDate = md.DateTimeField()
    ProjectID = md.ForeignKey(Project, on_delete=md.CASCADE, blank=True, null=True)

class Testimony (md.Model):
    def __str__(self):
        return self.Name
    TestimonyID = md.AutoField(primary_key=True)
    Name = md.CharField(max_length=64)
    PersonTitle = md.CharField(max_length=64)
    Quote = md.TextField(max_length=512)