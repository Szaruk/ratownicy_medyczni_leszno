from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    path('', views.main_posts, name='main_page'),
    path('posty', views.post_list, name='posty'),
    path('statystyki', views.statistics_list, name='statystyki'),
    path('szkolenia', views.training_post_list, name='szkolenia'),
    path('kontakt', TemplateView.as_view(template_name = "blog/contact.html"), name="kontakt"),
    path('o-nas', views.about_us_list, name='o-nas'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]