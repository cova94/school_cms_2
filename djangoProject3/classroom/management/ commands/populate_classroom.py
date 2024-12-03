from diploma.class_library.class_index import CORE_CLASSES
from classroom import models
import random
from diploma.models import CoreClass
from django.core.management.base import BaseCommand
from faker import Faker
from classroom import models

from students.models import Teacher, Student


class Command(BaseCommand):
    help = 'Populate Classrooms'



    def handle(self, *args, **options):
        fake = Faker()
        core_classes = CoreClass.objects.all()
        core = random.choice(core_classes)

        teachers = Teacher.objects.all()
        teacher = random.choice(teachers)

        students = Student.objects.all()[:30]

        