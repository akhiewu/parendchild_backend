from django.shortcuts import render

from utils.custom_viewset import CustomViewSet
from utils.response_wrapper import ResponseWrapper
from .serializers import *
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.conf import settings

# ............***............ Index ............***............
@login_required
def index(request):
    context = {}

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs
    }
    return render(request, 'page/company-profile/profile.html', context)

# ............***............ Company ............***............
@login_required
def company_profile(request):
    company_qs = Company.objects.all().last()
    context = {
        'company_qs':company_qs
    }
    return render(request, 'page/company-profile/profile.html', context)


@login_required
def company_profile_update(request, id):
    company_qs = Company.objects.filter(pk = id).last()
    page_title = 'Company Profile '
    form = CompanyManageForm(instance=company_qs)
    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'form': form
    }
    if request.method == 'POST':
        form = CompanyManageForm(request.POST, request.FILES, instance=company_qs)
        if form.is_valid():
            form.save()

        company_qs.name = request.POST.get('name')
        company_qs.description = request.POST.get('description')
        company_qs.address = request.POST.get('address')
        company_qs.phone = request.POST.get('phone')
        company_qs.email = request.POST.get('email')
        company_qs.socials = request.POST.get('socials')
        company_qs.facebook_url = request.POST.get('facebook_url')
        company_qs.twitter_url = request.POST.get('twitter_url')
        company_qs.instagram_url = request.POST.get('instagram_url')
        company_qs.linkedin_url = request.POST.get('linkedin_url')
        company_qs.save()
        return HttpResponseRedirect(reverse('company_profile'))
    return render(request, 'page/company-profile/profile_update.html', context)


# ............***............ Parent ............***............

@login_required()
def parent_list(request):
    parent_list_qs = Parent.objects.all()
    page_title = 'Parent List'
    is_parent = False
    if parent_list_qs.count() > 0:
        is_parent = True

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'parent_list_qs': parent_list_qs,
        'is_parent' : is_parent
    }
    return render(request, 'page/parent/parent-list.html', context)


@login_required
def parent_create(request):
    page_title = 'Parent Create'
    form = ParentManageForm(request.POST)

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'form':form
    }
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        address = request.POST.get("address")
        street = request.POST.get("street")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip") 
        parent_qs = Parent.objects.create(
            first_name=first_name,last_name=last_name, address=address,
            street=street, city=city, state=state, zip=zip
        )
        company_qs = Company.objects.all().last()
        if company_qs:
            parent_qs.company = company_qs
            parent_qs.save()
        return HttpResponseRedirect(reverse('parent_list'))

    return render(request, 'page/parent/parent-create.html', context)



@login_required
def parent_update(request, id):
    parent_qs = Parent.objects.filter(pk = id).last()
    page_title = 'Parent Update'
    form = ParentManageForm(instance=parent_qs)
    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'form': form
    }
    if request.method == 'POST':
        form = ParentManageForm(request.POST, request.FILES,
                              instance=parent_qs)
        if form.is_valid():
            form.save()
        parent_qs.first_name = request.POST.get('first_name')
        parent_qs.last_name = request.POST.get('last_name')
        parent_qs.address = request.POST.get('address')
        parent_qs.street = request.POST.get('street')
        parent_qs.city = request.POST.get('city')
        parent_qs.state = request.POST.get('state')
        parent_qs.zip = request.POST.get('zip')
        company_qs = Company.objects.all().last()
        if company_qs:
            parent_qs.company = company_qs
        parent_qs.save()    
        return HttpResponseRedirect(reverse('parent_list'))
    return render(request, 'page/parent/parent-create.html', context)


@login_required
def parent_details(request, id):
    parent_qs = Parent.objects.filter(pk = id).last()
    page_title = 'Parent Details'

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'parent_qs': parent_qs
    }
    return render(request, 'page/parent/parent-details.html', context)


# ............***............ Child Description ............***............

@login_required()
def child_description_list(request):
    child_description_list_qs = Child.objects.all()
    page_title = 'child Description List'
    is_child_description = False
    if child_description_list_qs.count() > 0:
        is_child_description = True

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'child_description_list_qs': child_description_list_qs,
        'is_child_description' : is_child_description
    }
    return render(request, 'page/parent/child-description-list.html', context)


@login_required
def child_description_create(request):
    page_title = 'Child Description Create'
    form = ChildDescriptionManageForm(request.POST)

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'form': form
    }
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        child_description_qs = Child.objects.create(
            first_name=first_name,last_name=last_name,
        )
        parent_qs = Parent.objects.all().last()
        if parent_qs:
            child_description_qs.vision = parent_qs
            child_description_qs.save()
        return HttpResponseRedirect(reverse('child_description_list'))
    return render(request, 'page/parent/child-description-create.html', context)



@login_required
def child_description_update(request, id):
    child_description_qs = Child.objects.filter(pk = id).last()
    page_title = 'Child Description Update'
    form = ChildDescriptionManageForm(instance=child_description_qs)

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'form': form
    }
    if request.method == 'POST':
        form = ChildDescriptionManageForm(request.POST, request.FILES,
                              instance=child_description_qs)
        if form.is_valid():
            form.save()
        child_description_qs.first_name = request.POST.get('first_name')
        child_description_qs.last_name = request.POST.get('last_name')
        parent_qs = Parent.objects.all().last()
        if parent_qs:
            child_description_qs.vision = parent_qs
        child_description_qs.save()
        return HttpResponseRedirect(reverse('child_description_list'))
    return render(request, 'page/parent/child-description-create.html', context)


@login_required
def child_description_details(request, id):
    child_description_qs = Child.objects.filter(pk = id).last()
    page_title = 'Child Description Details'

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'child_description_qs': child_description_qs
    }
    return render(request, 'page/parent/child-description-details.html', context)

