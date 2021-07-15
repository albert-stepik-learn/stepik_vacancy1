from django.db import models


class Speciality(models.Model):
    title = models.CharField(max_length=120)
    code = models.Choices(['testing', 'gamedev'])
    picture = models.URLField(default='https://place-hold.it/100x60')


class Company(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=80)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    title = models.CharField(max_length=120)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    skills = models.Choices(['Python'])
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')




