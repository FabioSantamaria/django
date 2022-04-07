"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

#from prueba.views import contact_form_view, thanks_view
#from house.views import house_form_view
#from house_form.views import manage_articles
#from store.views import BookListView

from house_pricing_estimator import views

urlpatterns = [
    #path('', home_view, name='home'),
    #path('store/', BookListView),
    #path('thanks/', thanks_view, name='thanks'),
    #path('contact/', contact_form_view, name='contact'),
    #path('articles/', manage_articles, name='articles'),
    #path('house/', house_form_view, name='house'),
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),

    path('admin/', admin.site.urls),
]
