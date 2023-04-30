from django.db import models

class Label(models.Model):
id = models.AutoField(primary_key=True)
name = models.CharField(unique=True, max_length=120)

class Image(models.Model):
id = models.AutoField(primary_key=True)
label = models.ForeignKey(Label, on_delete=models.SET_NULL, related_name="rois", null=True)
file = models.FileField(upload_to="hist_images", max_length=255
