from django.db import models as md

class Project (md.Model):
    def __str__(self):
        return 'Project: ' + self.ProjectName
    ProjectID = md.BigAutoField(primary_key=True)
    ProjectName = md.CharField(max_length=64)
    ProjectDesc = md.TextField(max_length=512)
    ProjectLeader = md.CharField(max_length=64)
    LeaderEmail = md.EmailField(max_length=64)

class Job (md.Model):
    def __str__(self):
        return 'Job: ' + self.JobName
    JobID = md.AutoField(primary_key=True)
    JobName = md.CharField(max_length=64)
    JobDesc = md.TextField(max_length=512)
    PubDate = md.DateTimeField()
    ProjectID = md.ForeignKey(Project, on_delete=md.CASCADE)


