-- creates the database hbtn_0d_2 and the user user_0d_2.
-- cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
