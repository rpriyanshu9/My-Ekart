from django.db import models


# Create your models here.
class Blog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=5000, default="")
    head0 = models.CharField(max_length=5000, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=5000, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=5000, default="")
    chead2 = models.CharField(max_length=5000, default="")
    pub_date = models.CharField(max_length=5000, default="")
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title
