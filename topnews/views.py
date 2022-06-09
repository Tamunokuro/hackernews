from multiprocessing import context
from unittest import result
from urllib import request
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Story, Comment, Job
from django.db.models import Q
# Create your views here.

def home(request):
    topstories = Story.objects.all().order_by('-created')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(topstories, 10)
    try:
        mystories = paginator.page(page)
    except PageNotAnInteger:
        mystories = paginator.page(1)
    except EmptyPage:
        mystories = paginator.page(paginator.num_pages)

    context = {"topstories":mystories, "totalstories":topstories.count()}
    return render(request, 'topnews/home.html', context)


def jobs(request):
    my_jobs = Job.objects.all().order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(my_jobs, 15)
    try:
        myjobs = paginator.page(page)
    except PageNotAnInteger:
        myjobs = paginator.page(1)
    except EmptyPage:
        myjobs = paginator.page(paginator.num_pages)

    context= {"my_jobs":myjobs, 'total_jobs':my_jobs.count()}
    return render(request, 'topnews/jobs.html', context)

def comments(request):
    topcomments = Comment.objects.select_related('story_id').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(topcomments, 65)
    try:
        my_comments = paginator.page(page)
    except PageNotAnInteger:
        my_comments = paginator.page(1)
    except EmptyPage:
        my_comments = paginator.page(paginator.num_pages)
    
    context = {"topcomments":my_comments, "total_comments":topcomments.count()}
    return render(request, 'topnews/comments.html', context)


def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    story_comments = Comment.objects.filter(story_id=pk).order_by('-created')

    context = {"story":story, "story_comments":story_comments}
    return render(request, 'topnews/storydetail.html', context=context)


          
def search(request):
    context = {}
    
    search = request.GET.get('search')
    results = Job.objects.filter(Q(
            job_title__icontains=search)).order_by('-created')
    if search in results:

        page = request.GET.get('page', 1)
        paginator = Paginator(results, 15)
        try:
            job_results = paginator.page(page)
        except PageNotAnInteger:
            job_results = paginator.page(1)
        except EmptyPage:
            job_results = paginator.page(paginator.num_pages)

        context['results'] = results
        context['job_results'] = job_results
        context['total_jobs'] = results.count()
        return render(request, 'topnews/job.html', context)
        
    else:
        stories = Story.objects.filter(Q(author__icontains=search) | Q(
            item_type__icontains=search) | Q(title__icontains=search)).order_by('-created')
        page = request.GET.get('page', 1)
        paginator = Paginator(stories, 15)
        try:
            story_results = paginator.page(page)
        except PageNotAnInteger:
            story_results = paginator.page(1)
        except EmptyPage:
            story_results = paginator.page(paginator.num_pages)

    
    context['story_results'] = story_results
    context['stories'] = stories
    
    
    return render(request, 'topnews/search.html', context)




                
                # page = request.GET.get('page', 1)
                # paginator = Paginator(stories, 15)
                # try:
                #     story_results = paginator.page(page)
                # except PageNotAnInteger:
                #     story_results = paginator.page(1)
                # except EmptyPage:
                #     story_results = paginator.page(paginator.num_pages)

         
   
        
            


