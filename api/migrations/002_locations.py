steps = [
    [
        """
        CREATE TABLE locations (
            location_id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            address VARCHAR(200) NOT NULL,
            latitude DECIMAL NOT NULL,
            longitude DECIMAL NOT NULL,
            added_by INT REFERENCES accounts(account_id) ON DELETE RESTRICT,
            date_added DATE DEFAULT CURRENT_DATE,
            last_updated DATE DEFAULT CURRENT_DATE
        )
        """,
        """
        DROP TABLE locations
        """,
    ]
]
