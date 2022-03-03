var locked = false;

function animate() {
    btns = document.getElementById("welcome_buttons");
    hder = document.getElementById("welcome_screen");

    btns.classList.add("scrolldown-buttons");
    hder.classList.add("scrolldown-frame");

    btns.addEventListener("animationend",
        () => btns.style.display = "none", {
            once: true
        }
    );
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

