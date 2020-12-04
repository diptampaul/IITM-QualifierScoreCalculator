from django.db import models

# Create your models here.

class FileUpload(models.Model):
    file_uploaded = models.FileField()
    public_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, null=True, default='127.0.0.1')
    name = models.CharField(max_length=200)
    paper_code = models.IntegerField()
    total_marks = models.FloatField()
    engcount = models.FloatField()
    ctcount = models.FloatField()
    statcount = models.FloatField()
    mathcount = models.FloatField()
