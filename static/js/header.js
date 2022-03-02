window.onwheel = e => {
  if(e.deltaY >= 0){
    // Scrolling Down with mouse
    console.log('Scroll Down');
  } else {
    // Scrolling Up with mouse
    console.log('Scroll Up');
  }
}
