steps = [
    [
        """
        CREATE TABLE accounts (
            account_id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(200) UNIQUE NOT NULL, 
            hashed_password VARCHAR(200) NOT NULL
        )
        """,
        """
        DROP TABLE accounts
        """,
    ]
]
