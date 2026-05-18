from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
    )
    categories = models.ManyToManyField(
        Category,
        related_name="books",
        blank=True,
    )
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    cover_image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title