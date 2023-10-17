-- SQLite
-- id = db.Column(db.Integer, primary_key=True)
--     name = db.Column(db.String(50), nullable=False)
--     comment = db.Column(db.String(500), nullable=False)
--     stars = db.Column(db.Integer, nullable=False)
--     date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

CREATE TABLE Review (
    id	INTEGER NOT NULL,
    name	TEXT NOT NULL,
    comment	TEXT NOT NULL,
    stars	INTEGER NOT NULL,
    date	DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id AUTOINCREMENT)
);


