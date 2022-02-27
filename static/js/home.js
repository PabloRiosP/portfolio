// global lock, so put this code in a closure of some sort so you're not polluting.
let locked = false;
let lastCall = false;

function runOnScroll(element) {
    if(locked) return;

    if (lastCall) clearTimeout(lastCall);
    lastCall = setTimeout(() => {
        runOnScroll(element);
        // you do this because you want to handle the last
        // scroll event, even if it occurred while another
        // event was being processed.
    }, 200);

    // ...your code goes here...


    locked = false;
};
