from pprint import pprint
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://:@localhost:5432/')
connection = engine.connect()

n = connection.execute("""SELECT genre, COUNT(performer_genre.performer_id) FROM genre
LEFT JOIN performer_genre ON genre.id = performer_genre.genre_id
GROUP BY genre.id""").fetchall()

y = connection.execute("""SELECT COUNT(i.year_album) FROM (SELECT album.year_album FROM album 
LEFT JOIN track ON album.id = track.album_id) i 
WHERE i.year_album BETWEEN 2019 AND 2020""").fetchall()

avg = connection.execute("""SELECT name_album, AVG(time_track) FROM track
JOIN album ON track.album_id = album.id
GROUP BY name_album""").fetchall()

py = connection.execute("""SELECT DISTINCT name FROM performer
JOIN performer_album ON performer.id = performer_album.performer_id
JOIN album ON performer_album.album_id = album.id
WHERE year_album != 2020""").fetchall()

cp = connection.execute("""SELECT name_collection FROM collection
JOIN track_collection ON track_collection.collection_id = collection.id
JOIN track ON track_collection.track_id = track.id
JOIN album ON track.album_id = album.id
JOIN performer_album ON performer_album.album_id = album.id
JOIN performer ON performer.id = performer_album.performer_id
WHERE name = 'ATL'""").fetchall()

ag = connection.execute("""SELECT name_album FROM album
JOIN performer_album ON album.id = performer_album.album_id
JOIN performer ON performer_album.performer_id = performer.id
JOIN performer_genre ON  performer.id = performer_genre.performer_id
JOIN genre ON performer_genre.genre_id = genre.id
GROUP BY name_album, name
HAVING COUNT(genre.id) > 1""").fetchall()

tnc = connection.execute("""SELECT name_track FROM track
LEFT JOIN track_collection ON track.id = track_collection.track_id
WHERE track_collection.track_id IS NULL""").fetchall()

st = connection.execute("""SELECT name FROM performer
JOIN performer_album ON performer.id = performer_album.performer_id
JOIN album ON performer_album.album_id = album.id
JOIN track ON album.id = track.album_id
WHERE time_track = (SELECT MIN(time_track) FROM track)""").fetchall()

at = connection.execute("""SELECT name_album FROM album
JOIN track ON album.id = track.album_id
GROUP BY name_album
HAVING COUNT(track.album_id) = (SELECT MIN(c) FROM (SELECT COUNT(track.album_id) c FROM track
GROUP BY track.album_id) t)
""").fetchall()

pprint(n)
pprint(y)
pprint(avg)
pprint(py)
pprint(cp)
pprint(ag)
pprint(tnc)
pprint(st)
pprint(at)




# количество исполнителей в каждом жанре;
# количество треков, вошедших в альбомы 2019-2020 годов;
# средняя продолжительность треков по каждому альбому;
# все исполнители, которые не выпустили альбомы в 2020 году;
# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
# название альбомов, в которых присутствуют исполнители более 1 жанра;
# наименование треков, которые не входят в сборники;
# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
# название альбомов, содержащих наименьшее количество треков.