ALTER TABLE IF EXISTS ONLY public.feedback
    DROP CONSTRAINT IF EXISTS fk_multiple_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_teacher_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_student_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_one_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_memory_game_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.pair_solution
    DROP CONSTRAINT IF EXISTS fk_multiple_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_student_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_one_answer_question_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_memory_game_completion_time CASCADE;
ALTER TABLE IF EXISTS ONLY public.student
    DROP CONSTRAINT IF EXISTS fk_languages CASCADE,
    DROP CONSTRAINT IF EXISTS fk_language_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_pair_solution CASCADE;

DROP TABLE IF EXISTS public.student;
DROP TABLE IF EXISTS public.teacher;
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



CREATE TABLE teacher
(
    id       INT GENERATED ALWAYS AS IDENTITY,
    "name"   CHAR(50) NOT NULL,
    email    CHAR(50) NOT NULL,
    password text,
    PRIMARY KEY (id)
);


CREATE TABLE student
(
    id          INT GENERATED ALWAYS AS IDENTITY,
    "name"      CHAR NOT NULL,
    email       CHAR NOT NULL,
    password    text,
    birthday    DATE,
    points      INT,
    language_id INT,
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
    language_id INT UNIQUE,
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

CREATE TABLE memory_game
(
    id        INT GENERATED ALWAYS AS IDENTITY,
    filename1 text NOT NULL,
    text1     text,
    filename2 text NOT NULL,
    text2     text,
    filename3 text NOT NULL,
    text3     text,
    filename4 text NOT NULL,
    text5     text,
    filename5 text NOT NULL,
    text6     text,
    filename6 text NOT NULL,
    completion_time INT UNIQUE,
    PRIMARY KEY (id)
);


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
    ADD CONSTRAINT fk_language_id FOREIGN KEY (language_id) REFERENCES language (id),
    ADD CONSTRAINT fk_pair_solution FOREIGN KEY (id) REFERENCES pair_solution (student_id);

