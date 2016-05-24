$(function() {
  $(window).scroll(function() {
    var top = $(this).scrollTop();
    var flowSearch = $("#flowSearchForm");
    if (top - 36 < 0) {
      flowSearch.css("display", "none");
    } else {
      flowSearch.css("display", "block");
    }
  });
});
  
window.onload = function() {
  var oDiv = document.getElementById('login-model-body');
  var aBtn = oDiv.getElementsByTagName('li');
  var aDiv = document.querySelectorAll(".form-div");
  
  for (var i = 0; i < aBtn.length; i++) {
    aBtn[i].index = i;
    aBtn[i].addEventListener('click', function() {
      for (var i = 0; i < aBtn.length; i++) {
        aBtn[i].className = '';
        aDiv[i].style.display = "none";
      }
      this.className = 'active';
      aDiv[this.index].style.display = "block";
    }, false);
  }
  
  var oBlock = document.getElementById('contentNav');
  var aLi = oBlock.getElementsByTagName('li');
  
  for (var i = 0; i < aLi.length; i++) {
    aLi[i].addEventListener('click', function() {
      for (var i = 0; i < aLi.length; i++) {
        aLi[i].className = '';
      }
      this.className = 'active';
    }, false);
  }
  
  function getByClass(tagName, className) {
    var tag = document.getElementsByTagName(tagName);
    var tagAll = [];
    for (var i = 0; i < tag.length; i++) {
      if (tag[i].className.indexOf(className) != -1) {
        tagAll[tagAll.length] = tag[i];
      }
    }
    return tagAll;
  }
}
  
var oTdc = document.getElementById("tdc");
  
oTdc.addEventListener('mouseover', function() {
  startMove(oTdc, {
    right: 0
  }, false);
}, false);
