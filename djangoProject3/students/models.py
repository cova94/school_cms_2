from django.db import models
from django.contrib.auth.models import User

class Student(User):
    gpa = models.FloatField(default=0)
    classification = models.CharField(max_length=12,
                                      blank=False,
                                      null=False)
    # specialization
    is_test_entry = models.BooleanField(default=False)
    #address
    #emergency_contact
    #medical_info
    

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = "Student"

    def calculate_gpa(self, grades):
        pass

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Teacher(User):

    degree = models.CharField(max_length=12,
                              blank=False,
                              null=False)
    university = models.CharField(max_length=100,
                                  blank=True,
                                  null=True)
    is_test_entry = models.BooleanField(default=False)

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = "Student"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
