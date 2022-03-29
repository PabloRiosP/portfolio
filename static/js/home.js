var locked = false;

var header = document.getElementById("welcome_screen");
var bar = document.getElementById("nav-bar");

var barheight = window.getComputedStyle(bar, null).getPropertyValue("height").toString();

bar.style.top = `-${barheight}`;
bar.style.transition = "top 0.5s";

function transitions() {
    // Webpage Elements
    let btns = document.getElementById("welcome_buttons");

    // Element Attributes
    let hdheight = parseInt(window.getComputedStyle(header, null).getPropertyValue("height").toString());
    let btnsheight = window.getComputedStyle(btns, null).getPropertyValue("height").toString();

    // Attributes calculation for transitions
    hdheight = parseInt((hdheight*2)/3);

    // Applying immediate styles and transitions
    header.style.position = "relative";
    btns.style.height = btnsheight;
    btns.style.opacity = "0.0";

    // Applying transitions with delay
    // 0.5s
    setTimeout(function () {
        header.style.height = `${hdheight}px`;
        header.style.marginTop = barheight;
        bar.style.top = "0px";
        btns.style.transition = "height 0.5s";
        btns.style.height = "0px";
    }, 500);

    // 1s
    setTimeout(function () {
        btns.remove();
        document.body.style.overflowY = "visible";
    }, 1000);
}

// Transition will be done if it isn't yet done before.
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

// The document runs it when the webpage is fully loaded.
window.addEventListener('load', (e) => {
    var vp = document.getElementsByClassName("project-pic-viewport");
    var pic = document.getElementsByClassName("project-picture");

    for (let i = 0; i < vp.length; i++) {
        let ph = pic[i].naturalHeight;
        let pw = pic[i].naturalWidth;

        let vh = window.getComputedStyle(vp[i], null)
                    .getPropertyValue("height").toString();
        let vw = window.getComputedStyle(vp[i], null)
                    .getPropertyValue("width").toString();

        if (ph > pw) {
            pic[i].style.width = vw;
            pic[i].style.top = `${(parseInt(vh) - ((parseInt(vw) * ph) / pw)) / 2}px`;
        } else {
            pic[i].style.height = vh;
            pic[i].style.left = `${(parseInt(vw) - ((parseInt(vh) * pw) / ph)) / 2}px`;
        }
    }
});
