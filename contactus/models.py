from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateField(auto_now=True)

    class Meta:
        permissions = (
            ("view_contact", "Can view contact"),
        )

    def __unicode__(self):
        return self.name
