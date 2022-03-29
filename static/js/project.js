var header = document.getElementById("item-header");
var bar = document.getElementById("nav-bar");
var mainContainer = document.getElementById("main-container");

var barHeight = window.getComputedStyle(bar, null).getPropertyValue("height").toString();

function fixBodySize() {
    let headerHeight = parseInt(window.getComputedStyle(header, null).getPropertyValue("height").toString());
    let mainHeight = parseInt(window.getComputedStyle(mainContainer, null).getPropertyValue("height").toString());
    let footerHeight = parseInt(window.getComputedStyle(
        document.getElementById("main-footer"), null
    ).getPropertyValue("height").toString());

    if (innerHeight > (parseInt(barHeight) + headerHeight + mainHeight + footerHeight)) {
        let h = `${(innerHeight - parseInt(barHeight) - headerHeight - footerHeight)}px`;
        document.getElementById("lateral-bar").style.height = h;
        document.getElementById("project").style.height = h;
    }
}

header.style.marginTop = barHeight;

// Function to fix page size is executed once webpage is loaded and any time when the browser is resized.
fixBodySize();
document.addEventListener('resize', function(e) {
    fixBodySize();
});
