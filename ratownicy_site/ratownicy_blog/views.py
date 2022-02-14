from django.shortcuts import render, get_object_or_404
from .models import Post, PostImage, StatisticsImage, AboutUs, MainInfo, InfoSectionDetails, InfoSectionTitle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main_posts(request):
    info_section_title = InfoSectionTitle.objects.all()
    info_section_details = InfoSectionDetails.objects.all()
    main_info = MainInfo.objects.all()
    main_post = Post.published.all().order_by('-publish').first()
    posts = Post.published.all().exclude(title = main_post)[:4]
    statistics = StatisticsImage.objects.all().order_by('-statisticsPublished')[:3]

    return render(request,
                  'blog/base.html',
                  {'main_post' : main_post , 'posts' : posts, 'statistics': statistics, 
                  'main_info': main_info,'info_section_details': info_section_details,
                  'info_section_title': info_section_title})

def post_list(request):
    posts = Post.published.all().filter(categories = "podstawowe")
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/all-posts.html',
                  { 'page': page,
                    'posts': posts})

def training_post_list(request):
    training_posts = Post.published.all().filter(categories="szkolenia")
    paginator = Paginator(training_posts, 5)
    page = request.GET.get('page')
    try:
        training_posts = paginator.page(page)
    except PageNotAnInteger:
        training_posts = paginator.page(1)
    except EmptyPage:
        training_posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/szkolenia.html',
                  {'page': page,
                   'training_posts': training_posts})

def statistics_list(request):
    statistics_list = StatisticsImage.objects.all().order_by('-statisticsPublished')
    paginator = Paginator(statistics_list, 6)
    page = request.GET.get('page')
    try:
        statistics_list = paginator.page(page)
    except PageNotAnInteger:
        statistics_list = paginator.page(1)
    except EmptyPage:
        statistics_list = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/statistics.html',
                  { 'page': page,
                    'statistics_list': statistics_list})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status = 'opublikowane',
                                    publish__year = year,
                                    publish__month = month,
                                    publish__day = day)
    photos = PostImage.objects.filter(post = post)
    return render(request,
                  'blog/post/post-details.html',
                    {'post': post, 'photos': photos})

def about_us_list(request):
    person_list = AboutUs.objects.all()
    return render(request,
                  'blog/about_us.html',
                  {'person_list': person_list})

    