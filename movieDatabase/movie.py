import sqlite3

from sqlalchemy import true

con = sqlite3.connect("movies.db")
cur = con.cursor()
cur.execute("CREATE TABLE movie (movie_name VARCHAR(60), actor VARCHAR(24), actress VARCHAR(24), year INT(4), director_name VARCHAR(24));")
while true:
    movie_name=str(input("Enter the name of the movie name: "))
    actor=str(input("Actor: "))
    actress=str(input("Actress: "))
    year=int(input("Year Of Release: "))
    director_name=str(input("Director_name :"))
    cur.execute(f"INSERT INTO movie VALUES ('{movie_name}', '{actor}', '{actress}', '{year}','{director_name}');")
    x=str(input("Enter STOP to STOP: "))
    if x=='stop':
        break
cur.execute("Select * from movie")
for i in cur.fetchall():
    print(i)
