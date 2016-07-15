// JavaScript Document
  $(function() {
      $(window).scroll(function() {
          var top = $(this).scrollTop();
          var flowSearch = $("#flowSearchForm");
          if (top < 36) {
              flowSearch.css("display", "none");
          } else {
              flowSearch.css("display", "block");
          }
      });
  });


setInterval(function transfer(){
 var width=document.documentElement.clientWidth || document.body.clientWidth;
 var oNAV= document.getElementById("NAV");

          if (width<754) {
              oNAV.style.display="block";
          } else {
              oNAV.style.display="none";
          }
},10);










