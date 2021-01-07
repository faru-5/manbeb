from django.db import models
from django.utils import timezone

class Book(models.Model):
    # branch choice
    # need some improvements on branchs
    BRANCHS = (
        ('Natural Science', 'Natural Science'),
        ('Social Science', 'Social Science'),
        ('other', 'other')
    )
    SUBJECTS = (
        ('biology','biology'),
        ('chemistry', 'chemistry'),
        ('business','business'),
        ('english','english'),
        ('civic', 'civic'),
    )
    title = models.CharField(max_length=200, blank=True)
    book = models.FileField(upload_to='books', blank=True)
    cover = models.ImageField(blank=True, upload_to="cover")
    grade = models.CharField(max_length=3)
    branch = models.CharField(max_length=30, choices=BRANCHS)
    subject = models.CharField(max_length=30, choices=SUBJECTS)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

