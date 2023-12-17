from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse
from forums.models import Post


# Create your views here.
@login_required(login_url='/home/')
def game_snake(request):
    return render(request, 'game.html')


@login_required(login_url='/home/')
def forums(request):
    if request.method == 'POST':
        # 处理表单提交

        title = request.POST.get('post-title')
        content = request.POST.get('post-content')

        # 创建并保存新的Post对象
        Post.objects.create(post_name=title, post_content=content)


        # 可以根据需要重定向到成功页面或其他页面
        return redirect("forums:forums")
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'forums.html', {'posts': posts})


@login_required(login_url='/home/')
def welcome(request):
    #print(request.user.is_authenticated)
    fname = request.user.first_name
    return render(request, 'welcome.html', {"fname": fname})


@login_required(login_url='/home/')
def contact(request):
    return render(request, 'contact.html')


@login_required(login_url='/home/')
def ab(request):
    return render(request, 'notes/ab.html')