from django.urls import path

from travel.views import home_view, add_blog, add_blog_image, blogs, blog_by_id, country_by_id

urlpatterns = [
    path('', home_view, name='home'),
    path('add-blog/', add_blog, name='add_blog'),
    path('add-blog-image/', add_blog_image, name='add_blog_image'),
    path('blogs/', blogs, name='blogs'),
    path('blog-by-id/<int:pk>/', blog_by_id, name='blog'),
    path('city-by-id/<int:pk>/', country_by_id, name='city'),
]