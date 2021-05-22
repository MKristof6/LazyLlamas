DROP TABLE IF EXISTS teacher;
CREATE TABLE teacher(
    teacher_id INT GENERATED ALWAYS AS IDENTITY,
    "name" CHAR(50) NOT NULL,
    email CHAR(50) NOT NULL,
    password text,
    PRIMARY KEY(teacher_id)
);

DROP TABLE IF EXISTS student;
CREATE TABLE student(
    student_id INT GENERATED ALWAYS AS IDENTITY,
    "name" CHAR NOT NULL,
    email CHAR NOT NULL,
    password text,
    birthday DATE,
        PRIMARY KEY(student_id)
);

DROP TABLE IF EXISTS feedback;
CREATE TABLE feedback(
    question_id INT,
    teacher_id INT,
    student_id INT,
    feedback text,
        FOREIGN KEY(teacher_id)
        REFERENCES teacher(teacher_id),
        FOREIGN KEY(student_id)
        REFERENCES student(student_id)
);

DROP TABLE IF EXISTS solution;
CREATE TABLE solution(
    question_id INT,
    student_id INT,
    student_answer INT,
        FOREIGN KEY(student_id)
        REFERENCES student(student_id)
);

DROP TABLE IF EXISTS pair_solution;
CREATE TABLE pair_solution(
    question_id INT,
    student_id INT,
    foreign_text text,
    hun_text text,
        FOREIGN KEY(student_id)
        REFERENCES student(student_id)
);

DROP TABLE IF EXISTS one_answer_question;
CREATE TABLE one_answer_question(
    question_id INT GENERATED ALWAYS AS IDENTITY,
    text text,
    PRIMARY KEY(question_id)
);

DROP TABLE IF EXISTS multiple_answer_question;
CREATE TABLE multiple_answer_question(
    question_id INT GENERATED ALWAYS AS IDENTITY,
    text text,
    PRIMARY KEY(question_id)
);

DROP TABLE IF EXISTS word_pair;
CREATE TABLE word_pair(
    pair_id INT GENERATED ALWAYS AS IDENTITY,
    foreign_word text,
    hun_word text,
    question_id INT,
    PRIMARY KEY(pair_id)
);

DROP TABLE IF EXISTS one_answer_answer;
CREATE TABLE one_answer_answer(
    answer_id INT GENERATED ALWAYS AS IDENTITY,
    text text,
    question_id INT,
    PRIMARY KEY(answer_id)
);

DROP TABLE IF EXISTS multiple_answer_answer;
CREATE TABLE multiple_answer_answer(
    answer_id INT GENERATED ALWAYS AS IDENTITY,
    text text,
    question_id INT,
    correct BOOLEAN,
    PRIMARY KEY(answer_id)
);