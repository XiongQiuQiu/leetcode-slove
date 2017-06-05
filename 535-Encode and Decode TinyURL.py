class Codec:
    def __init__(self):
        self.__tiny_url = "http://tinyurl.com/"
        self.__alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        for _ in range(6):
            self.key.append(self.__alphabet[random.randint(0, len(self.__alphabet) - 1)])
        self.longUrl = longUrl
        return self.__tiny_url + ''.join(self.key)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.longUrl
