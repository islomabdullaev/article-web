from django.db import models

class TimeStampedModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
         abstract = True


class News(TimeStampedModel):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to="news")
    is_top = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "News"
        ordering = ["-created_at"]


class Newsletter(TimeStampedModel):
    email = models.CharField(max_length=128)


    def __str__(self):
        return self.email
