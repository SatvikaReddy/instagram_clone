from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
import uuid
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# class BaseModel(models.Model):
#     """Base model for the application. Uses UUID for pk."""
#     id = models.UUIDField(
#         primary_key=True,
#         editable=False,
#         default=uuid.uuid4,
#     )

#     class Meta:
#         """Metadata."""
#         abstract = True

class post(models.Model):
    """A photo posted by a user."""
    user = models.ForeignKey(
        User, verbose_name="Created By", on_delete=models.CASCADE, related_name="photos"
    )

    caption = models.TextField()
    photo = ProcessedImageField(
        upload_to="photos",
        format="JPEG",
        options={"quality": 90},
        processors=[ResizeToFit(width=1200, height=1200)],
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Photo on {self.date_created}"

    class Meta:
        """Metadata."""

        ordering = ["-date_created"]

class Like(models.Model):
    """A 'like' on a photo."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    photo = models.ForeignKey(post, on_delete=models.CASCADE, related_name="likes")

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} Like"

    class Meta:
        """Metadata."""

        unique_together = (("user", "photo"),)
        ordering = ["-date_created"]

class Comment(models.Model):
    """A comment on a post."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    photo = models.ForeignKey(post, on_delete=models.CASCADE, related_name="comments")

    content = models.TextField(max_length=2000)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        """Metadata."""

        ordering = ["-date_created"]