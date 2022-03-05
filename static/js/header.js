var locked = false;

function animate() {
	let btns = document.querySelectorAll("#welcome_buttons a");
	let hder = document.getElementById("welcome_screen");
	let btn_div = document.getElementById("welcome_buttons");
	//let pic = document.getElementById("avatar");

	btn_div.classList.add("sd-buttons");
	hder.classList.add("sd-frame");
    //pic.classList.add("sd-avatar");

	setTimeout(function () {
		btns.style.display = "none";
		btn_div.style.display = "none";
	}, 2000);
}

function onWheelReaction() {
    locked = true;
    animate();
}

function onKeyDownReaction(e) {
    let k = e.key.toString();
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
