const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
const $ = window.$;
$(function () {
  $.ajax({
    url: url,
    success: function (response) {
      $('div#hello').text(response.hello);
    }
  });
});
