from django.db import models


class Tag(models.Model):
  name = models.CharField(max_length=50, null=False)
  slug = models.CharField(max_length=50, null=False)

  def __str__(self):
    return self.slug


class Hack(models.Model):
  content = models.TextField(null=False)
  star = models.IntegerField(default=0, null=False)
  tag = models.ManyToManyField(Tag)

  def __str__(self):
    return self.content
