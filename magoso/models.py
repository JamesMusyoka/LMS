from django.db import models

class user(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to=, blank=True)

    instructor = 'instructor'
    student = 'student'
    admin = 'admin'

    user_types = [
        (instructor, 'instructor'),
        (student, 'student'),
        (admin, 'admin'),
    ]
    user_types = models.CharField(max_length=50, choices=user_types)

    fullstack = 'fullstack'
    frontend = 'frontend'
    backend = 'backend'

    grouping = [
        (fullstack, 'fullstack'),
        (frontend, 'frontend'),
        (backend, 'backend'),
    ]
    grouping = models.CharField(max_length=50, choices=grouping, null=True)

    cohort4 = 'cohort 4'
    cohort5 = 'cohort 5'
    cohort6 = 'cohort 6'
    cohort7 = 'cohort 7'
    cohort8 = 'cohort 8'
    cohort9 = 'cohort 9'
    cohort10 = 'cohort 10'
    cohort11 = 'cohort 11'
    cohort12 = 'cohort 12'
    cohort13 = 'cohort 13'
    cohort14 = 'cohort 14'
    cohort15 = 'cohort 15'
    cohort16 = 'cohort 16'

    cohort = [
        (cohort4, 'cohort 4'),
        (cohort5, 'cohort 5'),
        (cohort6, 'cohort 6'),
        (cohort7, 'cohort 7'),
        (cohort8, 'cohort 8'),
        (cohort9, 'cohort 9'),
        (cohort10, 'cohort 10'),
        (cohort11, 'cohort 11'),
        (cohort12, 'cohort 12'),
        (cohort13, 'cohort 13'),
        (cohort14, 'cohort 14'),
        (cohort15, 'cohort 15'),
        (cohort16, 'cohort 16'),
    ]
    cohort = models.CharField(max_length=50, choices=cohort)

    def __str__(self):
        return self.user.username
    