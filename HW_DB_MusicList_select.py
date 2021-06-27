from pprint import pprint
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://:@localhost:5432/')
connection = engine.connect()
year = connection.execute("""SELECT name_album, year_album FROM album
WHERE year_album = 2019
""").fetchall()
sorted_time = connection.execute("""SELECT name_track, time_track FROM track
ORDER BY time_track DESC
""").fetchone()
time = connection.execute("""SELECT name_track FROM track
WHERE time_track >= 210
""").fetchall()
collection = connection.execute("""SELECT name_album FROM collection
WHERE year_album BETWEEN 2018 and 2020
""").fetchall()
one_w = connection.execute("""SELECT name FROM performer
WHERE name NOT LIKE '%% %%'
""").fetchall()
like = connection.execute("""SELECT name_track FROM track
WHERE name_track iLIKE '%%like%%'
""").fetchall()
pprint(year)
pprint(sorted_time)
pprint(time)
pprint(collection)
pprint(one_w)
pprint(like)

