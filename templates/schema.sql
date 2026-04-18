-- =====================================
-- PARTICIPANTS
-- =====================================
CREATE TABLE IF NOT EXISTS participants (
    participant_id INTEGER PRIMARY KEY,
    participant_name TEXT NOT NULL UNIQUE,
    has_paid BOOLEAN DEFAULT 0
);

-- =====================================
-- MATCHES
-- =====================================
CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY,
    group_name TEXT,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    home_goals INTEGER,
    away_goals INTEGER
    outcome TEXT
);

-- =====================================
-- PREDICTIONS
-- =====================================
CREATE TABLE IF NOT EXISTS predictions (
    prediction_id INTEGER PRIMARY KEY,
    participant_id INTEGER NOT NULL,
    match_id INTEGER NOT NULL,
    home_goals INTEGER,
    away_goals INTEGER,
    prediction_outcome TEXT,

    FOREIGN KEY (participant_id) REFERENCES participants(participant_id),
    FOREIGN KEY (match_id) REFERENCES matches(match_id),

    UNIQUE (participant_id, match_id)
);