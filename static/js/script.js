/* jshint esversion: 11, jquery: true */

$('.toast').toast('show');

document.addEventListener("DOMContentLoaded", function () {
    // on page load, hide the preloader animation
    document.getElementById("preloader").style.opacity = 0;
    setTimeout(() => {
        document.getElementById("preloader").remove();
    }, 1000);
});