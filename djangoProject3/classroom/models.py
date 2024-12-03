from django.db import models
from students.models import Student, Teacher
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Classroom(models.Model):
    name = models.CharField(max_length=75)
    class_code = models.CharField(max_length=10, blank=True, null=True)
    class_number = models.SmallIntegerField(blank=True, null=True)
    # syllabus
    # location
    # days
    # start_time
    max_seats = models.SmallIntegerField(default=0, blank=True, null=True)
    seats_taken = models.SmallIntegerField(default=0, blank=True, null=True)
    required_materials = models.TextField(blank=True, null=True)
    teachers = models.ManyToManyField(Teacher,
                                     through='ClassroomTeacher',
                                     related_name='classrooms')
    students = models.ManyToManyField(Student,
                                      through='ClassroomStudent',
                                      related_name='classrooms')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)


    def calculate_final_grade(self):
        pass

    def __str__(self):
        return f"{self.name} {self.class_code}"


class ClassroomStudent(models.Model):
    student = models.ForeignKey(Student, related_name="classes", on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, related_name="classroom_students", on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.student} in {self.classroom}"


class ClassroomTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, related_name="classes", on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, related_name="classroom_teachers", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher} in {self.classroom}"


class Quizam(models.Model):
    """
    Contains basic about quiz and exams. Still need to add questions and the ability to upload
    files and images and link to model forms for answers.
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    classroom = models.ForeignKey(Classroom, related_name="quizams", on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    due_date = models.DateField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    points_available = models.IntegerField(default=100, blank=True, null=True)

    def calculate_grade(self):
        pass

    def __str__(self):
        return f"{self.name} in {self.classroom}"


class Assignment(models.Model):
    """
    This contains information for projects and assignments.
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    classroom = models.ForeignKey(Classroom, related_name="assignments", on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    due_date = models.DateField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    points_available = models.IntegerField(default=100, blank=True, null=True)

    def calculate_grade(self):
        pass

    def __str__(self):
        return f"{self.name} in {self.classroom}"

class CompletedQuizam(Quizam):
    quiz_template = models.ForeignKey(Quizam, related_name="submissions", on_delete=models.CASCADE)
    student = models.ForeignKey(ClassroomStudent, related_name="completed_quizzes", on_delete=models.CASCADE)
    points_scored = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

class CompletedAssignment(Assignment):
    assignment_template = models.ForeignKey(Assignment, related_name="submissions", on_delete=models.CASCADE)
    student = models.ForeignKey(ClassroomStudent, related_name="completed_assignments", on_delete=models.CASCADE)
    points_scored = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name
class Grade(models.Model):
   student = models.ForeignKey(ClassroomStudent, related_name="my_grades", on_delete=models.CASCADE,
                               null=True, blank=True)
   weighted_points = models.IntegerField(default=0, blank=True, null=True)
   weighted_available = models.IntegerField(default=0, blank=True, null=True)

   # ContentType for GNF
   content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                    blank=True, null=True)
   object_id = models.PositiveIntegerField(blank=True, null=True)
   content_object = GenericForeignKey('content_type', 'object_id')

   def __str__(self):
        return f"{self.weighted_points} / {self.weighted_available}"


class FinalGrade(models.Model):
    student = models.ForeignKey(Student, related_name="my_grades", on_delete=models.CASCADE)
    grade = models.SmallIntegerField(default=0)
    classroom = models.ForeignKey(Classroom, related_name="final_grades", on_delete=models.CASCADE)

    def __str__(self):
        return f"final grade:{self.grade}/100 for {self.student.first_name}"