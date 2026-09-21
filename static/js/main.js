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

