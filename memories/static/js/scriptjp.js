// document.getElementById('button-custom').addEventListener('click',fuction(){
//     document.querySelector('.bg-modal-jp').style.display = 'flex';
// });

// document.querySelector('.button-wrap-lg').addEventListener('click',function(){
//     document.querySelector('.bg-modal-jp').style.display="flex";
// });

// Hide the picture if clicked, replace with a div element with youtube video
// $('.jp-top-pic').on('click',function(){
//     var $div = $('<div/>', {'class': 'iframe-container', html: '<iframe width="560" height="315" src="https://www.youtube.com/embed/IwnsR8EAbKg?modestbranding=1&rel=0" frameborder="0" allow="accelerometer; autoplay=1; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'});
//     $(this).replaceWith($div);
// });


// The next three code chunks load the youtube videos after the page loads
$(window).load(function(){
    var $div = $('<div/>', {'class': 'iframe-container', html: '<iframe width="560" height="315" src="https://www.youtube.com/embed/IwnsR8EAbKg?modestbranding=1&rel=0" frameborder="0" allow="accelerometer; autoplay=1; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'});
    $('.jp-test44').replaceWith($div);
  });
$(window).load(function(){
    var $div = $('<div/>', {'class': 'iframe-container', html: '<iframe width="560" height="315" src="https://www.youtube.com/embed/JOQrgF52KfI?modestbranding=1&rel=0" frameborder="0" allow="accelerometer; autoplay=1; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'});
    $('.jp-test45').replaceWith($div);
  });
$(window).load(function(){
    var $div = $('<div/>', {'class': 'iframe-container', html: '<iframe width="560" height="315" src="https://www.youtube.com/embed/aye2hbx1jNM?modestbranding=1&rel=0" frameborder="0" allow="accelerometer; autoplay=1; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'});
    $('.jp-test46').replaceWith($div);
  });


// this loads the icon in the nav bar
$(window).load(function(){
    var $div = $('<div/>', {'class': 'rd-navbar-brand ', html: '<a class="brand" href="#"><img class="brand-logo-dark" src="/static/images/WingWarpIcon-48x48.png" alt="" width="48" height="48"/></a>'});
    $('.jp-replace-icon-1').replaceWith($div);
  });


// alternate method to load the youtube videos
//   $( document ).ready(function() {
//     var $div = $('<div/>', {'class': 'iframe-container', html: '<iframe width="560" height="315" src="https://www.youtube.com/embed/IwnsR8EAbKg?modestbranding=1&rel=0" frameborder="0" allow="accelerometer; autoplay=1; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'});
//     $('.jp-test44').replaceWith($div);
//  });
//   $( document ).ready(function() {
//     var $div = $('<div/>', {'class': 'iframe-container', html: '<iframe width="560" height="315" src="https://www.youtube.com/embed/JOQrgF52KfI?modestbranding=1&rel=0" frameborder="0" allow="accelerometer; autoplay=1; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'});
//     $('.jp-test45').replaceWith($div);
//  });
//   $( document ).ready(function() {
//     var $div = $('<div/>', {'class': 'iframe-container', html: '<iframe width="560" height="315" src="https://www.youtube.com/embed/aye2hbx1jNM?modestbranding=1&rel=0" frameborder="0" allow="accelerometer; autoplay=1; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'});
//     $('.jp-test46').replaceWith($div);
//  });