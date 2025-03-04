from django.db import models

class Movie(models.Model):
    moive_name = models.CharField(max_length=200, null=False)
    language = models.CharField(max_length=75, null=False)
    gener = models.CharField(max_length=100, null=False)
    rating = models.FloatField()

class Show(models.Model):
    movie = models.CharField(max_length=100, null=False)
    time = models.TimeField()
    price = models.FloatField()

class Booking(models.Model):
    user = models.CharField(max_length=50, null=False)
    show = models.CharField(max_length=100, null=False)
    seat = models.CharField(max_length=50, null=False)
    booking_time = models.DateTimeField()
    total_price = models.FloatField()
    is_paid = models.BooleanField(default=False)


class Student(models.Model):
    first_name = models.CharField(max_length=50, null = False)
    last_name = models.CharField(max_length=50, null = False)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=10, null = False)
    address = models.TextField()

class Class(models.Model):
    grade = models.CharField(max_length=10, null = False)
    section = models.CharField(max_length=5, null=False)
    students = models.ManyToManyField(Student, related_name="student_class")

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True)
    address = models.TextField()
    assigned_class = models.OneToOneField(Class, on_delete=models.SET_NULL, null=True, related_name="class_teacher")

class Subject(models.Model):
    name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=10, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="subjects")
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="subjects")

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="marks")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="marks")
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)

class Ranking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="ranking")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="ranking")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="ranking")
    marks = models.ForeignKey(Marks, on_delete=models.CASCADE, related_name="ranking")
    total_marks = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    rank = models.PositiveIntegerField()