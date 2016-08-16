from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.


class Member(models.Model):

    class Meta:
        verbose_name_plural = _('Students')

    firstname = models.CharField(
        max_length=50
    )

    lastname = models.CharField(
        max_length=50
    )


class Staff(models.Model):

    class Meta:
        verbose_name_plural = _('Staff')

    member = models.ForeignKey(
        'member.Member',
        verbose_name=_('person'),
        related_name='staff_person',
    )


class Student(models.Model):

    class Meta:
        verbose_name_plural = _('Student')

    member = models.ForeignKey(
        'member.Member',
        verbose_name=_('person'),
        related_name='student_person',
    )
