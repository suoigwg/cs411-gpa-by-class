drop table if exists Grade;
drop table if exists Course;
create table Course
(
    subject varchar(10),
    number int,
    title varchar(100) not null,
    primary key (subject, number)
);

create table Grade
(
    subject varchar(10),
    number int,
    year int,
    gpa real,
    term varchar(10),
    class_size int,
    prof_name varchar(100) UNIQUE,
    check (gpa >= 0 and gpa <= 4),
    check ( year >= 1970 ),
    check ( class_size >= 0 ),
    foreign key (subject) references Course (subject) on delete cascade on update cascade,
    foreign key (number) references Course (number) on delete cascade on update cascade,
    primary key (subject, number, year, term, prof_name)
);
