from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    created = models.DateTimeField('Creation', auto_now_add=True)
    last_update = models.DateTimeField('Last Update', auto_now=True)
    status = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'cog'),
        ('lni-stats-up', 'Status'),
        ('lni-user', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    service = models.CharField('Service', max_length=100)
    description = models.CharField('Description', max_length=200)
    icon = models.CharField('Icon', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Member(Base):
    name = models.CharField('Name', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField('Image', upload_to='team',
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.name


class Feature(Base):
    ICON_CHOICES = (
        ('lni-cog', 'cog'),
        ('lni-leaf', 'leaf'),
        ('lni-user', 'Users'),
        ('lni-layers', 'layers'),
        ('lni-laptop-phone', 'laptop'),
        ('lni-rocket', 'Rocket'),
    )
    feature = models.CharField('Feature', max_length=100)
    description = models.CharField('Description', max_length=200)
    icon = models.CharField('Icon', max_length=16, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name = 'Features'

    def __str__(self):
        return self.feature
