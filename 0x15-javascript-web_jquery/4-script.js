const $ = window.$;
$('div#toggle_header').click(function (e) {
  $('header').toggleClass('green').toggleClass('red');
});
