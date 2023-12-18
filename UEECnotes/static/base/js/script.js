// to control open/close nav
$(document).ready(function() {
  $('.side-panel-toggle').on('click', function() {
    $('.content').toggleClass('content-is-open');
  });
});