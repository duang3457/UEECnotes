from django.shortcuts import render


def userprofile(request):
    return render(request, 'userprofile/userprofile.html')
