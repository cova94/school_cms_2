from django.db import models
from students.models import Student

class Diploma(models.Model):
    """
    Responsible for storing all information about students overall progress towards graduation.
    """
    graduation_date = models.DateField(null=True, blank=True)
    GPA = models.FloatField(null=True, blank=True)
    GPA2 = models.FloatField(null=True, blank=True)
    hours_attempted = models.IntegerField(null=True, blank=True)
    hours_completed = models.IntegerField(null=True, blank=True)
    classes_attempted = models.JSONField(null=True, blank=True)
    classes_completed = models.JSONField(null=True, blank=True)

class StudentDiploma(Diploma):
    """
    Ties the Diploma model to a specific student.
    """
    student = models.OneToOneField(Student, related_name="my_diploma", on_delete=models.CASCADE)

    def __str__(self):
        return f"Diploma for {self.student.first_name}{self.student.last_name}"


class CoreClass(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=5)
    class_type = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField()
    credits = models.IntegerField()
    pre_requisites = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.department}{self.code}"


class ElectiveClass(CoreClass):
    is_elective = models.BooleanField(default=True)


class SpecialistClass(CoreClass):
    pass

class Term(models.Model):
    """
    Contains information about classes being taken in a single term.
    """
    name = models.CharField(max_length=20)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    max_hours_allowed = models.IntegerField(default=20)
    registered_for = models.JSONField(null=True, blank=True)
    in_progress = models.JSONField(null=True, blank=True)
    gpa = models.FloatField(default=0, null=True)

class StudentTerm(Term):
    """
    This is responsible for tying a student object and a term object and will also have a hidden
    field for classroom objects for the term.
    """
    student = models.ForeignKey(Student, related_name="my_terms", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} for {self.student.first_name} {self.student.last_name}"
