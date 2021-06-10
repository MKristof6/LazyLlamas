ALTER TABLE IF EXISTS ONLY public.student
    DROP CONSTRAINT IF EXISTS fk_languages CASCADE,
    DROP CONSTRAINT IF EXISTS fk_language_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_pair_solution CASCADE;
ALTER TABLE IF EXISTS ONLY public.feedback
    DROP CONSTRAINT IF EXISTS fk_multiple_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_teacher_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_student_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_one_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_memory_game_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.solution
    DROP CONSTRAINT IF EXISTS fk_multiple_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_student_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_one_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_memory_game_completion_time CASCADE;

DROP TABLE IF EXISTS public.teacher;
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
DROP TABLE IF EXISTS public.listening_game;
DROP TABLE IF EXISTS public.listening_game_possibilities;

DROP TABLE IF EXISTS public.memory_game;



CREATE TABLE teacher
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
    language_id INT[],
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
    teacher_id                  INT,
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
    student_id  INT UNIQUE,
    language_id INT[],
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





DROP TABLE IF EXISTS listening_cards;
DROP TABLE IF EXISTS public.listening_game_answer;
DROP TABLE IF EXISTS public.listening_game_possibilities;

CREATE TABLE listening_game_answer
(
    id     INT GENERATED ALWAYS AS IDENTITY,
    answer text,
    PRIMARY KEY (id)
);


CREATE TABLE listening_cards
(
    id             INT GENERATED ALWAYS AS IDENTITY,
    task_id      INT NOT NULL ,
    PRIMARY KEY (id)
);

CREATE TABLE listening_game_possibilities
(
    id          INT GENERATED ALWAYS AS IDENTITY,
    card_id     INT,
    possibility text,
    PRIMARY KEY (id)
);


ALTER TABLE listening_cards
    ADD CONSTRAINT fk_answers FOREIGN KEY (id) REFERENCES listening_game_answer(id);

ALTER TABLE listening_cards
    ADD CONSTRAINT fk_possibility FOREIGN KEY (id) REFERENCES listening_game_possibilities(id);










CREATE TABLE memory_game
(
    id              INT GENERATED ALWAYS AS IDENTITY,
    filename1       text NOT NULL,
    text1           text,
    filename2       text NOT NULL,
    text2           text,
    filename3       text NOT NULL,
    text3           text,
    filename4       text NOT NULL,
    text5           text,
    filename5       text NOT NULL,
    text6           text,
    filename6       text NOT NULL,
    completion_time INT UNIQUE,
    PRIMARY KEY (id)
);

INSERT INTO language(name)
VALUES ('English');
INSERT INTO language(name)
VALUES ('French');
INSERT INTO language(name)
VALUES ('Italian');
INSERT INTO language(name)
VALUES ('Spanish');
INSERT INTO teacher (name, email, password)
VALUES ('balintovics', 'molnar99b@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu');
INSERT INTO student (name, email, password, birthday, language_id)
VALUES ('Zsófi', 'zsofiaszonja.kassai@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu',
        '1969.06.09.', ARRAY [1, 2]);
INSERT INTO student_languages (student_id, language_id)
VALUES (1, ARRAY [1, 2]);
INSERT INTO student (name, email, password, birthday, language_id)
VALUES ('Kristóf', 'kristof.murai@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu',
        '1969.06.09.', ARRAY [1, 2]);
INSERT INTO student_languages (student_id, language_id)
VALUES (2, ARRAY [1, 2]);
INSERT INTO student (name, email, password, birthday, language_id)
VALUES ('Barna', 'barna.urmossy@gmail.com', '$2b$12$N/XIozKGAVxNZGqDpa.IW.pi1JYdlXguyTyKmXekvjel.5GC6uRpu',
        '1969.06.09.', ARRAY [1, 2]);
INSERT INTO student_languages (student_id, language_id)
VALUES (3, ARRAY [1, 2]);

ALTER TABLE ONLY public.feedback
    ADD CONSTRAINT fk_multiple_answer_question_id FOREIGN KEY (multiple_answer_question_id) REFERENCES multiple_answer_question (id),
    ADD CONSTRAINT fk_teacher_id FOREIGN KEY (teacher_id) REFERENCES teacher (id),
    ADD CONSTRAINT fk_student_id FOREIGN KEY (student_id) REFERENCES student (id),
    ADD CONSTRAINT fk_one_answer_question_id FOREIGN KEY (one_answer_question_id) REFERENCES one_answer_question (id),
    ADD CONSTRAINT fk_memory_game_id FOREIGN KEY (memory_game_id) REFERENCES memory_game (id);

ALTER TABLE ONLY public.solution
    ADD CONSTRAINT fk_multiple_answer_question_id FOREIGN KEY (multiple_answer_question_id) REFERENCES multiple_answer_question (id),
    ADD CONSTRAINT fk_student_id FOREIGN KEY (student_id) REFERENCES student (id),
    ADD CONSTRAINT fk_one_answer_question_id FOREIGN KEY (one_answer_question_id) REFERENCES one_answer_question (id),
    ADD CONSTRAINT fk_memory_game_completion_time FOREIGN KEY (memory_game_completion_time) REFERENCES memory_game (completion_time);

ALTER TABLE public.student
    ADD CONSTRAINT fk_languages FOREIGN KEY (id) REFERENCES student_languages (student_id),
--     ADD CONSTRAINT fk_language_id FOREIGN KEY (language_id) REFERENCES language (id),
    ADD CONSTRAINT fk_pair_solution FOREIGN KEY (id) REFERENCES pair_solution (student_id);



