from django.db import models


class About(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Stores a single contact request message
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
