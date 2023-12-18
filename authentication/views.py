

from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from . tokens import generate_token

from UEECnotes import settings

# Create your views here.
def home(request):

    return render(request, "authentication/home.html")


def profile(request):
    return render(request, "authentication/profile.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_conf = request.POST.get('password_conf')
          
        user_isActive = User.objects.filter(username=username).first()
        if user_isActive:
            if user_isActive.is_active:
                messages.error(request, "username already exist! Please try some other username")
                return redirect('authentication:signup')
            else:
                user_isActive.delete()

        email_isActive = User.objects.filter(email=email).first()
        if email_isActive:
            if email_isActive.is_active:
                messages.error(request, "username already registered!")
                return redirect('authentication:signup')
            else:
                email_isActive.delete()

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('authentication:signup')

        if password != password_conf:
            messages.error(request, "Passwords didn't match")
            return redirect('authentication:signup')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('authentication:signup')

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.is_active = False
        my_user.save()

        messages.success(request, "Your Account has been successfully created. We have sent you a confirmation email, please confirm your email address in order to activate account.")

        # welcome Email
        subject = "Welcome to UEECnotes!!"
        message = " Hello " +\
                  my_user.first_name +\
                  "!! \n" +\
                  " Welcome to UEECnotes!! \n" \
                  " Thank you for visiting our website \n" \
                  " We have also sent you a confirmation email, please confirm your email address in order to activate account. \n\n" \
                  " Thanking you \n" \
                  " 招募前端开发、后端开发、内容创作团队成员\n"\
                  " Yang"
        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email

        current_site = get_current_site(request)
        email_subject = "Confirm your email @ UEECnotes"
        message2 = render_to_string('authentication/email_confirmation.html', {
            'name': my_user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generate_token.make_token(my_user)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [my_user.email],
        )
        email.fail_silently = True
        email.send()
        # sign up successfully
        return redirect('authentication:welcome')

    return render(request, "authentication/signup.html")


def signin(request):

    if request.method == "POST":
        # it is similar to request.POST.get('username')
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # sign in successfully
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "forums/welcome.html", {'fname': fname})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('authentication:home')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('authentication:home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('authentication:welcome')
    else:
        return render(request, 'authentication/activate_failed.html')
