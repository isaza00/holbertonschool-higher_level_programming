-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- cat 103-rating_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
SELECT tv_genres.name, sum(tv_show_ratings.rate) AS rating FROM tv_show_ratings INNER JOIN tv_shows ON tv_show_ratings.show_id = tv_shows.id INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY rating DESC;
