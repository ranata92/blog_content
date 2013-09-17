from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta


class ExpQuerySet(models.query.QuerySet):
    '''
    QuerySet for administrative purpose only. Gives access to expired Pastes 
    to archive and delete them
    '''

    def actual(self):
        return self.filter(expiration_date__gte=date.today())

    def expired(self):
        return self.filter(expiration_date__lt=date.today())


class ActualExpiredManager(models.Manager):
    '''
    Class to manage ExpQuerySet. Gives access to it's 
    actual() and expired() methods.
    '''

    def get_query_set(self):
        return ExpQuerySet(self.model)

    def __getattr__(self, attr, *args):
        if attr.startswith("_") or attr.startswith("__"):
            raise AttributeError
        return getattr(self.get_query_set(), attr, *args)


class ActualManager(models.Manager):
    '''
    Actual manager to work with. Returns a QuerySet of actual Pastes.
    '''

    def get_query_set(self):
        return ExpQuerySet(self.model).actual()

    def __getattr__(self, attr, *args):
        if attr.startswith("_") or attr.startswith("__"):
            raise AttributeError
        return getattr(self.get_query_set(), attr, *args)



class Paste(models.Model):

    SYNTAX_CHOICES = (
        ('txt', u'Text'),
        ('py', u'Python'),
        ('js', u'JavaScript'),
        ('rb', u'Ruby'),
        ('pl', u'Perl'),
        ('asp', u'ASP.NET'),
        ('java', u'Java'),
    )

    title = models.CharField(max_length=100, blank=True, verbose_name=u"Paste's Title")
    author = models.ForeignKey(User, null=True, verbose_name=u"Paste's Author")
    content = models.TextField()
    syntax = models.CharField(max_length=5, choices=SYNTAX_CHOICES, default='txt')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u"Was created at")
    modified_at = models.DateTimeField(auto_now=True, verbose_name=u"Was modified at")
    expiration_date = models.DateField(verbose_name=u"Date to expire")

    _objects = ActualManager()
    act_exp = ActualExpiredManager()
    objects = models.Manager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if len(self.title) == 0:
            self.title = u"Untitled Post"
        super(Paste, self).save(*args, **kwargs)

    class Meta:
        ordering=['-created_at']

    def was_modified(self):
        r_range = self.created_at + timedelta(minutes=2)
        if self.modified_at < r_range:
            return False
        return True
    was_modified.short_description = "Was modified"
    was_modified.boolean = True

    def is_expired(self):
        if self.expiration_date < date.today():
            return True
        return False
    is_expired.short_description = "Is expired"
    is_expired.boolean = True

