const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const $ = window.$;
$(function () {
  $.ajax({
    url: url,
    success: function (response) {
      $('div#character').text(response.name);
    }
  });
});
