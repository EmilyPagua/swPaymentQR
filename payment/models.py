from django.db import models
import datetime

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class TypeUser(models.Model):
    owner = models.ForeignKey('auth.User', related_name='payment')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

def save(self, *args, **kwargs):
    options = self.title and {'name': self.title} or {}
    formatter = HtmlFormatter(style=self.style, full=True, **options)
    self.highlighted = highlight(self.code, formatter)
    super(TypeUser, self).save(*args, **kwargs)
