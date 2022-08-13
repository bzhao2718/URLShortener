from django.shortcuts import render, get_object_or_404, redirect
from .models import ShortURL
from .forms import URLShortenForm, URLGenerateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import datetime, os
import time
from . import generator_util, Constants, DaoUtil


def home(request):
    context = {'name': 'Home'}
    return render(request, "base.html", context)


def shorturl(request, url_key):
    # retrieve the original url using url_key
    context = {}
    try:
        shorturl = ShortURL.objects.filter(url_key=url_key).first()
        # No match found for the url_key
        if not shorturl:
            context['error_message'] = "There is no matching URL found for key: {}.".format(url_key)
            return render(request=request, template_name="error_page.html", context=context)
        else:
            destination = shorturl.original_url
            return redirect(destination)
    except Exception as ex:
        context['error_message'] = ex.message if hasattr(ex, 'message') else ex
        # Display the error message
        return render(request=request, template_name="error_page.html", context=context)


@login_required
def user_url_history(request):
    context = {}
    # only user
    if not request.user.is_authenticated:
        context['error_message'] = "You have not logged in yet. Please log in or sign up for a new account."
        return render(request=request, template_name="error_page.html", context=context)

    shorturls = ShortURL.objects.filter(user_id=request.user.id).order_by("created_time")
    url_history_list = []
    for result_dict in shorturls.values():
        shortened_url = os.path.join(Constants.LOCAL_HOST, result_dict['url_key'])
        url_history_list.append((result_dict['original_url'], shortened_url, result_dict['created_time']))
    context['url_history_list'] = url_history_list

    return render(request, 'url_history.html', context)


def customize(request):
    context = {}
    try:
        # form_data = URLShortenForm(request.POST) if request.method=="POST" else URLShortenForm()
        if request.method == "POST":
            form_data = URLShortenForm(request.POST)
            original_url = form_data.data.get('original_url')
            url_key = form_data.data.get('url_key')

            # if key the customized key exsists already, warning the user
            if url_key and DaoUtil.is_url_key_exsits(url_key):
                context['warnings'] = "The key your entered has been used. Please choose a different one."
                context['form'] = form_data
                return render(request, "customize_form.html", context=context)

            DaoUtil.save_shorturl(original_url=original_url, url_key=url_key, user_id=request.user.id)
            context['success_message'] = "You have successfully shortened your URL."
            context['short_url'] = os.path.join(Constants.LOCAL_HOST, url_key)
            context['original_url'] = original_url
        else:
            form_data = URLShortenForm()
            # form_data.url_key.required=False
            # form_data.url_key.disabled=True

        context['form'] = form_data
        return render(request, "customize_form.html", context=context)
    except Exception as ex:
        context['error_message'] = ex.message if hasattr(ex, 'message') else ex
        return render(request=request, template_name="error_page.html", context=context)


def generate(request):
    context = {}
    try:
        if request.method == "POST":
            form_data = URLGenerateForm(request.POST)
            original_url = form_data.data.get('original_url')
            url_key = generator_util.generate_unique_key()

            DaoUtil.save_shorturl(original_url=original_url, url_key=url_key, user_id=request.user.id)

            context['success_message'] = "You have successfully shortened your URL."
            context['short_url'] = os.path.join(Constants.LOCAL_HOST, url_key)
            context['original_url'] = original_url
        else:
            form_data = URLGenerateForm()

        context['form'] = form_data
        return render(request, "generate_form.html", context=context)
    except Exception as ex:
        context['error_message'] = ex.message if hasattr(ex, 'message') else ex
        return render(request=request, template_name="error_page.html", context=context)


def signup(request):
    if request.POST == "POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully signed up an account.")
            return redirect("login")
    else:
        form = UserCreationForm()
        context = {"form": form}
    return render(request, "signup.html", context)


def create_examples():
    dt = datetime.datetime.now()
    # timestamp = datetime.timestamp(now)
    timestamp = time.time()
    # visitor = Visitor(name="Jack Zhao",email="myemal@emal.com", created_time=dt)
    # visitor.save()
    shorturl = ShortURL(url_key="abcdef", original_url="https://github.com/PacktPublishing/Web-Development-with-Django",
                        created_time=dt, )
    shorturl.save()


def print_examples():
    # visitor=Visitor.objects.get(name="Jack Zhao")
    # print("visitor: ", visitor)
    shorturl = ShortURL.objects.get(url_key="abcdef")
    print("shorturl key: {} | and original url: {}".format(shorturl.url_key, shorturl.original_url))


@login_required
def profile(request):
    user = request.user
    permissions = user.get_all_permissions()
    return render(request, "profile.html", {'user': user, 'permissions': permissions})


from django.views import View
from django.views.generic.edit import FormView


class ShortenerView(FormView):
    template_name = "generate_form.html"
    form_class = URLShortenForm
    success_url = "/customize"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginFormView(FormView):
    template_name = "registration/login.html"
