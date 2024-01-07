from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


@login_required(login_url='/home/')
def userprofile(request):
    MyUser = request.user
    fname = MyUser.first_name
    major = MyUser.future_major
    return render(request, 'userprofile/userprofile.html',
                  {
                      "fname": fname,
                      "major": major
                  })
