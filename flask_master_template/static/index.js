/*This function Flashes a message to the user.  The
first usage is in the base template, as to call attention
to the fact, that this file should not be altered.*/
function flashing_text() {
   var x = document.getElementById("warning-text");
   setInterval(function() {
      x.style.display = (x.style.display == 'none' ? '' : 'none');
   }, 300);
}


/*
_______________
|    Toolbar   \__________________________________
|  Example can be found in 'toolbar_example.html'
*/


function homeLink(){
    window.location = 'file:///home/b10/Desktop/project_files/B10OnlineHtml/Html/index.html';
}
function aboutmeLink(){
    window.location = 'file:///home/b10/Desktop/project_files/B10OnlineHtml/Html/index.html';
}
function openHomeMenu(){
    var x = document.getElementById("toolbar-dropdown");
    if (x.style.display == "none"){
        x.style.display = "block";
    }
    else{
        x.style.display = "none";
  }
}


/*
__________________
|    Slideshow    \__________________________________
|  Example can be found in 'slideshow_example.html'
*/


var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
