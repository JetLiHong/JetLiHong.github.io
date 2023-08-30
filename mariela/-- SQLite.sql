CREATE TABLE application (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ipfilter TEXT NOT NULL
);

INSERT INTO application (name, ipfilter) 
VALUES ("het verhaal van Nederland", "192.168.1.1");

INSERT INTO application (name, ipfilter) 
VALUES ("de slimste mens", "192.168.2.2");

