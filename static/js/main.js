document.addEventListener("DOMContentLoaded", function () {

    console.log("AI Farmer Assistance Platform loaded successfully.");

    const menuButton = document.querySelector(".mobile-menu-btn");
    const sidebar = document.querySelector(".sidebar");

    if (!menuButton || !sidebar) {
        console.log("Mobile menu elements not found.");
        return;
    }

    menuButton.addEventListener("click", function () {

        sidebar.classList.toggle("active");

        if (sidebar.classList.contains("active")) {
            menuButton.innerHTML = "✕";
            menuButton.setAttribute("aria-label", "Close Menu");
        } else {
            menuButton.innerHTML = "☰";
            menuButton.setAttribute("aria-label", "Open Menu");
        }

    });

    /* Sidebar link click hone ke baad mobile par sidebar close */
    const sidebarLinks = sidebar.querySelectorAll("a");

    sidebarLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            if (window.innerWidth <= 768) {
                sidebar.classList.remove("active");

                menuButton.innerHTML = "☰";
                menuButton.setAttribute("aria-label", "Open Menu");
            }

        });

    });

});

document.addEventListener("DOMContentLoaded", function () {
    const menuButton = document.querySelector(".mobile-menu-btn");
    const navbarLinks = document.querySelector(".navbar-links");

    if (!menuButton || !navbarLinks) return;

    menuButton.setAttribute("aria-expanded", "false");

    menuButton.addEventListener("click", function () {
        const isOpen = navbarLinks.classList.toggle("active");

        menuButton.setAttribute("aria-expanded", String(isOpen));
        menuButton.setAttribute(
            "aria-label",
            isOpen ? "Close Menu" : "Open Menu"
        );

        menuButton.textContent = isOpen ? "✕" : "☰";
    });

    navbarLinks.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", function () {
            navbarLinks.classList.remove("active");
            menuButton.setAttribute("aria-expanded", "false");
            menuButton.setAttribute("aria-label", "Open Menu");
            menuButton.textContent = "☰";
        });
    });
});

