INSERT INTO teacher (name, email, password) VALUES ('balintovics', 'molnar99b@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu');
INSERT INTO student (name, email, password, birthday) VALUES ('Zsófi', 'zsofiaszonja.kassai@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu', '1969.06.09.');
INSERT INTO student (name, email, password, birthday) VALUES ('Kristóf', 'kristof.murai@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu', '1969.06.09.');
INSERT INTO student (name, email, password, birthday) VALUES ('Barna', 'barna.urmossy@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu', '1969.06.09.');

INSERT INTO listening_game(id, card_id, answer) VALUES ( 1, 1, 'Cat');
INSERT INTO listening_game( id, card_id, answer) VALUES ( 1, 2, 'Dog');
INSERT INTO listening_game( id, card_id, answer) VALUES ( 1, 3, 'Llama');
INSERT INTO listening_game( id, card_id, answer) VALUES ( 1, 4, 'Giraffe');
INSERT INTO listening_game( id, card_id, answer) VALUES ( 1, 5, 'Elephant');
INSERT INTO listening_game( id, card_id, answer) VALUES ( 1, 6, 'Lion');
INSERT INTO listening_game_possibilities(id, card_id, possibilities) VALUES (1, 1, 'Can');
INSERT INTO listening_game_possibilities(id, card_id, possibilities) VALUES (1, 1, 'Cat');
INSERT INTO listening_game_possibilities(id, card_id, possibilities) VALUES (1, 1, 'Cap');

INSERT INTO language(name) VALUES ('English');
INSERT INTO language(name) VALUES ('French');
INSERT INTO language(name) VALUES ('Italian');
INSERT INTO language(name) VALUES ('Spanish');
