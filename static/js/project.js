var main_container = document.getElementById("main-container");
var bar = document.getElementById("nav-bar");

var barHeight = window.getComputedStyle(bar, null).getPropertyValue("height").toString();

main_container.style.marginTop = barHeight;
