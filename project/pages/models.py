from django.db import models


class Video(models.Model):
    """Video block for page."""

    video_file = models.URLField()
    subtitles = models.URLField()

    class Meta:
        db_table = 'pages__videos'

    def __str__(self):
        return str(self.id)


class Audio(models.Model):
    """Audio block for page."""

    bitrate = models.PositiveIntegerField()

    class Meta:
        db_table = 'pages__audios'

    def __str__(self):
        return str(self.id)


class Text(models.Model):
    """Text block for page."""

    text = models.TextField()

    class Meta:
        db_table = 'pages__texts'

    def __str__(self):
        return str(self.id)


class Page(models.Model):
    """Represent a page."""

    title = models.CharField('Заголовок', max_length=256)

    class Meta:
        db_table = 'pages__pages'

    def __str__(self):
        return self.title


class Block(models.Model):
    """Page block."""

    ordered = models.PositiveIntegerField('Порядок', default=0)
    page = models.ForeignKey('Page', on_delete=models.CASCADE, related_name='blocks')
    video = models.ForeignKey('Video', on_delete=models.SET_NULL, null=True, blank=True)
    audio = models.ForeignKey('Audio', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.ForeignKey('Text', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'pages__blocks'

    def __str__(self):
        return self.page.title

