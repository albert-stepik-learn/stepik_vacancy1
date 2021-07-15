from django.shortcuts import render

from vacancy.models import Vacancy


def main_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy/index.html', context= {})


def vacancies_view(request):
    return render(request, 'vacancy/vacancies.html')


def vacancy_view(request, vacancy_id):

    return render(request, 'vacancy.html')


def rubric_view(request, rubric_id):
    return render(request)


def company_view(request, campany_id):
    return render(request)


def confirm_view(request):
    return render(request)
