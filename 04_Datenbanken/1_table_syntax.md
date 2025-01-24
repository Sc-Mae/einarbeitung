CREATE DATABASE einarbeitung_dateiformate;


einarbeitung_dateiformate;

CREATE TABLE squad (
    sid INT AUTO_INCREMENT PRIMARY KEY,
    SquadName VARCHAR(255),
    HomeTown VARCHAR(255),
    formed INT,
    position VARCHAR(255),
    SecretBase VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE member (
    mid INT AUTO_INCREMENT PRIMARY KEY,
    sid INT,
    name VARCHAR(255),
    age INT,
    SecretIdentity VARCHAR(255),
    FOREIGN KEY (mid) REFERENCES squad(sid)
);

CREATE TABLE power (
    pid INT AUTO_INCREMENT PRIMARY KEY,
    mid INT,
    power VARCHAR(255),
    FOREIGN KEY (pid) REFERENCES member(mid)
);