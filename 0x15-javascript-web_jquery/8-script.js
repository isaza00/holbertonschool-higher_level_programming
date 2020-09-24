const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $ = window.$;
$(function () {
  $.ajax({
    url: url,
    success: function (response) {
      for (const movie of response.results) {
        $('ul#list_movies').append('<li>' + movie.title + '</li>');
      }
    }
  });
});
