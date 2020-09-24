const $ = window.$;
$(function () {
  const url = 'https://fourtonfish.com/hellosalut/';
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    $('div#hello').text(lang);
    $.ajax({
      url: url,
      data: { lang: lang },
      success: function (response) {
        $('div#hello').text(response.hello);
      }
    });
  });
});
