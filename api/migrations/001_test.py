steps = [
    [
        """
        CREATE TABLE test (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL    
        )
        """,
        """
        DROP TABLE test
        """,
    ]
]
