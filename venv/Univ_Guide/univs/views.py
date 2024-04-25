from django.shortcuts import render
from .models import University, City, Hobby, Post
from random import randint
from django.http import JsonResponse
from fuzzywuzzy import fuzz
from unidecode import unidecode
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'home.html')

def all_univs(request):
    universities = University.objects.all()

    universities_data = []

    for university in universities:
        university_data = {
            'uid': university.uid,
            'name': university.name,
            'city_id': university.city.cid,
            'utype': university.utype,
            'colleges': []
        }

        university_colleges = university.colleges.all()
        for university_college in university_colleges:
            college_data = {
                'cid': randint(0, 1000),
                'name': university_college.collage.name,
                'departments': []
            }

            college_departments = university_college.departments.all()
            for department in college_departments:
                department_data = {
                    'name': department.name,
                    'avg': department.min_avg,
                }
                college_data['departments'].append(department_data)

            university_data['colleges'].append(college_data)

        universities_data.append(university_data)
    
    context = {
        'universities':universities_data,
        'cities': City.objects.all()
    }

    return render(request, 'universities.html',context=context)



def h_basied(request):
    hobbies = Hobby.objects.all()
    context = {
        'hobbies':hobbies,
    }
    return render(request, 'hobbies_based.html', context=context)



def filter_univ(request):
    futype = request.GET.get('utype')
    fdtype = request.GET.get('dtype')
    fmin_avg = request.GET.get('min_avg')
    fhobbies = request.GET.getlist('hobbies[]', None)
    universities = University.objects.all()

    universities_data = []

    for university in universities:
        university_data = {
            'uid': university.uid,
            'name': university.name,
            'city_id': university.city.cid,
            'utype': university.utype,
            'colleges': []
        }

        university_colleges = university.colleges.all()
        for university_college in university_colleges:
            college_data = {
                'cid': randint(0, 1000),
                'name': university_college.collage.name,
                'departments': []
            }

            college_departments = university_college.departments.all()
            for department in college_departments:
                department_data = {
                    'name': department.name,
                    'dtype':department.dtype,
                    'min_avg': department.min_avg,
                    'hobbies': []
                }

                for hobby in department.hobbies.all():
                    department_data['hobbies'].append(hobby.name)

                college_data['departments'].append(department_data)

            university_data['colleges'].append(college_data)

        universities_data.append(university_data)
    
    universities_data_filterd = []

    for university in universities_data:
        if futype != 'all':
            if university['utype'] != futype:
                continue
        for college in university['colleges']:
            for department in college['departments']:
                if department['dtype'] == fdtype or department['dtype'] == 'b' or fdtype == 'b':
                    if department['min_avg'] <= float(fmin_avg):
                        if fhobbies:
                            for hobby in department['hobbies']:
                                hobby_normalized = unidecode(hobby)
                                fhobbies_normalized = [unidecode(fh) for fh in fhobbies]
                                if hobby_normalized in fhobbies_normalized:
                                    universities_data_filterd.append(f"{university['name']}/{college['name']}/{department['name']}")
                                    continue
                                else:
                                    if any(fuzz.partial_ratio(hobby_normalized, fh) >= 80 for fh in fhobbies_normalized):
                                        universities_data_filterd.append(f"{university['name']}/{college['name']}/{department['name']}")
                                        continue
                        else:
                            universities_data_filterd.append(f"{university['name']}/{college['name']}/{department['name']}")

    return JsonResponse({'universities': universities_data_filterd})




def news_posts(request):
    news_posts = Post.objects.order_by('-date')
    context = {
        'news_posts': news_posts
    }

    return render(request, 'newspage.html', context)


def news_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post
    }

    return render(request, 'news_post.html', context)


def advices(request):
    return render(request, 'advices.html')