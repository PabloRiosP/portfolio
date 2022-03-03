var locked = false;

var btn_div = document.getElementById("welcome_buttons");
var btn_div_h = window.getComputedStyle(btn_div).getPropertyValue('height');

console.log(btn_div_h)
console.log(typeof btn_div_h)

function animate() {

    btns = document.querySelectorAll("#welcome_buttons a");
    //hder = document.getElementById("welcome_screen");

    btn_div.classList.add("scrolldown-buttons");
    //hder.classList.add("scrolldown-frame");

    /*setTimeout(function () {
        btns.style.display = "none";
        btn_div.style.display = "none";
    }, 2000);*/
}

function onWheelReaction() {
    locked = true;
    animate();
}

function onKeyDownReaction(e) {
    let k = e.key.toString();
    console.log(k);
    if (k === 'ArrowDown' || k === 'ArrowUp') {
        locked = true;
        animate();
    }
}

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
