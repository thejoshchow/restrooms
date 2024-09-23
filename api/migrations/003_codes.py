steps = [
    [
        """
        CREATE TABLE codes (
            code_id SERIAL PRIMARY KEY,
            required BOOLEAN DEFAULT FALSE,
            date_added DATE DEFAULT CURRENT_DATE,
            last_updated DATE DEFAULT CURRENT_DATE,
            location_id INT REFERENCES locations(location_id) ON DELETE CASCADE,
            added_by INT REFERENCES accounts(account_id) ON DELETE RESTRICT

        )
        """,
        """
        DROP TABLE codes
        """,
    ]
]
