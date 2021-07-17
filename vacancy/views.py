from django.shortcuts import render, get_object_or_404
from django.http import Http404

from vacancy.models import Company,  Speciality, Vacancy


def main_view(request):
    return render(
        request,
        'vacancy/index.html',
        context={
            'specialities': Speciality.objects.all(),
            'companies': Company.objects.all()
        }
    )


def vacancies_view(request):
    return render(
        request,
        'vacancy/vacancies.html',
        context={
            'vacancies': Vacancy.objects.all()
        }
    )


def vacancy_view(request, vacancy_id):
    return render(
        request,
        'vacancy/vacancy.html',
        context={
            'vacancy': get_object_or_404(Vacancy, pk=vacancy_id)
        }
    )


def speciality_view(request, speciality_code):
    vacancies = Vacancy.objects.filter(speciality__code=speciality_code)
    vacancies_total = len(vacancies)
    return render(
        request,
        'vacancy/speciality.html',
        context={
            'speciality': get_object_or_404(Speciality, code=speciality_code),
            'vacancies': vacancies,
            'vacancies_total': vacancies_total,
        }
    )


def companies_view(request):
    companies = Company.objects.all()
    companies_total = len(companies)
    return render(
        request,
        'vacancy/companies.html',
        context={
            'companies': companies,
            'companies_total': companies_total,
        }
    )

def company_view(request, company_id):
    return render(
        request,
        'vacancy/company.html',
        context={
            'company': get_object_or_404(Company, id=company_id)
        }
    )


def confirm_view(request):
    return Http404
