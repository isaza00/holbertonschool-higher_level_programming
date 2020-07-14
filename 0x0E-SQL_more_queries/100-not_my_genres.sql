-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- cat 100-not_my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT DISTINCT tv_genres.name FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_genres.name NOT IN (SELECT tv_genres.name FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_shows.title = "Dexter") ORDER BY tv_genres.name ASC;
