from django.db import models
from django.db.models import F


class Video(models.Model):
    """Video block for page."""

    title = models.CharField(max_length=256)
    video_file = models.URLField()
    subtitles = models.URLField()
    counter = models.IntegerField(default=0)

    class Meta:
        db_table = 'pages__videos'

    def __str__(self):
        return self.title

    def increase_counter(self):
        self.counter += 1
        self.save(update_fields=['counter'])


class Audio(models.Model):
    """Audio block for page."""

    title = models.CharField(max_length=256)
    bitrate = models.PositiveIntegerField()
    counter = models.IntegerField(default=0)

    class Meta:
        db_table = 'pages__audios'

    def __str__(self):
        return self.title

    def increase_counter(self):
        self.counter += 1
        self.save(update_fields=['counter'])


class Text(models.Model):
    """Text block for page."""

    title = models.CharField(max_length=256)
    text = models.TextField()
    counter = models.IntegerField(default=0)

    class Meta:
        db_table = 'pages__texts'

    def __str__(self):
        return self.title

    def increase_counter(self):
        self.counter += 1
        self.save(update_fields=['counter'])


class Page(models.Model):
    """Represent a page."""

    title = models.CharField('Заголовок', max_length=256)
    counter = models.IntegerField(default=0)

    class Meta:
        db_table = 'pages__pages'

    def __str__(self):
        return self.title

    def increase_counters(self):
        """Increase page and blocks counters."""
        self.counter += 1
        self.save(update_fields=['counter'])
        blocks = Block.objects.filter(page=self)
        for block in blocks:
            block.increase_counter()


class Block(models.Model):
    """Page block."""

    ordered = models.PositiveIntegerField('Порядок', default=0)
    page = models.ForeignKey('Page', on_delete=models.CASCADE, related_name='blocks')
    video = models.ForeignKey('Video', on_delete=models.SET_NULL, null=True, blank=True)
    audio = models.ForeignKey('Audio', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.ForeignKey('Text', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'pages__blocks'
        ordering = ('ordered', )

    def __str__(self):
        return self.page.title

    def increase_counter(self):
        if self.video:
            self.video.increase_counter()
        elif self.audio:
            self.audio.increase_counter()
        elif self.text:
            self.text.increase_counter()
