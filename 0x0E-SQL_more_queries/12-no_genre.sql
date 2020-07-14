-- lists all shows contained in hbtn_0d_tvshows without a genre linked. 
-- cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres RIGHT OUTER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_show_genres.genre_id IS NULL ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
