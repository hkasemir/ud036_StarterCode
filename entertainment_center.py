import media
import fresh_tomatoes

movies_list = [
        media.Movie(
            'Beauty and the Beast',
            'https://youtu.be/tRlzmyveDHE',
            'http://static.tvtropes.org/pmwiki/pub/images/beauty_beast_poster.jpg'
        ),
        media.Movie(
            'Monty Python and the Holy Grail',
            'https://youtu.be/urRkGvhXc8w',
            'http://gravillis.s3.amazonaws.com/wp-content/uploads/2013/11/Monty-Python-Holy-Grail-poster.jpg'
        ),
        media.Movie(
            'Pirates of the Caribbean: the Curse of the Black Pearl',
            'https://youtu.be/naQr0uTrH_s',
            'https://www.movieposter.com/posters/archive/main/11/MPW-5924'
        ),
        media.Movie(
            'The Jacket',
            'https://youtu.be/rCxQ83Pg1Ko',
            'http://ecx.images-amazon.com/images/I/51Fx5qbu36L._SX940_.jpg'
        ),
        media.Movie(
            '10 Things I Hate About You',
            'https://youtu.be/vpVZS5nTxh8',
            'https://ameliatcreativemedia.files.wordpress.com/2014/01/10thingsihateaboutyou.jpg'
        ),
        media.Movie(
            'Star Wars: The Force Awakens',
            'https://youtu.be/sGbxmsDFVnE',
            'https://originalvintagemovieposters.com/wp-content/uploads/2016/05/Force-Awakens-4900-Large-705x1024.jpg'
        ),
    ]

fresh_tomatoes.open_movies_page(movies_list)
