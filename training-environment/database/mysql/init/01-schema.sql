
USE javacream;

CREATE TABLE IF NOT EXISTS Services (
    name VARCHAR(100) PRIMARY KEY,
    ipaddress VARCHAR(45) NOT NULL,
    port INT NOT NULL
);

INSERT INTO Services (name, ipaddress, port) VALUES
    ('web1',  '10.1.1.1', 8080),
    ('web2',  '10.1.1.2', 8080),
    ('db1',   '10.1.2.3', 5678),
    ('misc1', '10.1.2.4', 9876);
