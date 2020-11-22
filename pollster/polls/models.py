from django.db import models

# Create your models here.

# (models.Model) inherits all the methods ng models.Model class
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # we want to link question FK to the PK of Question table
    # if a question is deleted, all of choices are deleted. models.ForeignKey(<Link of the table here>, other actions)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # para readable yung string sa admin area
    def __str__(self):
        return self.choice_text



    # pag ganito lang ginawa natin, lalabas sa admin area ay: question<object> 
    # gamit tayo ng def __str__(self): // define string (self) that takes in instance of the class.