from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=50, null=False)
    courseNumber = models.IntegerField()
    instructor = models.CharField(max_length=50, null=False)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title


# Create your models here.
object1 = djangoClasses(
    1,
    "Class 1",
    1,
    "Dr.Bob",
    90)
object1.save()
object1.__str__()


object2 = djangoClasses(
    2,
    "Class 2",
    2,
    "Dr.Billy",
    90)
object2.save()
object2.__str__()


object3 = djangoClasses(
    3,
    "Class 3",
    3, "Dr.Joe",
    90)
object3.save()
object3.__str__()
