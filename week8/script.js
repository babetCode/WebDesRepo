document.addEventListener("DOMContentLoaded", function() {
    const hamburger = document.getElementById("hamburger");
    const dropdownMenu = document.getElementById("dropdown-menu");

    hamburger.addEventListener("click", function() {
        dropdownMenu.classList.toggle("show");
    });
});
