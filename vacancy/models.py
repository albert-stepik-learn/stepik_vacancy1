import json

from django.db import models


class Speciality(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    picture = models.URLField(default='https://place-hold.it/100x60')

    # def code_set(self, code):
    #     self.code = json.dumps(code)
    #
    # def code_get(self):
    #     return json.loads(self.code)
    #

class Company(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=200)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    # def code_set(self, skills):
    #     self.skills = json.dumps(skills)
    #
    # def code_get(self):
    #     return json.loads(self.skills)



