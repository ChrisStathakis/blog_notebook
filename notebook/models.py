from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


COLORS = (
        ('a', 'yellow'),
        ('b', 'white'),
        ('c', 'green'),
        ('d', 'red'),
        ('e', 'blue')
    )


class Tags(models.Model):
    title = models.CharField(unique=True, max_length=240)

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse('notes:tag_update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('notes:tag_delete', kwargs={'pk': self.id})

    @staticmethod
    def filters_data(request, qs):
        q = request.GET.get('q', None)
        search_name = request.GET.get('search_name', None)

        qs = qs.filter(title__icontains=q) if q else qs
        qs = qs.filter(title__icontains=search_name) if search_name else qs
        return qs


class Note(models.Model):
    pinned = models.BooleanField(default=False)
    title = models.CharField(max_length=400)
    description = HTMLField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True, null=True)
    tag = models.ManyToManyField(Tags, blank=True)
    color = models.CharField(max_length=1, choices=COLORS, default='a')

    class Meta:
        ordering = ['-pinned', '-timestamp']

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse('notes:note_update', kwargs={'pk': self.id})

    @staticmethod
    def filters_data(request, qs):
        q = request.GET.get('q', None)
        tags = request.GET.getlist('tag', None)
        if tags:
            tags_ = Tags.objects.filter(id__in=tags)
            qs = qs.filter(tag__in=tags_)
        qs = qs.filter(title__icontains=q) if q else qs
        return qs