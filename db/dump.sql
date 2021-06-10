INSERT INTO teacher (name, email, password) VALUES ('balintovics', 'molnar99b@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu');
INSERT INTO student (name, email, password, birthday) VALUES ('Zsófi', 'zsofiaszonja.kassai@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu', '1969.06.09.');
INSERT INTO student (name, email, password, birthday) VALUES ('Kristóf', 'kristof.murai@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu', '1969.06.09.');
INSERT INTO student (name, email, password, birthday) VALUES ('Barna', 'barna.urmossy@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu', '1969.06.09.');

INSERT INTO listening_game_answer(  answer) VALUES ('Cat');
INSERT INTO listening_game_answer(  answer) VALUES ( 'Dog');
INSERT INTO listening_game_answer(  answer) VALUES ('Llama');
INSERT INTO listening_game_answer(  answer) VALUES ('Giraffe');
INSERT INTO listening_game_answer(  answer) VALUES ( 'Elephant');
INSERT INTO listening_game_answer(  answer) VALUES ( 'Lion');



INSERT INTO listening_game_possibilities(card_id, possibility) VALUES (1, 'Can');
INSERT INTO listening_game_possibilities(card_id, possibility) VALUES (1, 'Cat');
INSERT INTO listening_game_possibilities(card_id, possibility) VALUES (1, 'Cap');
INSERT INTO listening_game_possibilities(card_id, possibility) VALUES (2, 'dope');
INSERT INTO listening_game_possibilities(card_id, possibility) VALUES (2, 'dog');
INSERT INTO listening_game_possibilities(card_id, possibility) VALUES (2, 'dot');

INSERT INTO listening_cards( task_id ) VALUES (1);
INSERT INTO listening_cards(task_id)VALUES (2);



INSERT INTO language(name) VALUES ('English');
INSERT INTO language(name) VALUES ('French');
INSERT INTO language(name) VALUES ('Italian');
INSERT INTO language(name) VALUES ('Spanish');
