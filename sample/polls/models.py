from django.db import models

# class Question(models.Model):
# 	question_text = models.CharField(max_length=200)
# 	pub_date = models.DateTimeField("date published")


# class Choice(models.Model):
# 	question = models.ForeignKey(Question, on_delete = models.CASCADE)
# 	choice_text = models.CharField(max_length=200)
# 	votes = models.IntegerField(default=0)

class Book(models.Model):
	title = models.CharField(max_length=100, null=True)
	author = models.CharField(max_length=100, null=True)
	published_date = models.DateField()
