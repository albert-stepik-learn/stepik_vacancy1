from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Company,  Speciality, Vacancy


def main_view(request):
    # specialities = Speciality.objects.all()
    # for speciality in specialities
    # speciality_vacancies_totals = len(Speciality.vacancies.all())
    return render(
        request,
        'vacancy/index.html',
        context={
            'specialities': Speciality.objects.all(),
            'companies': Company.objects.all(),
        }
    )


class VacancyListView(ListView):
    model = Vacancy
    queryset = Vacancy.objects.all()


class VacancyDetailView(DetailView):
    model = Vacancy


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


class SpecialityDetailView(DetailView):
    model = Speciality
    slug_field = 'code'
    slug_url_kwarg = 'code'

    def get_context_data(self, **kwargs):
        context = super(SpecialityDetailView, self).get_context_data(**kwargs)
        context['vacancy_list'] = Vacancy.objects.filter(speciality__id=self.object.pk)
        return context


class CompanyListView(ListView):
    model = Company


class CompanyDetailView(DetailView):
    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['vacancy_list'] = Vacancy.objects.filter(company__id=self.object.pk)
        return context


def confirm_view(request):
    return Http404
