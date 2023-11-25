-- Create database table
-- "schema" or "table definitions"nshare this code for create table 
--                      to show what it can do or store

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

-- Generate some dummy data below with insert into task to test end points 

INSERT INTO task (
    summary,
    description
) VALUES (
    "walk the dog",
    "take the dog to the park for a nice walk"
),
(
    "Laundry",
    "do all the laundry"
),
(
    "finish homework",
    "Complete and finish all assignments before Sunday"
);