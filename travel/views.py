from django.shortcuts import render, redirect
from django.contrib import messages

from travel.models import City, CityImages, Blog

def home_view(request):
    search = request.GET.get('search')
    if search:
        cities = City.objects.filter(name__icontains=search)
    else:
        cities = City.objects.all()

    context = {
        "cities": cities,
    }
    return render(request, 'home.html', context=context)

def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        city_name = request.POST.get('city')
        user = request.user
        city = City.objects.filter(name=city_name).first()
        blog = Blog.objects.create(title=title, content=content, city=city, user=user)
        blog.save()
        blog_id = blog.id
        request.session['blog_id'] = blog_id
        messages.success(request, 'Blog muvaffaqiyatli qo\'shildi!')
        return redirect('add_blog_image')
    return render(request, 'add_blog.html')

def add_blog_image(request):
    blog = Blog.objects.get(id=request.session.get('blog_id'))
    city = blog.city

    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            city_image = CityImages.objects.create(blog=blog, city=city, image=image)
            city_image.save()
            messages.success(request, 'Rasm muvaffaqiyatli qo\'shildi!')

        if request.POST.get('action') == 'add_more':
            return redirect('add_blog_image')
        else:
            return redirect('home')

    return render(request, 'add_image.html')

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs,
    }
    return render(request, 'blogs.html', context=context)

def blog_by_id(reqiest, pk):
    blog = Blog.objects.filter(id=pk).first()
    context = {
        "blog": blog,
    }
    return render(reqiest, 'blog.html', context)

def country_by_id(reqiest, pk):
    country = City.objects.filter(id=pk).first()
    context = {
        "country": country,
    }
    return render(reqiest, 'country.html', context)