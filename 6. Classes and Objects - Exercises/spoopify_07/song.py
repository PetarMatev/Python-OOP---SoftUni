class Song:
    def __init__(self, name: str, length: float, single: bool,):
        self.name = name
        self.length = length
        self.single = single

    # creating a method to return info
    def get_info(self):
        return f"{self.name} - {self.length}"
