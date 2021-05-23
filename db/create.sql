ALTER TABLE IF EXISTS ONLY public.feedback
    DROP CONSTRAINT IF EXISTS feedback_student_id_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.feedback
    DROP CONSTRAINT IF EXISTS feedback_teacher_id_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.pair_solution
    DROP CONSTRAINT IF EXISTS pair_solution_student_id_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.solution
    DROP CONSTRAINT IF EXISTS solution_student_id_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.student_languages
    DROP CONSTRAINT IF EXISTS student_languages_student_id_fkey CASCADE;

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
    one_answer_question_id      INT,
    multiple_answer_question_id INT,
    student_id                  INT,
    student_answer              INT,
    FOREIGN KEY (student_id)
        REFERENCES student (id)
);

CREATE TABLE feedback
(
    id                 INT,
    teacher_id                  INT,
    student_id                  INT,
    feedback                    text,
    one_answer_question_id      INT,
    multiple_answer_question_id INT,
    FOREIGN KEY (teacher_id)
        REFERENCES teacher (id),
    FOREIGN KEY (student_id)
        REFERENCES student (id)
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
    PRIMARY KEY (id),
    FOREIGN KEY (student_id)
        REFERENCES student (id),
    FOREIGN KEY (language_id)
        REFERENCES language (id)
);


CREATE TABLE pair_solution
(
    question_id  INT,
    student_id   INT,
    foreign_text text,
    hun_text     text,
    FOREIGN KEY (student_id)
        REFERENCES student (id)
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
ALTER TABLE ONLY feedback ADD CONSTRAINT fk_one_answer_question_id FOREIGN KEY (one_answer_question_id)
        REFERENCES one_answer_question (id);
ALTER TABLE ONLY solution ADD CONSTRAINT fk_one_answer_question_id FOREIGN KEY (one_answer_question_id)
        REFERENCES one_answer_question (id);

ALTER TABLE ONLY feedback ADD CONSTRAINT fk_multiple_answer_question_id FOREIGN KEY (multiple_answer_question_id)
        REFERENCES multiple_answer_question(id);
ALTER TABLE ONLY solution ADD CONSTRAINT fk_multiple_answer_question_id FOREIGN KEY (multiple_answer_question_id)
        REFERENCES multiple_answer_question (id);