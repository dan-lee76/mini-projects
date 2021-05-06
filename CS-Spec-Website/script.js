//This script controls the show/hide functionality on the timelines
var year = document.getElementsByClassName("container-title");
var i;

for (i = 0; i < year.length; i++) {
  year[i].addEventListener("click", function() {
    var x;
    var parent = this.parentElement;
    for (x = 0; x < parent.children.length; x++) {
      child = parent.children[x];
      if (child.classList.contains("container")) {
        if (child.style.display === "block") {
          child.style.display = "none";
        } else {
          child.style.display = "block";
        }
      }      
    }
  });
}