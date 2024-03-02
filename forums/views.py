from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse
from forums.models import Post


# Create your views here.


@login_required(login_url='/home/')
def forums(request):
    fname = request.user.first_name
    user_id = request.user.id
    if request.method == 'POST':
        # 处理表单提交

        title = request.POST.get('post-title')
        content = request.POST.get('post-content')

        # 创建并保存新的Post对象
        Post.objects.create(
            post_name = title, 
            post_content = content, 
            post_by_id = user_id, 
            post_by_name = fname)

        # 可以根据需要重定向到成功页面或其他页面
        return redirect("forums:forums")
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'forums/forums.html', {'posts': posts, 'fname': fname})



def welcome(request):
    # print(request.user.is_authenticated)
    if request.user.is_authenticated:
        # 安全地访问 first_name，因为用户已登录
        fname = request.user.first_name
    else:
        # 处理未登录用户的情况
        # 例如，你可以设置一个默认的名字，或者直接跳过某些操作
        fname = "游客"
    return render(request, 'forums/welcome.html', {"fname": fname})


@login_required(login_url='/home/')
def contact(request):
    fname = request.user.first_name
    return render(request, 'forums/contact.html', {"fname": fname})


def update_log(request):
    return render(request, 'forums/update_log.html')


@login_required(login_url='/home/')
def ab(request):
    fname = request.user.first_name
    return render(request, 'notes/ab.html', {"fname": fname})