function init(){function e(e,t,i,n,s,o,a,r){var l=function(){var e=!1;return function(t){return void 0!==t&&(e=t),e}}();iw=new google.maps.InfoWindow,google.maps.event.addListener(e,"click",function(){if(l())iw.close(),l(!1);else{var u="<div style='color:#000;background-color:#fff;padding:5px;width:150px;'><h4>"+i+"</h4><p>"+n+"<p><p>"+s+"<p><a href='mailto:"+o+"' >"+o+"<a><a href='"+r+"'' >"+a+"<a></div>";iw=new google.maps.InfoWindow({content:u}),iw.open(t,e),l(!0)}}),google.maps.event.addListener(iw,"closeclick",function(){l(!1)})}var t={center:new google.maps.LatLng(27.734607,85.664078),zoom:12,zoomControl:!0,zoomControlOptions:{style:google.maps.ZoomControlStyle.DEFAULT},disableDoubleClickZoom:!0,mapTypeControl:!0,mapTypeControlOptions:{style:google.maps.MapTypeControlStyle.HORIZONTAL_BAR},scaleControl:!0,scrollwheel:!1,panControl:!0,streetViewControl:!0,draggable:!0,overviewMapControl:!0,overviewMapControlOptions:{opened:!1},mapTypeId:google.maps.MapTypeId.ROADMAP,styles:[{stylers:[{visibility:"off"}]},{featureType:"road",stylers:[{visibility:"on"},{color:"#ffffff"}]},{featureType:"road.arterial",stylers:[{visibility:"on"},{color:"#fee379"}]},{featureType:"road.highway",stylers:[{visibility:"on"},{color:"#fee379"}]},{featureType:"landscape",stylers:[{visibility:"on"},{color:"#f3f4f4"}]},{featureType:"water",stylers:[{visibility:"on"},{color:"#7fc8ed"}]},{},{featureType:"road",elementType:"labels",stylers:[{visibility:"off"}]},{featureType:"poi.park",elementType:"geometry.fill",stylers:[{visibility:"on"},{color:"#83cead"}]},{elementType:"labels",stylers:[{visibility:"off"}]},{featureType:"landscape.man_made",elementType:"geometry",stylers:[{weight:.9},{visibility:"off"}]}]},n=document.getElementById("map"),s=new google.maps.Map(n,t),o=[["Coffee Shop","London","121 1212 2121","info@coffee.com","coffee.com",27.7236,85.5247,"https://mapbuildr.com/assets/img/markers/solid-pin-blue.png"]];for(i=0;i<o.length;i++)description="undefined"==o[i][1]?"":o[i][1],telephone="undefined"==o[i][2]?"":o[i][2],email="undefined"==o[i][3]?"":o[i][3],web="undefined"==o[i][4]?"":o[i][4],markericon="undefined"==o[i][7]?"":o[i][7],marker=new google.maps.Marker({icon:markericon,position:new google.maps.LatLng(o[i][5],o[i][6]),map:s,title:o[i][0],desc:description,tel:telephone,email:email,web:web}),link="http://"!=web.substring(0,7)?"http://"+web:web,e(marker,s,o[i][0],description,telephone,email,web,link)}jQuery(document).ready(function(e){e(".scroll a, .navbar-brand, .gototop,.explore").click(function(t){t.preventDefault(),e("html,body").animate({scrollTop:e(this.hash).offset().top},600,"swing"),e(".scroll li").removeClass("active"),e(this).parents("li").toggleClass("active")})});var wow=new WOW({boxClass:"wowload",animateClass:"animated",offset:0,mobile:!0,live:!0});wow.init(),$(".carousel").swipe({swipeLeft:function(){$(this).carousel("next")},swipeRight:function(){$(this).carousel("prev")},allowPageScroll:"vertical"}),google.maps.event.addDomListener(window,"load",init);var map;