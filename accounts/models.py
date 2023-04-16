from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
from django.utils import timezone

from django.db.models import ImageField


class feed(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=200)


class student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    course = models.TextField(max_length=200)
    semester = models.CharField(max_length=20)
    contact = models.IntegerField()
    prof = models.ImageField(upload_to="photos/", null=True)
    mess = models.ImageField(upload_to="messphotos/", null=True)


class Meal(models.Model):
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)

    def is_breakfast_time(self):
        now = timezone.now()
        return now.time() >= datetime.time(22, 0) or now.time() < datetime.time(7, 0)

    def is_lunch_time(self):
        now = timezone.now()
        return datetime.time(10, 0) <= now.time() < datetime.time(12, 0)

    def is_dinner_time(self):
        now = timezone.now()
        return datetime.time(15, 0) <= now.time() < datetime.time(18, 0)

    def count_checked_boxes(self):
        count = 0
        if self.breakfast:
            count += 1
        if self.lunch:
            count += 1
        if self.dinner:
            count += 1
        return count
    
    DAY_CHOICES = (
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    )

    MEAL_CHOICES = (
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
    )

    day = models.IntegerField(choices=DAY_CHOICES)
    meal_type = models.CharField(choices=MEAL_CHOICES, max_length=20)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Add any other relevant fields here

    class Meta:
        unique_together = ("day", "meal_type")
