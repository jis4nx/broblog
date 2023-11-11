from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime
from django.urls import reverse


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    content_image = models.ImageField(
        blank=True, default="../static/images/panji-adhi-YLtJv5rCFFM-unsplash.jpg"
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        dt_string = datetime.now().strftime("%d-%m-%Y-%H-%M")
        tslug = f"{self.title}-{self.author}-{dt_string}"
        self.slug = slugify(tslug)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def total_comments(self):
        return Comment.objects.filter(blog=self).count()

    def __str__(self):
        return self.comment


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False, blank=True)
