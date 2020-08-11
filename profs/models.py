from django.db import models

# Create your models here.


class Prof(models.Model):
    name = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    aor = models.TextField()
    phone = models.BigIntegerField()
    web = models.CharField(max_length=512)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name
