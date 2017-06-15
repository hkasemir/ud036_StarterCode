import media
import fresh_tomatoes

# a list of my favorite Movies instantiated using the Movie class from media
movies_list = [
        media.Movie(
            'Beauty and the Beast',
            'https://youtu.be/tRlzmyveDHE',
            'http://bit.ly/2s3yfMr'
        ),
        media.Movie(
            'Monty Python and the Holy Grail',
            'https://youtu.be/urRkGvhXc8w',
            'http://bit.ly/2sqUqfY'
        ),
        media.Movie(
            'Pirates of the Caribbean: the Curse of the Black Pearl',
            'https://youtu.be/naQr0uTrH_s',
            'http://bit.ly/2toMlFR'
        ),
        media.Movie(
            'The Jacket',
            'https://youtu.be/rCxQ83Pg1Ko',
            'http://bit.ly/2toC78D'
        ),
        media.Movie(
            '10 Things I Hate About You',
            'https://youtu.be/vpVZS5nTxh8',
            'http://bit.ly/2toQ729'
        ),
        media.Movie(
            'Star Wars: The Force Awakens',
            'https://youtu.be/sGbxmsDFVnE',
            'http://bit.ly/2rtIWZT'
        ),
    ]

fresh_tomatoes.open_movies_page(movies_list)

