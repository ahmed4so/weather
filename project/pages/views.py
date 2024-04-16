from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import customers
from .models import Post


def home(request):
    
    return render(request, 'pages/index.html', )



@login_required
def about(request):
    customer = customers.objects.get(user=request.user)
    return render(request, 'pages/about.html', {'customer_fullname': customer.Fullname})





@login_required
def contact(request):
    customer = customers.objects.get(user=request.user)
    return render(request, 'pages/contact.html', {'customer_fullname': customer.Fullname})


@login_required
def news(request):
    customer = customers.objects.get(user=request.user)
    posts = Post.objects.all()
    return render(request, 'pages/news.html',{'posts': posts} )




@login_required
def Service(request):
   
    return render(request, 'pages/service.html', )


