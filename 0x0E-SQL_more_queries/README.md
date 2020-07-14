Shell integration

For people not familiar with MySQL syntax, here are handy shell functions which are easy to remember and use (to use them, you need to load the shell functions included further down).

Here is example:

$ mysql-create-user admin mypass
| CREATE USER 'admin'@'localhost' IDENTIFIED BY 'mypass'

$ mysql-create-db foo
| CREATE DATABASE IF NOT EXISTS foo

$ mysql-grant-db admin foo
| GRANT ALL ON foo.* TO 'admin'@'localhost'
| FLUSH PRIVILEGES

$ mysql-show-grants admin
| SHOW GRANTS FOR 'admin'@'localhost'
| Grants for admin@localhost                                                                                   
| GRANT USAGE ON *.* TO 'admin'@'localhost' IDENTIFIED BY PASSWORD '*6C8989366EAF75BB670AD8EA7A7FC1176A95CEF4' |
| GRANT ALL PRIVILEGES ON `foo`.* TO 'admin'@'localhost'

$ mysql-drop-user admin
| DROP USER 'admin'@'localhost'

$ mysql-drop-db foo
| DROP DATABASE IF EXISTS foo