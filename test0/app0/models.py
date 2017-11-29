from django.db import models

# Create your models here.


class Ids(models.Model):
    objects = models.Manager()
    id = models.IntegerField(primary_key=True, default=0)


class UserMetaInfo(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.username


class PaperMetaInfo(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=32)
    summary = models.CharField(max_length=400)
    filepath = models.FileField(upload_to='./pdf')

    def __str__(self):

        return self.title


class PaperUploadInfo(models.Model):
    objects = models.Manager()
    paper_id = models.IntegerField()
    uploader_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'paper ' + self.paper_id + ' and uploader ' + self.uploader_id + " at date " + self.date



