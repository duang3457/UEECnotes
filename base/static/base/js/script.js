// to control open/close nav
$(document).ready(function() {
  $('.side-panel-toggle').on('click', function() {
    $('.base_content').toggleClass('content-is-open');
  });
});


// 在页面加载时为当前 URL 对应的 <a> 元素添加 active 类
$(document).ready(function() {
    var currentUrl = window.location.pathname;
    $('a[href="' + currentUrl + '"]').addClass('active');
});

function handleClick(clickedElement) {
    // 移除所有 <a> 元素的 active 类
    $('a').removeClass('active');
    // 给点击的 <a> 元素添加 active 类
    $(clickedElement).addClass('active');
}