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

          if (width<750) {
              oNAV.style.display="block";
          } else {
              oNAV.style.display="none";
          }
},10);
setInterval(function transfer(){
 var width=document.documentElement.clientWidth || document.body.clientWidth;
 var obasedOnCampus= document.getElementById("basedOnCampus");

          if (width<750) {
              obasedOnCampus.style.borderRight="0";
          } else {
              obasedOnCampus.style.borderRight="1px solid #eee";
          }
},10);

/*   setInterval(function hid(){
 var width=document.documentElement.clientWidth || document.body.clientWidth;
 var ocdusermodalcontainer= document.getElementsByClassName("cd-user-modal-container");

          if (width<754) {
              ocdusermodalcontainer[0].style.maxWidth="340px";
          } else {
              ocdusermodalcontainer[0].style.maxWidth="480px";
          }
},10);*/


   setInterval(function change(){
 var width=document.documentElement.clientWidth || document.body.clientWidth;
 var oleftlabel= document.getElementById("leftlabel");

          if (width<754) {
              oleftlabel.style.marginLeft="20px";
          } else {
              oleftlabel.style.marginLeft="0";
          }
},10);


  jQuery(document).ready(function($) {
      var $form_modal = $('.cd-user-modal'),
          $form_login = $form_modal.find('#cd-login'),
          $form_signup = $form_modal.find('#cd-signup'),
          $form_modal_tab = $('.cd-switcher'),
          $tab_login = $form_modal_tab.children('li').eq(0).children('a'),
          $tab_signup = $form_modal_tab.children('li').eq(1).children('a'),
          $main_nav = $('.main_nav'),
          $close=$('#close');
   var sTdc = document.getElementById("stdc");
      var oTdc = document.getElementById("tdc");
      var timer = null;

      sTdc.addEventListener('mouseover', function() {
          clearTimeout(timer);
          oTdc.style.display = "block";
      }, false);
      oTdc.addEventListener('mouseover', function() {
          clearTimeout(timer);
          oTdc.style.display = "block";
      }, false);

      sTdc.addEventListener('mouseout', function() {
          timer = setTimeout(function() {
              oTdc.style.display = "none";
          }, 500);
      }, false);
      oTdc.addEventListener('mouseout', function() {
          timer = setTimeout(function() {
              oTdc.style.display = "none";
          }, 500);
      }, false);

      var aLi = $('#contentNav li');
      for (i = 0; i < aLi.length; i++) {
          aLi[i].addEventListener('click', function() {
              for (var i = 0; i < aLi.length; i++) {
                  aLi[i].className = '';
              }
              this.className = 'active';
          }, false);
      }


  });


