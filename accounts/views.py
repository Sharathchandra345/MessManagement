from datetime import date
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .models import feed, student, Meal

from datetime import datetime
# signup
def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Created Successfully!!")
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, "accounts/signup.html", {"form": fm})


# Login View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                upass = fm.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return HttpResponseRedirect("/profile/")
        else:
            fm = AuthenticationForm()
        return render(request, "accounts/userlogin.html", {"form": fm})
    else:
        return HttpResponseRedirect("/profile/")


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")



# profile
#retrieving meal according to day of week

def checkbox_form(request):
    current_time = datetime.now().time()
    if current_time >= datetime.strptime("22:00", "%H:%M").time() or current_time <= datetime.strptime("07:00", "%H:%M").time():
        breakfast_display = True
    else:
        breakfast_display = False

    if current_time >= datetime.strptime("10:00", "%H:%M").time() and current_time <= datetime.strptime("12:00", "%H:%M").time():
        lunch_display = True
    else:
        lunch_display = False

    if current_time >= datetime.strptime("15:00", "%H:%M").time() and current_time <= datetime.strptime("18:00", "%H:%M").time():
        dinner_display = True
    else:
        dinner_display = False

    if request.method == 'POST':
        breakfast_checkbox = request.POST.get('breakfast', False)
        lunch_checkbox = request.POST.get('lunch', False)
        dinner_checkbox = request.POST.get('dinner', False)
        checkbox_count = 0

        if breakfast_checkbox:
            checkbox_count += 1
        if lunch_checkbox:
            checkbox_count += 1
        if dinner_checkbox:
            checkbox_count += 1

        # do something with the checkbox values here
        # ...

    context = {
        'breakfast_display': breakfast_display,
        'lunch_display': lunch_display,
        'dinner_display': dinner_display,
    }
    return render(request, 'checkbox_form.html', context)
def get_today_meals():
    today = date.today().weekday() + 1  # Convert weekday index to day number (1-7)
    print(today)
    meals = Meal.objects.filter(day=today)
    print(meals)
    return meals

#user profile display
def user_profile(request):
    if request.user.is_authenticated:
        meals = get_today_meals()

        return render(
            request, "accounts/profile.html", {"name": request.user, "meals": meals}
        )
    else:
        return HttpResponseRedirect("/")


#profile form
def profileform(request):
    if request.method == "POST":
        name = request.POST["name"]
        roll = request.POST["roll"]
        course = request.POST["course"]
        semester = request.POST["semester"]
        contact = request.POST["contact"]
        pic = request.FILES["prof"]
        mess = request.FILES["mess"]
        std = student(
            name=name,
            roll=roll,
            prof=pic,
            mess=mess,
            course=course,
            semester=semester,
            contact=contact,
        )
        std.save()
    return render(request, "accounts/profileform.html")


#feedback
def feedback(request):
    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        new = feed(name=name, email=email, message=message)
        new.save()
    return render(request, "accounts/feedback.html")

#contact
def contact(request):
    return render(request, "accounts/contacts.html")

#full_mess
def full_mess(request):
    return render(request, "accounts/full_mess.html")
#nighttuck
def night_tuck(request):
    return render(request, "accounts/nighttuck.html")