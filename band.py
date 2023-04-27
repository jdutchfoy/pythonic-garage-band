class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return "instrument"


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def play_solo(self):
        return "face-melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def play_solo(self):
        return "bass solo"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)

    def play_solo(self):
        return "drum solo"


class Band:
    _all_bands = []

    def __init__(self, name):
        self.name = name
        self.members = []
        self.__class__._all_bands.append(self)

    def add_member(self, member):
        self.members.append(member)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}"

    @classmethod
    def to_list(cls):
        return cls._all_bands
