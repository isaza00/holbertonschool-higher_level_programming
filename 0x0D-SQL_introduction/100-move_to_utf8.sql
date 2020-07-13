--  converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server
-- cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
ALTER DATABASE databasename CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
