function showProfileForm() {

    const section = document.getElementById("editProfileSection");

    if (!section) {
        console.error("Edit Profile section not found!");
        return;
    }

    // Form ko visible karo
    section.classList.add("show");

    // Form tak smooth scroll
    setTimeout(function () {
        section.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }, 100);
}


function openEditProfile() {
    showProfileForm();
}


function openAddProfile() {
    showProfileForm();
}