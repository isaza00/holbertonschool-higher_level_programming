-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
-- usage cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name FROM second_table ORDER BY score DESC;
