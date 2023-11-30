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


# ............***............ Vision Description ............***............

@login_required()
def vision_description_list(request):
    vision_description_list_qs = VisionDescription.objects.all()
    page_title = 'Vision Description List'
    is_vision_description = False
    if vision_description_list_qs.count() > 0:
        is_vision_description = True

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'vision_description_list_qs': vision_description_list_qs,
        'is_vision_description' : is_vision_description
    }
    return render(request, 'page/vision/vision-description-list.html', context)


@login_required
def vision_description_create(request):
    page_title = 'Vision Description Create'
    form = VisionDescriptionManageForm(request.POST)

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'form': form
    }
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        icon = request.FILES["icon"]
        vision_description_qs = VisionDescription.objects.create(
            title=title,description=description, icon=icon
        )
        vision_qs = Vision.objects.all().last()
        if vision_qs:
            vision_description_qs.vision = vision_qs
            vision_description_qs.save()
        return HttpResponseRedirect(reverse('vision_description_list'))
    return render(request, 'page/vision/vision-description-create.html', context)



@login_required
def vision_description_update(request, id):
    vision_description_qs = VisionDescription.objects.filter(pk = id).last()
    page_title = 'Vision Description Update'
    form = VisionDescriptionManageForm(instance=vision_description_qs)

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'form': form
    }
    if request.method == 'POST':
        form = VisionDescriptionManageForm(request.POST, request.FILES,
                              instance=vision_description_qs)
        if form.is_valid():
            form.save()
        vision_description_qs.title = request.POST.get('title')
        vision_description_qs.description = request.POST.get('description')
        vision_qs = Vision.objects.all().last()
        if vision_qs:
            vision_description_qs.vision = vision_qs
        vision_description_qs.save()
        return HttpResponseRedirect(reverse('vision_description_list'))
    return render(request, 'page/vision/vision-description-create.html', context)


@login_required
def vision_description_details(request, id):
    vision_description_qs = VisionDescription.objects.filter(pk = id).last()
    page_title = 'Vision Description Details'

    company_qs = Company.objects.all().last()
    context = {
        'company_qs': company_qs,
        'page_title': page_title,
        'vision_description_qs': vision_description_qs
    }
    return render(request, 'page/vision/vision-description-details.html', context)

