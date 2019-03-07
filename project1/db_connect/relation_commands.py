sqlcommands = (    
                              
                """
                CREATE TABLE IF NOT EXISTS users(
                    userid SERIAL PRIMARY KEY,
                    username VARCHAR (30) UNIQUE NOT NULL,
                    password VARCHAR NOT NULL,
                    email VARCHAR (30) UNIQUE NOT NULL
                    )
                """,
                """
                CREATE TABLE IF NOT EXISTS books(
                    bookid SERIAL PRIMARY KEY,
                    isbn VARCHAR UNIQUE,
                    title VARCHAR NOT NULL,
                    author VARCHAR NOT NULL,
                    year BIGINT
                    )
                """,
                """
                CREATE TABLE IF NOT EXISTS reviews(
                    reviewid SERIAL,
                    book_id INT REFERENCES books(bookid),
                    reviewer INT REFERENCES users(userid) NOT NULL,
                    review VARCHAR NOT NULL,
                    review_count INT NOT NULL,
                    average_score INT NOT NULL,
                    PRIMARY KEY (reviewid,book_id,reviewer)
                    )
                """
)