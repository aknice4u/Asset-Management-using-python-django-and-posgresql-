import json
from datetime import datetime

from django.contrib.auth import logout, authenticate, login, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Category
from .models import Brand
from .models import Assets
from .models import Department
from .models import CompanyBranch
import requests


# from django.http import httpResponse


# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def home(request):
    return render(request, "assetsmgt/index.html")


def add_category(request):
    all_cat = {'category_list': Category.objects.all()}
    return render(request, "assetsmgt/add_category.html", all_cat)


def save_category(request):
    category_name = request.POST['category_name']
    dateadded = timezone.now

    cat = Category(category_name=category_name)
    cat.save()
    success_msg = "Successfully Saved"
    return redirect('/add-category')


def update_category(request, id):
    if request.method == "GET":
        single_cat = {'category_single': Category.objects.get(pk=id)}
        return render(request, "assetsmgt/update_category.html", single_cat)


def save_updated(request):
    id = request.POST['id']
    catname = Category.objects.get(pk=id)
    category_name = request.POST['category_name']

    # cat = Category(category_name=category_name)
    catname.category_name = category_name
    catname.save()
    return redirect('/add-category')


def delete_category(request, id):
    cat = Category.objects.get(pk=id)
    cat.delete()
    return redirect('/add-category')


def create_brand(request):
    if request.method == "GET":
        all_cat = Category.objects.all()
        all_brands = Brand.objects.all().select_related('category')
        return render(request, "assetsmgt/brand/create_brand.html",
                      {'category_list': all_cat, 'brand_list': all_brands})
    else:
        if request.method == "POST":
            category = request.POST['category_name']
            brand = request.POST['brand_name']
            save_brand = Brand(category_id=category, brand_name=brand)
            save_brand.save()
            r = requests.post('http://127.0.0.1:5000/api/getall',
                              data={'first_name': 'Emmanuel', 'surname': 'Grace', 'email': 'emma@mail.com',
                                    'phone': '3664883636'})

            return redirect('/add-brand')


def edit_brand(request, id):
    if request.method == "GET":
        brandid = id
        all_cat = Category.objects.all()
        single_brand = Brand.objects.get(pk=id)
        return render(request, "assetsmgt/brand/update_brand.html",
                      {'brand_single': single_brand, 'brandid': brandid, 'category_list': all_cat})


def update_brand(request):
    id = request.POST['id']
    brandname = Brand.objects.get(pk=id)
    brand = request.POST['brand_name']
    catid = request.POST['category_name']

    # cat = Category(category_name=category_name)
    brandname.category_id = catid
    brandname.brand_name = brand
    brandname.save()
    return redirect('/add-brand')
    return redirect('add-brand')


def delete_brand(request, id):
    bran = Brand.objects.get(pk=id)
    bran.delete()
    return redirect('/add-brand')


def add_asset(request):
    if request.method == "GET":
        all_cat = Category.objects.all()
        return render(request, "assetsmgt/assets/add_assets.html", {'category_list': all_cat})
    else:
        if request.method == "POST":
            assetname = request.POST['assetname']
            year_purchased = request.POST['year_purchased']
            condition = request.POST['condition']
            brand = request.POST['brand_name']
            category = request.POST['category_name']
            amount_purchased = request.POST['amount_purchased']
            current_value = request.POST['current_value']
            quantity = request.POST['quantity']
            warranty = request.POST['warranty_date']

            myfile = request.FILES['asset_image']
            fs = FileSystemStorage()
            filename = myfile.name
            photo_path = filename
            save_asset = Assets(
                assetname=assetname, year_purchased=year_purchased, category_id=category, brand_id=brand,
                quantity=quantity, current_value_amount=current_value, amount_purchased=amount_purchased,
                condition=condition, photo_path=photo_path
            )
            save_asset.save()
            thefile = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(thefile)

            return redirect('add-asset')


def fetch_brands(request):
    catid = request.POST['category_id']
    all_brands = list(Brand.objects.filter(category=catid).values())
    return JsonResponse(all_brands, safe=False)


def list_assets(request):
    all_assets = Assets.objects.all().select_related('category').select_related('brand')
    return render(request, "assetsmgt/assets/list_assets.html", {'assets_list': all_assets})


def view_login(request):
    if request.method == 'GET':
        return render(request, 'assetsmgt/login/login.html')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        return render(request, 'assetsmgt/login/login.html')


def add_department(request):
    if request.method == 'GET':
        all_departments = Department.objects.all()
        return render(request, 'assetsmgt/department/add_department.html', {'allDepartments': all_departments})
    else:
        if request.method == "POST":
            department = request.POST['department']
            description = request.POST['description']
            save_dept = Department(
                department=department, description=description, )
            save_dept.save()
            return redirect('/add-department')


def update_department(request, id=0):
    dept = Department.objects.get(pk=id)
    if request.method == "GET":
        return render(request, 'assetsmgt/department/edit_department.html', {'single_department': dept})
    if request.method == "POST":
        department = request.POST['department']
        description = request.POST['description']
        dept.department = department
        dept.description = description
        dept.save()
        return redirect("/update-department/" + str(id))


def delete_department(request, id):
    dept = Department.objects.get(pk=id)
    dept.delete()
    return redirect('/add-department')


def add_branch(request):
    if request.method == "GET":
        all_branch = CompanyBranch.objects.all()
        return render(request, "assetsmgt/company_branch/branch.html", {'branch_list': all_branch})
    if request.method == "POST":
        branch = request.POST['location']
        address = request.POST['address']
        phone = request.POST['phone']
        dateUpdated = datetime.now()
        save_branch = CompanyBranch(
            location=branch, address=address, contact=phone, update_at=dateUpdated)
        save_branch.save()
        return redirect('/add-branch')


def update_branch(request):
    return render(request, "assetsmgt/company_branch/branch.html")


def delete_branch(request):
    return render(request, "assetsmgt/company_branch/branch.html")


def edit_asset(request, id):
    if request.method == "GET":
        all_cat = Category.objects.all()
        single_asset = Assets.objects.get(pk=id)
        headers = {
            'Authorization': 'Token 832481d258d40291ed4a45179c33a517526570dd'
        }
        response = requests.get('http://127.0.0.1:5000/api/getall', headers=headers)
        allstaff = response.json()

    return render(request, "assetsmgt/assets/edit_asset.html",
                  {'singleAsset': single_asset, 'allCat': all_cat, 'staff': allstaff})
