from django.db import models


class Blog_model(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.FileField(upload_to='image/')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) > 43:
            return self.body[:43] + ' ...'
        else:
            return self.body