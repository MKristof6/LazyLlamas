ALTER TABLE IF EXISTS ONLY public.student
    DROP CONSTRAINT IF EXISTS fk_languages CASCADE,
    DROP CONSTRAINT IF EXISTS fk_language_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.feedback
    DROP CONSTRAINT IF EXISTS fk_amigo_id CASCADE,
    DROP CONSTRAINT IF EXISTS fk_student_id CASCADE;


DROP TABLE IF EXISTS public.amigo;
DROP TABLE IF EXISTS public.student;

DROP TABLE IF EXISTS public.solution;
DROP TABLE IF EXISTS public.feedback;

DROP TABLE IF EXISTS public.student_languages;
DROP TABLE IF EXISTS public.language;

DROP TABLE IF EXISTS public.memory_game;
DROP TABLE IF EXISTS public.sorting_game;
DROP TABLE IF EXISTS public.matching_game;
DROP TABLE IF EXISTS public.comprehensive_reading;
DROP TABLE IF EXISTS public.listening_game;

DROP TABLE IF EXISTS public.memory_game_solution;
DROP TABLE IF EXISTS public.matching_game_solution;
DROP TABLE IF EXISTS public.comprehensive_reading_solution;
DROP TABLE IF EXISTS public.listening_game_solution;

DROP TABLE IF EXISTS public.student_exercises;
DROP TABLE IF EXISTS public.exercise_type;


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

CREATE TABLE student_exercises
(
 id          INT GENERATED ALWAYS AS IDENTITY,
 student_id INT,
 game_id INT,
 game_type INT
);

CREATE TABLE exercise_type
(
    id  INT GENERATED ALWAYS AS IDENTITY,
    game_type text
);


CREATE TABLE feedback
(
    id                          INT,
    amigo_id                    INT,
    student_id                  INT,
    title                       text,
    feedback                    text
);


CREATE TABLE language
(
    id         INT GENERATED ALWAYS AS IDENTITY,
    name       text,
    voice_code text,
    PRIMARY KEY (id)
);


CREATE TABLE student_languages
(
    id          INT GENERATED ALWAYS AS IDENTITY,
    student_id  INT,
    language_id INT,
    PRIMARY KEY (id)
);


CREATE TABLE memory_game
(

    id     INT GENERATED ALWAYS AS IDENTITY,
    exercise_type INT DEFAULT 1,
    language text NOT NULL,
    theme  text NOT NULL,
    image1 VARCHAR,
    text1  text,
    image2 VARCHAR,
    text2  text,
    image3 VARCHAR,
    text3  text,
    image4 VARCHAR,
    text4  text,
    image5 VARCHAR,
    text5  text,
    image6 VARCHAR,
    text6  text,
    PRIMARY KEY (id)
);

CREATE TABLE sorting_game
(
    id     INT GENERATED ALWAYS AS IDENTITY,
    exercise_type INT DEFAULT 2,
    language text,
    theme text,
    categories    TEXT[],
    words  TEXT[],
    PRIMARY KEY (id)
);

    

CREATE TABLE matching_game
(
    id        INT GENERATED ALWAYS AS IDENTITY,
    exercise_type INT DEFAULT 3,
    language text not null,
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

CREATE TABLE comprehensive_reading(
    id     INT GENERATED ALWAYS AS IDENTITY,
    exercise_type INT DEFAULT 4,
    language text,
    theme text,
    long_text varchar(1000),
    questions text[]
);

CREATE TABLE listening_game
(
    id     INT GENERATED ALWAYS AS IDENTITY,
    exercise_type INT DEFAULT 5,
    game_id INT,
    language text,
    theme text,
    answers text[],
    correct_answer text,
    PRIMARY KEY (id)
);




CREATE TABLE memory_game_solution
(
    id            INT GENERATED ALWAYS AS IDENTITY,
    student_id    INT,
    game_id       INT,
    solution_time INT
);

CREATE TABLE matching_game_solution
(
    id        INT GENERATED ALWAYS AS IDENTITY,
    student_id INT,
    game_id INT,
    solution_time INT
);

CREATE TABLE comprehensive_reading_solution
(
    id            INT GENERATED ALWAYS AS IDENTITY,
    student_id    INT,
    game_id       INT,
    solution text[]
);


CREATE TABLE listening_game_solution
(
    id            INT GENERATED ALWAYS AS IDENTITY,
    student_id    INT,
    game_id       INT,
    solution text[]
);
