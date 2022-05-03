DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS cart;
DROP TABLE IF EXISTS workout;
DROP TABLE IF EXISTS exercise;

CREATE TABLE user (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(25) not null,
    email varchar(50) not null,
    password varchar(25) not null,
    exerciseTime int not null default 0,
    exerciseSets int not null default 0,
    exerciseRest int not null default 0
);

CREATE TABLE cart (
    cartID int not null,
    userID int not null,
    exerciseID not null,
    muscleGroup varchar(20) not null,
    PRIMARY KEY (cartID),
    FOREIGN KEY (userID) REFERENCES user(userID),
    FOREIGN KEY (exerciseID) REFERENCES exercise(exerciseID),
    FOREIGN KEY (muscleGroup) REFERENCES exercise(muscleGroup)
);

CREATE TABLE workout (
    workoutID int not null,
    difficulty int not null,
    userRating int not null,
    workoutCompletion int not null,
    startDate date,
    completionDate date,
    PRIMARY KEY (workoutID)
);

CREATE TABLE exercise (
    exerciseID int not null,
    workoutID integer not null,
    muscleGroupID integer not null,
    exerciseName varchar(50) not null,
    exerciseLink varchar(200) not null,
    muscleGroup varchar(20) not null,
    exerciseDescription varchar(250) not null,
    PRIMARY KEY (exerciseID),
    FOREIGN KEY (workoutID) REFERENCES workout(workoutID)
);