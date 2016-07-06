$(function(){
  $("#btn-login").click(
    function(){
      if($("#account").val()=="" || $("#password").val()==""){
        return false;
      }
      var account = $("#account").val();
      var password = $("#password").val();
      var rememberme = false;
      if($("#rememberme").prop("checked")==true){
        rememberme = true;
      }
      $("#btn-login").html("登录中");
      $("#btn-login").attr("disabled","disabled");
      var ajax = $.ajax({
        url: "/service/login/",
        type: 'POST',
        data: {
          account: account,
          password: password,
          rememberme: rememberme
        }
      });

      ajax.done(function(msg){
        if(msg=="true"){
          window.location.reload(true);
        }else{
          alert(msg);
          $("#password").val("");
          $("#btn-login").html("登录");
          $("#btn-login").removeAttr("disabled");
        }
      });

      ajax.fail(function(jqXHR,textStatus){
        alert("Request failed :" + textStatus);
        $("#btn-login").html("登录");
        $("#btn-login").removeAttr("disabled");
      });
    }
  );


      $(window).scroll(function() {
          var top = $(this).scrollTop();
          var flowSearch = $("#flowSearchForm");
          if (top < 36) {
              flowSearch.css("display", "none");
          } else {
              flowSearch.css("display", "block");
          }
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

   setInterval(function hid(){
 var width=document.documentElement.clientWidth || document.body.clientWidth;
 var ocdusermodalcontainer= document.getElementsByClassName("cd-user-modal-container");

          if (width<754) {
              ocdusermodalcontainer[0].style.maxWidth="340px";
          } else {
              ocdusermodalcontainer[0].style.maxWidth="480px";
          }
},10);


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


	
      //弹出窗口
      $main_nav.on('click', function  start(event) {

          if ($(event.target).is($main_nav)) {
              // on mobile open the submenu
              $(this).children('a').toggleClass('is-visible');
          } else {
              // on mobile close submenu
              $main_nav.children('a').removeClass('is-visible');
              //show modal layer
              $form_modal.addClass('is-visible');
              //show the selected form
              ($(event.target).is('.cd-signup')) ? signup_selected(): login_selected();
          }

      });



      //关闭弹出窗口
      $('.cd-user-modal').on('click', function(event) {
          if ($(event.target).is($form_modal) || $(event.target).is('.cd-close-form')) {
              $form_modal.removeClass('is-visible');
          }
      });
      $('.cd-user-modal').on('click', function(event) {
          if ($(event.target).is($form_modal) || $(event.target).is('.cd-close-form')) {
              $form_modal.removeClass('is-visible');
          }
      });
      //点叉叉关闭窗口
/*       $close.on('click',function(event){
          $form_modal.removeClass('is-visible');
         })*/
         var  aclose=document.getElementById("close"),
              form_modal = document.getElementsByClassName("cd-user-modal");
			  aclose.addEventListener('click', function() {
			  form_modal[0].className = 'cd-user-modal nav nav-tabs nav-justified';
               }, false);
      //使用Esc键关闭弹出窗口
      $(document).keyup(function(event) {
          if (event.which == '27') {
              $form_modal.removeClass('is-visible');
          }
      });

      //切换表单
      $form_modal_tab.on('click', function(event) {
          event.preventDefault();
          ($(event.target).is($tab_login)) ? login_selected(): signup_selected();
      });

      function login_selected() {
          $form_login.addClass('is-selected');
          $form_signup.removeClass('is-selected');
          $tab_login.addClass('selected');
          $tab_signup.removeClass('selected');
      }

      function signup_selected() {
          $form_login.removeClass('is-selected');
          $form_signup.addClass('is-selected');
          $tab_login.removeClass('selected');
          $tab_signup.addClass('selected');
      }

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

/*      var $aLi1 = $("#personal_data li");
      for (i = 0; i < $aLi1.length; i++) {
          $aLi1.addEventListener('click', function() {
              for (var i = 0; i < aLi.length; i++) {
                  $aLi1.className = '';
              }
              this.className = 'active';
          }, false);
      }
*/
      /*var $aLi1 = $("#personal_data li");
      $aLi1[i].addEventListener('click', function() {
          var num = this.index();
          for (var i = 0; i < this.length; i++) {
              $("#personal_data li:eq(" + num + ") a span").css("background", "#ffffff");
          }
          $("#personal_data li a span").css("background", "#f5f5f5");
      });*/

  });

/*  function getByClass(tagName, className) {
      var tag = document.getElementsByTagName(tagName);
      var tagAll = [];
      for (var i = 0; i < tag.length; i++) {
          if (tag[i].className.indexOf(className) != -1) {
              tagAll[tagAll.length] = tag[i];
          }
      }
      return tagAll;
  }
*/
