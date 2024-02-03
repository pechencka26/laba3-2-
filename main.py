class Book:
    def init(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def str(self):
        return f"self.name by self.author"

    def repr(self):
        return f"self.class.name('self.name', 'self.author')"


class PaperBook(Book):
    def init(self, name, author, pages):
        super().init(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages should be a positive integer")
        self._pages = value

    def str(self):
        return f"super().str(), self.pages pages"

    def repr(self):
        return f"self.class.name('self.name', 'self.author', self.pages)"


class AudioBook(Book):
    def init(self, name, author, duration):
        super().init(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float) or value <= 0:
            raise ValueError("Duration should be a positive float")
        self._duration = value

    def str(self):
        return f"super().str(), self.duration hours"

    def repr(self):
        return f"self.class.name('self.name', 'self.author', self.duration)"
