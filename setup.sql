-- Create database table

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

-- Generate some dummy data

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