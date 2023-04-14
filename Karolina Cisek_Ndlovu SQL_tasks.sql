CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

CREATE TABLE movie_info(
Movie_ID INT PRIMARY KEY,
Movie_Name VARCHAR(50),
Movie_Length TIME,
Age_Rating VARCHAR(5));

CREATE TABLE screens(
Screen_ID INT PRIMARY KEY, 
Four_K BOOLEAN);

CREATE TABLE showings(
Showing_ID INT, 
Movie_ID INT,
Screen_ID INT,
Start_Time TIME,
Available_Seats INT,
FOREIGN KEY (Movie_ID) REFERENCES movie_info(Movie_ID),
FOREIGN KEY (Screen_ID) REFERENCES screens(Screen_ID));

SELECT mov.Movie_Name, sh.Start_Time
FROM movie_info mov
JOIN showings sh
ON mov.movie_id = sh.movie_id
WHERE sh.Start_Time > '12:00:00' AND sh.Available_Seats >= 1
ORDER BY sh.Start_Time;

SELECT mov.Movie_Name, count(*)
FROM movie_info mov
JOIN showings sh
ON mov.movie_id = sh.movie_id
GROUP BY mov.Movie_Name
ORDER BY count(*) DESC
LIMIT 1



