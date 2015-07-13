from django.db import models
from redactor.fields import RedactorField
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.text import slugify
import datetime
from os.path import basename, splitext

class Dataset(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True,max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    file_field = models.FileField(upload_to=settings.MEDIA_ROOT+'/%Y/%m/%d')
    
    class Meta:
        ordering = ['-created']
    
    def __unicode__(self):
        return u'%s' % self.name
    
    def get_absolute_url(self):
        return reverse('core.views.data',args=[self.slug])
    
    def save(self, *args, **kwargs):
        super(Dataset, self).save(*args, **kwargs)
        date = datetime.date.today()
        if self.name is None or self.name == "":
            self.name = splitext(basename(self.file_field.name))[0]
            self.slug = '%s-%i%i%i' % (
                 slugify(self.name), date.year, date.month, date.day
            )
        elif self.slug is None or self.slug == "":
            self.slug = '%s-%i%i%i%i' % (
                slugify(self.name), date.year, date.month, date.day, self.id
            )
        super(Dataset, self).save(*args, **kwargs)
