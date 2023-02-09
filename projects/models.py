import uuid
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField('Tag')
    review_number = models.IntegerField(default=0)
    review_total = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)


    def __str__(self):
        return self.title

class Review(models.Model):
    VOTES = (
        ('up','Up Vote'),
        ('down','Down Vote'),
    )

    # author
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    content = models.CharField(max_length=300)
    vote = models.CharField(max_length=20,choices=VOTES,null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)

    def __str__(self) -> str:
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)

    def __str__(self) -> str:
        return self.name