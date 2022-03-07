var locked = false;

function transitions() {
    // Webpage Elements
    let header = document.getElementById("welcome_screen");
    let btns = document.getElementById("welcome_buttons");
    let bar = document.getElementById("nav-bar");

    // Element Attributes
    let hdheight = parseInt(window.getComputedStyle(header, null).getPropertyValue("height").toString());
    let btnsheight = window.getComputedStyle(btns, null).getPropertyValue("height").toString();

    // Attributes calculation for transitions
    hdheight = parseInt((hdheight*2)/3);

    // Applying immediate trasnsitions
    btns.style.height = btnsheight;
    btns.style.opacity = 0.0;

    // Applying transitions with delay
    // 0.5s
    setTimeout(function () {
        header.style.height = `${hdheight}px`;
        header.style.top = "50px";
        bar.style.top = "0px";
        btns.style.transition = "height 0.5s";
        btns.style.height = "0px";
    }, 500);

    // 1s
    setTimeout(function () {
        btns.remove();
    }, 1000);
}

// Transition will be done if was not yet done before.
// If is activated with the mouse wheel conditions are
// not needed.
function onWheelReaction() {
    locked = true;
    transitions();
}

// With keyboard transition is enabled just with Down and Up
// arrows, other keys are ignored.
function onKeyDownReaction(e) {
    let k = e.key.toString();
    if (k === 'ArrowDown' || k === 'ArrowUp') {
        locked = true;
        transitions();
    }
}

// Event listeners.
// Any of those are activates just if no one are activated
// before. Obviously as a frontend js code is reset with a
// page reload, consistent with the css reload.
document.addEventListener('wheel', function(e) {
    if (!locked) {
        onWheelReaction();
    }
});

document.addEventListener('keydown', function(e) {
    if (!locked) {
        onKeyDownReaction(e);
    }
});
