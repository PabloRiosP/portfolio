document.addEventListener('wheel', function(e) {
  if (e.deltaY >= 0) {
    // Scrolling Down with mouse
    console.log('S Down');
  } else {
    // Scrolling Up with mouse
    console.log('S Up');
  }
});

document.addEventListener('keydown', function(e) {
  console.log(e.key);
});
