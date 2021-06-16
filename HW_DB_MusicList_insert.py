import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://:@localhost:5432/')
connection = engine.connect()
connection.execute("""INSERT INTO genre(genre)
VALUES('Russian rap');
""")
connection.execute("""INSERT INTO genre(genre)
VALUES('Rock');
""")
connection.execute("""INSERT INTO genre(genre)
VALUES('Pop');
""")
connection.execute("""INSERT INTO genre(genre)
VALUES('Electro');
""")
connection.execute("""INSERT INTO genre(genre)
VALUES('Russian rock');
""")
connection.execute("""INSERT INTO genre(genre)
VALUES('Dance music');
""")
connection.execute("""INSERT INTO performer(name)
VALUES('ATL');
""")
connection.execute("""INSERT INTO performer(name)
VALUES('Скриптонит');
""")
connection.execute("""INSERT INTO performer(name)
VALUES('Сплин');
""")
connection.execute("""INSERT INTO performer(name)
VALUES('System of A Down');
""")
connection.execute("""INSERT INTO performer(name)
VALUES('Pendulum');
""")
connection.execute("""INSERT INTO performer(name)
VALUES('The Prodigy');
""")
connection.execute("""INSERT INTO performer(name)
VALUES('Miyagi');
""")
connection.execute("""INSERT INTO performer(name)
VALUES('Nirvana');
""")
connection.execute("""INSERT INTO album(name_album, year_album)
VALUES('Кривой эфир', 2019);
""")
connection.execute("""INSERT INTO album(name_album, year_album)
VALUES('Бисер', 2016);
""")
connection.execute("""INSERT INTO album(name_album, year_album)
VALUES('Дом с нормальными явлениями', 2015);
""")
connection.execute("""INSERT INTO album(name_album, year_album)
VALUES('Гранатовый альбом', 1998);
""")
connection.execute("""INSERT INTO album(name_album, year_album)
VALUES('Toxicity', 2001);
""")
connection.execute("""INSERT INTO album(name_album, year_album)
VALUES('Witchcraft', 2010);
""")
connection.execute("""INSERT INTO album(name_album, year_album)
VALUES('Live At Brixton Academy', 2009);
""")
connection.execute("""INSERT INTO album(name_album, year_album)
VALUES('Invaders Must Die', 2009);
""")
connection.execute("""INSERT INTO album(name_album, year_album)
VALUES('Buster Keaton', 2019);
""")
connection.execute("""INSERT INTO album(name_album, year_album)
VALUES('Nevermind', 1991);
""")
connection.execute("""INSERT INTO performer_genre(performer_id, genre_id)
VALUES(1, 1);
""")
connection.execute("""INSERT INTO performer_genre(performer_id, genre_id)
VALUES(2, 1);
""")
connection.execute("""INSERT INTO performer_genre(performer_id, genre_id)
VALUES(3, 5);
""")
connection.execute("""INSERT INTO performer_genre(performer_id, genre_id)
VALUES(4, 2);
""")
connection.execute("""INSERT INTO performer_genre(performer_id, genre_id)
VALUES(5, 4);
""")
connection.execute("""INSERT INTO performer_genre(performer_id, genre_id)
VALUES(5, 6);
""")
connection.execute("""INSERT INTO performer_genre(performer_id, genre_id)
VALUES(6, 4);
""")
connection.execute("""INSERT INTO performer_genre(performer_id, genre_id)
VALUES(7, 1);
""")
connection.execute("""INSERT INTO performer_genre(performer_id, genre_id)
VALUES(8, 2);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(1, 1);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(1, 2);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(2, 2);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(2, 3);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(3, 4);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(4, 5);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(5, 6);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(5, 7);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(6, 7);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(6, 8);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(7, 9);
""")
connection.execute("""INSERT INTO performer_album(performer_id, album_id)
VALUES(8, 10);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(1, 'atlatl1', 250);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(1, 'atlatl2', 235);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(2, 'atlскриптонит1', 179);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(3, 'скриптонит1', 200);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(3, 'скриптонит2', 189);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(4, 'сплин1', 211);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(5, 'soad1', 178);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(5, 'soad2', 199);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(6, 'pendulum1', 200);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(6, 'pendulum2', 221);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(7, 'pendulumprodigy1', 197);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(8, 'prodigy1', 245);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(9, 'miyagi1', 190);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(9, 'miyagi2', 203);
""")
connection.execute("""INSERT INTO track(album_id, name_track, time_track)
VALUES(10, 'Smells Like Teen Spirit', 301);
""")
connection.execute("""INSERT INTO collection(name_album, year_album)
VALUES('collection1', 2020);
""")
connection.execute("""INSERT INTO collection(name_album, year_album)
VALUES('collection2', 2018);
""")
connection.execute("""INSERT INTO collection(name_album, year_album)
VALUES('collection3', 2019);
""")
connection.execute("""INSERT INTO collection(name_album, year_album)
VALUES('collection4', 2021);
""")
connection.execute("""INSERT INTO collection(name_album, year_album)
VALUES('collection5', 2020);
""")
connection.execute("""INSERT INTO collection(name_album, year_album)
VALUES('collection6', 2019);
""")
connection.execute("""INSERT INTO collection(name_album, year_album)
VALUES('collection7', 2021);
""")
connection.execute("""INSERT INTO collection(name_album, year_album)
VALUES('collection8', 2020);
""")
connection.execute("""INSERT INTO track_collection(track_id, collection_id)
VALUES(1, 1);
""")
connection.execute("""INSERT INTO track_collection(track_id, collection_id)
VALUES(4, 2);
""")
connection.execute("""INSERT INTO track_collection(track_id, collection_id)
VALUES(2, 2);
""")
connection.execute("""INSERT INTO track_collection(track_id, collection_id)
VALUES(3, 2);
""")
connection.execute("""INSERT INTO track_collection(track_id, collection_id)
VALUES(5, 2);
""")
connection.execute("""INSERT INTO track_collection(track_id, collection_id)
VALUES(15, 3);
""")
