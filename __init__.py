class Musician:
    def __init__(self, name): # name attribute
        self.name = name

    def __str__(self):  # musician object
        return f"{self.__class__.__name__} {self.name}"

    def __repr__(self):  # detailed string  Musician object
        return f"{self.__class__.__name__}({self.name!r})"

    def get_instrument(self):  # abstract method to get the musician's instrument
        raise NotImplementedError

    def play_solo(self):  # abstract method to play a solo
        raise NotImplementedError


class Guitarist(Musician):  # subclass of Musician
    def get_instrument(self):  # of abstract method in Musician
        return "guitar"

    def play_solo(self):  # of abstract method in Musician
        return "face-melting guitar solo"


class Bassist(Musician):  # subclass of Musician
    def get_instrument(self):  # of abstract method in Musician
        return "bass"

    def play_solo(self):  # of abstract method in Musician
        return "bass solo"


class Drummer(Musician):  # subclass of Musician
    def get_instrument(self):  # abstract method in Musician
        return "drums"

    def play_solo(self):  # abstract method in Musician
        return "drum solo"


class Band:
    all_bands = []  # class-level variable to keep track of all bands created

    def __init__(self, name):  # band with a name attribute
        self.name = name
        self.members = []  # empty list to hold the band 
        self.__class__.all_bands.append(self)  # add band to all_bands list

    def __str__(self):  # string of Band 
        return f"{self.name} ({len(self.members)} members)"

    def __repr__(self):  # detailed string of Band 
        return f"Band({self.name!r})"

    def play_solos(self):  # Maybe... method to ask each member to play a solo in order and return list of solos
        return [musician.play_solo() for musician in self.members]

    @classmethod
    def to_list(cls):  # Maybe....
        
        return cls.all_bands
