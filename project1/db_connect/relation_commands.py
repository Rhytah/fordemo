sqlcommands = (    
                              
                """
                CREATE TABLE IF NOT EXISTS users(
                    userid SERIAL ,
                    username VARCHAR (30)PRIMARY KEY,
                    password VARCHAR (10),
                    email VARCHAR (30)
                    )
                """,
                """
                CREATE TABLE IF NOT EXISTS books(
                    isbn VARCHAR PRIMARY KEY,
                    title VARCHAR,
                    author VARCHAR,
                    year BIGINT
                    )
                """,
                """
                CREATE TABLE IF NOT EXISTS reviews(book_title VARCHAR REFERENCES books(title),
                    reviewer VARCHAR REFERENCES users(username),
                    review_count INT,
                    average_score INT
                    )
                """
)