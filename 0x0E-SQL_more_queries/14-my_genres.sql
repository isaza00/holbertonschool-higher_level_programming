-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT tv_genres.name FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_shows.title = "Dexter" ORDER BY tv_genres.name ASC;
