from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import FarmerRegistrationForm
from .models import FarmerProfile, ProfileHistory


# =========================================================
# REGISTER
# =========================================================

def register(request):

    if request.method == "POST":

        form = FarmerRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            password = form.cleaned_data["password"]

            user.set_password(password)

            user.save()

            # Create Farmer Profile
            FarmerProfile.objects.create(
                user=user,
                phone=form.cleaned_data["phone"],
                village=form.cleaned_data["village"],
                district=form.cleaned_data["district"],
                state=form.cleaned_data["state"],
            )

            # Get Profile
            profile = FarmerProfile.objects.get(
                user=user
            )

            # Create First History Record
            ProfileHistory.objects.create(
                user=user,
                username=user.username,
                photo=profile.photo,
                phone=profile.phone,
                village=profile.village,
                district=profile.district,
                state=profile.state,
                land_size=profile.land_size,
            )

            login(request, user)

            messages.success(
                request,
                "Registration successful!"
            )

            return redirect("dashboard")

    else:

        form = FarmerRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


# =========================================================
# LOGIN
# =========================================================

def user_login(request):

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "accounts/login.html"
    )


# =========================================================
# LOGOUT
# =========================================================

@login_required
def user_logout(request):

    logout(request)

    return redirect("login")


# =========================================================
# PROFILE
# =========================================================

@login_required
def profile(request):

    farmer_profile, created = FarmerProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        # =================================================
        # USERNAME
        # =================================================

        username = request.POST.get(
            "username",
            ""
        ).strip()

        if username:

            # Check username changed
            if username != request.user.username:

                # Check duplicate username
                username_exists = User.objects.filter(
                    username=username
                ).exclude(
                    id=request.user.id
                ).exists()

                if username_exists:

                    messages.error(
                        request,
                        "This username is already taken. Please choose another username."
                    )

                    return redirect("profile")

                request.user.username = username

        # =================================================
        # EMAIL
        # =================================================

        request.user.email = request.POST.get(
            "email",
            ""
        ).strip()

        # Save User
        request.user.save()

        # =================================================
        # PHONE
        # =================================================

        farmer_profile.phone = request.POST.get(
            "phone",
            ""
        ).strip()

        # =================================================
        # VILLAGE
        # =================================================

        farmer_profile.village = request.POST.get(
            "village",
            ""
        ).strip()

        # =================================================
        # DISTRICT
        # =================================================

        farmer_profile.district = request.POST.get(
            "district",
            ""
        ).strip()

        # =================================================
        # STATE
        # =================================================

        farmer_profile.state = request.POST.get(
            "state",
            ""
        ).strip()

        # =================================================
        # LAND SIZE
        # =================================================

        land_size = request.POST.get(
            "land_size",
            ""
        ).strip()

        farmer_profile.land_size = (
            land_size if land_size else None
        )

        # =================================================
        # PHOTO
        # =================================================

        if request.FILES.get("photo"):

            farmer_profile.photo = request.FILES["photo"]

        # Save Farmer Profile
        farmer_profile.save()

        # =================================================
        # PROFILE HISTORY
        # =================================================

        ProfileHistory.objects.create(
            user=request.user,
            username=request.user.username,
            photo=farmer_profile.photo,
            phone=farmer_profile.phone,
            village=farmer_profile.village,
            district=farmer_profile.district,
            state=farmer_profile.state,
            land_size=farmer_profile.land_size,
        )

        messages.success(
            request,
            "Profile updated successfully!"
        )

        return redirect("profile")

    # =================================================
    # HISTORY
    # =================================================

    history = ProfileHistory.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "accounts/profile.html",
        {
            "farmer_profile": farmer_profile,
            "history": history,
        }
    )


# =========================================================
# PROFILE HISTORY
# =========================================================

@login_required
def profile_history(request):

    history = ProfileHistory.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "accounts/profile_history.html",
        {
            "history": history,
        }
    )


# =========================================================
# EDIT FARMER
# =========================================================

@login_required
def edit_farmer(request, user_id):

    # =================================================
    # GET USER
    # =================================================

    user = get_object_or_404(
        User,
        id=user_id
    )

    # =================================================
    # GET / CREATE FARMER PROFILE
    # =================================================

    farmer_profile, created = FarmerProfile.objects.get_or_create(
        user=user
    )

    # =================================================
    # POST
    # =================================================

    if request.method == "POST":

        # =================================================
        # USERNAME
        # =================================================

        new_username = request.POST.get(
            "username",
            ""
        ).strip()

        # Username empty check
        if not new_username:

            messages.error(
                request,
                "Username cannot be empty."
            )

            return redirect(
                "edit_farmer",
                user_id=user.id
            )

        # =================================================
        # DUPLICATE USERNAME CHECK
        # =================================================

        if new_username != user.username:

            username_exists = User.objects.filter(
                username=new_username
            ).exclude(
                id=user.id
            ).exists()

            if username_exists:

                messages.error(
                    request,
                    "This username is already taken. Please choose another username."
                )

                return redirect(
                    "edit_farmer",
                    user_id=user.id
                )

        # =================================================
        # UPDATE USERNAME
        # =================================================

        user.username = new_username

        # =================================================
        # EMAIL
        # =================================================

        user.email = request.POST.get(
            "email",
            ""
        ).strip()

        # =================================================
        # SAVE USER
        # =================================================

        user.save()

        # =================================================
        # PHONE
        # =================================================

        farmer_profile.phone = request.POST.get(
            "phone",
            ""
        ).strip()

        # =================================================
        # VILLAGE
        # =================================================

        farmer_profile.village = request.POST.get(
            "village",
            ""
        ).strip()

        # =================================================
        # DISTRICT
        # =================================================

        farmer_profile.district = request.POST.get(
            "district",
            ""
        ).strip()

        # =================================================
        # STATE
        # =================================================

        farmer_profile.state = request.POST.get(
            "state",
            ""
        ).strip()

        # =================================================
        # LAND SIZE
        # =================================================

        land_size = request.POST.get(
            "land_size",
            ""
        ).strip()

        farmer_profile.land_size = (
            land_size if land_size else None
        )

        # =================================================
        # PHOTO
        # =================================================

        if request.FILES.get("photo"):

            farmer_profile.photo = request.FILES["photo"]

        # =================================================
        # SAVE FARMER PROFILE
        # =================================================

        farmer_profile.save()

        # =================================================
        # CREATE PROFILE HISTORY
        # =================================================

        ProfileHistory.objects.create(
            user=user,
            username=user.username,
            photo=farmer_profile.photo,
            phone=farmer_profile.phone,
            village=farmer_profile.village,
            district=farmer_profile.district,
            state=farmer_profile.state,
            land_size=farmer_profile.land_size,
        )

        # =================================================
        # SUCCESS MESSAGE
        # =================================================

        messages.success(
            request,
            "Farmer profile updated successfully!"
        )

        # =================================================
        # REDIRECT HISTORY
        # =================================================

        return redirect(
            "profile_history"
        )

    # =================================================
    # EDIT PAGE
    # =================================================

    return render(
        request,
        "accounts/edit_farmer.html",
        {
            "farmer": user,
            "farmer_profile": farmer_profile,
        }
    )