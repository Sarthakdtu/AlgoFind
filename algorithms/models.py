from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=200)


class Code(models.Model):
    title = models.CharField(max_length=200)
    code_link = models.URLField(null=False, unique=True)

class CodeTag(models.Model):
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
