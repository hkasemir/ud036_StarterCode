import fresh_tomatoes


class Movie():
    '''Class for basic movie information,
    including title, trailer, and box art'''
    def __init__(self, title, youtube_url, image_url):
        self.title = title
        self.trailer_youtube_url = youtube_url
        self.poster_image_url = image_url

