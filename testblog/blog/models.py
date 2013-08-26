from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('P', u"Post"),
        ('T', u"Tutorial"),
        ('R', u"Review"),
    )
    title = models.CharField(max_length=150,\
                    verbose_name=u"Post title", unique=True)
    category = models.CharField(max_length=1,\
                    choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True,\
                    verbose_name=u"Post created")
    last_update = models.DateTimeField(auto_now=True,\
                    verbose_name=u"Last post update")
    content = models.TextField(max_length=10000,\
                    verbose_name=u"Post content")

    class Meta:
        ordering = ["-created_at"]

    def __unicode__(self):
        return "{0} '{1}' by {2}".format(self.category,\
                                  self.title, self.author)
    
    def get_absolute_url(self):
        return "/blog/{0}/".format(self.id)
