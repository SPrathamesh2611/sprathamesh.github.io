
document.addEventListener("DOMContentLoaded", function () {
    // Get all navbar links
    const navLinks = document.querySelectorAll(".navbar-nav a.nav-link");

    // Smooth scrolling when a link is clicked
    navLinks.forEach(function (link) {
        link.addEventListener("click", function (e) {
            e.preventDefault();

            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: "smooth",
                });
            }
        });
    });
});


