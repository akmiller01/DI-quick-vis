from django.db import models
from redactor.fields import RedactorField

class Data(models.Model):
    content = RedactorField(verbose_name=u'Text')
    file_field = models.FileField()
