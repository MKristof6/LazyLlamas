ALTER TABLE IF EXISTS ONLY public.student
    DROP CONSTRAINT IF EXISTS fk_languages CASCADE,
    DROP CONSTRAINT IF EXISTS fk_language_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_pair_solution CASCADE;
ALTER TABLE IF EXISTS ONLY public.feedback
    DROP CONSTRAINT IF EXISTS fk_multiple_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_amigo_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_student_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_one_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_memory_game_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.solution
    DROP CONSTRAINT IF EXISTS fk_multiple_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_student_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_one_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_memory_game_completion_time CASCADE;

DROP TABLE IF EXISTS public.amigo;
DROP TABLE IF EXISTS public.student;
DROP TABLE IF EXISTS public.pair_solution;
DROP TABLE IF EXISTS public.solution;
DROP TABLE IF EXISTS public.feedback;
DROP TABLE IF EXISTS public.student_languages;
DROP TABLE IF EXISTS public.language;
DROP TABLE IF EXISTS public.one_answer_question;
DROP TABLE IF EXISTS public.multiple_answer_question;
DROP TABLE IF EXISTS public.word_pair;
DROP TABLE IF EXISTS public.one_answer_answer;
DROP TABLE IF EXISTS public.multiple_answer_answer;
DROP TABLE IF EXISTS public.memory_game;
DROP TABLE IF EXISTS public.matching_exercise;
DROP TABLE IF EXISTS public.memory_game_solution;


CREATE TABLE amigo
(
    id       INT GENERATED ALWAYS AS IDENTITY,
    "name"   VARCHAR(50) NOT NULL,
    email    VARCHAR(50) NOT NULL UNIQUE,
    password TEXT        NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE student
(
    id          INT GENERATED ALWAYS AS IDENTITY,
    "name"      VARCHAR(50) NOT NULL,
    email       VARCHAR(50) NOT NULL UNIQUE,
    password    TEXT        NOT NULL,
    birthday    DATE,
    points      INT,
    PRIMARY KEY (id)
);


CREATE TABLE solution
(
    id                          INT GENERATED ALWAYS AS IDENTITY,
    one_answer_question_id      INT,
    multiple_answer_question_id INT,
    student_id                  INT,
    student_answer              INT,
    memory_game_completion_time INT,
    PRIMARY KEY (id)
);

CREATE TABLE feedback
(
    id                          INT,
    amigo_id                  INT,
    student_id                  INT,
    feedback                    text,
    one_answer_question_id      INT,
    multiple_answer_question_id INT,
    memory_game_id              INT
);


CREATE TABLE language
(
    id   INT GENERATED ALWAYS AS IDENTITY,
    name text,
    PRIMARY KEY (id)
);


CREATE TABLE student_languages
(
    id          INT GENERATED ALWAYS AS IDENTITY,
    student_id  INT,
    language_id INT,
    PRIMARY KEY (id)
);


CREATE TABLE pair_solution
(
    question_id  INT,
    student_id   INT UNIQUE,
    foreign_text text,
    hun_text     text
);

CREATE TABLE one_answer_question
(
    id   INT GENERATED ALWAYS AS IDENTITY,
    text text,
    PRIMARY KEY (id)
);

CREATE TABLE multiple_answer_question
(
    id   INT GENERATED ALWAYS AS IDENTITY,
    text text,
    PRIMARY KEY (id)
);

CREATE TABLE word_pair
(
    id           INT GENERATED ALWAYS AS IDENTITY,
    foreign_word text,
    hun_word     text,
    question_id  INT,
    PRIMARY KEY (id)
);

CREATE TABLE one_answer_answer
(
    id          INT GENERATED ALWAYS AS IDENTITY,
    text        text,
    question_id INT,
    PRIMARY KEY (id)
);

CREATE TABLE multiple_answer_answer
(
    id          INT GENERATED ALWAYS AS IDENTITY,
    text        text,
    question_id INT,
    correct     BOOLEAN,
    PRIMARY KEY (id)
);
    

CREATE TABLE matching_exercise
(
    id     serial
        constraint matching_exercise_pk
            primary key,
    theme text not null,
    word1  text not null,
    image1 text not null,
    word2  text not null,
    image2 text not null,
    word3  text not null,
    image3 text not null,
    word4  text not null,
    image4 text not null,
    word5  text not null,
    image5 text not null,
    word6  text not null,
    image6 text not null
);


CREATE TABLE memory_game
(
    id        INT GENERATED ALWAYS AS IDENTITY,
    theme     text NOT NULL,
    image1 VARCHAR,
    text1     text,
    image2 VARCHAR,
    text2     text,
    image3 VARCHAR,
    text3     text,
    image4 VARCHAR,
    text4     text,
    image5 VARCHAR,
    text5     text,
    image6 VARCHAR,
    text6     text,
    PRIMARY KEY (id)
);

CREATE TABLE memory_game_solution
(
    id        INT GENERATED ALWAYS AS IDENTITY,
    student_id INT,
    game_id INT,
    solution_time INT
);

INSERT INTO memory_game(theme, filename1, text1, filename2, text2, filename3, text3, filename4, text4, filename5, text5, filename6, text6)
VALUES ('animals','../static/images/memory_sample/cat.png', 'cat', '../static/images/memory_sample/dolphin.png', 'dolphin', '../static/images/memory_sample/fox.png', 'fox', '../static/images/memory_sample/horse.png', 'horse', '../static/images/memory_sample/owl.png', 'owl', '../static/images/memory_sample/wolf.png', 'wolf' );

INSERT INTO language(name) VALUES ('English');
INSERT INTO language(name) VALUES ('Français');
INSERT INTO language(name) VALUES ('Italiano');
INSERT INTO language(name) VALUES ('Español');
INSERT INTO amigo (name, email, password) VALUES ('balintovics', 'molnar99b@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu');
INSERT INTO student (name, email, password, birthday, points) VALUES ('Zsófi', 'zsofiaszonja.kassai@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu', '1969.06.09.', 33);
INSERT INTO student (name, email, password, birthday, points) VALUES ('Kristóf', 'kristof.murai@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu', '1969.06.09.', 2344);
INSERT INTO student (name, email, password, birthday, points) VALUES ('Barna', 'barna.urmossy@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu', '1969.06.09.', 233);
INSERT INTO student_languages (student_id, language_id) VALUES (1, 1 );
INSERT INTO student_languages (student_id, language_id) VALUES (1, 2 );
INSERT INTO student_languages (student_id, language_id) VALUES (2, 1 );
INSERT INTO student_languages (student_id, language_id) VALUES (2, 2 );
INSERT INTO student_languages (student_id, language_id) VALUES (3, 1 );
INSERT INTO student_languages (student_id, language_id) VALUES (3, 2 );


ALTER TABLE ONLY public.feedback
    ADD CONSTRAINT fk_multiple_answer_question_id FOREIGN KEY (multiple_answer_question_id) REFERENCES multiple_answer_question (id),
    ADD CONSTRAINT fk_amigo_id FOREIGN KEY (amigo_id) REFERENCES amigo (id),
    ADD CONSTRAINT fk_student_id FOREIGN KEY (student_id) REFERENCES student (id),
    ADD CONSTRAINT fk_one_answer_question_id FOREIGN KEY (one_answer_question_id) REFERENCES one_answer_question (id),
    ADD CONSTRAINT fk_memory_game_id FOREIGN KEY (memory_game_id) REFERENCES memory_game (id);

ALTER TABLE ONLY public.solution
    ADD CONSTRAINT fk_multiple_answer_question_id FOREIGN KEY (multiple_answer_question_id) REFERENCES multiple_answer_question (id),
    ADD CONSTRAINT fk_student_id FOREIGN KEY (student_id) REFERENCES student (id),
    ADD CONSTRAINT fk_one_answer_question_id FOREIGN KEY (one_answer_question_id) REFERENCES one_answer_question (id);

ALTER TABLE public.student
--  ADD CONSTRAINT fk_language_id FOREIGN KEY (language_id) REFERENCES language (id),
    ADD CONSTRAINT fk_pair_solution FOREIGN KEY (id) REFERENCES pair_solution (student_id);



