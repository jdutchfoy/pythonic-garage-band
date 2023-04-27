import unittest
from band import Band, Musician, Guitarist, Bassist, Drummer


class MusicianSubclassTest(unittest.TestCase):
    def test_musician_get_instrument(self):
        john = Musician("John")
        self.assertEqual(john.get_instrument(), "instrument")

    def test_musician_str_returns_name(self):
        john = Musician("John")
        self.assertEqual(str(john), "John")

    def test_musician_repr_includes_class_name_and_name(self):
        john = Musician("John")
        self.assertEqual(
            repr(john), "Musician instance. Name = John"
        )

    def test_guitarist_get_instrument(self):
        jimmy = Guitarist("Jimmy")
        self.assertEqual(jimmy.get_instrument(), "instrument")

    def test_guitarist_str_returns_name(self):
        jimmy = Guitarist("Jimmy")
        self.assertEqual(str(jimmy), "Jimmy")

    def test_guitarist_repr_includes_class_name_and_name(self):
        jimmy = Guitarist("Jimmy")
        self.assertEqual(
            repr(jimmy), "Guitarist instance. Name = Jimmy"
        )

    def test_bassist_get_instrument(self):
        john = Bassist("John")
        self.assertEqual(john.get_instrument(), "instrument")

    def test_bassist_str_returns_name(self):
        john = Bassist("John")
        self.assertEqual(str(john), "John")

    def test_bassist_repr_includes_class_name_and_name(self):
        john = Bassist("John")
        self.assertEqual(
            repr(john), "Bassist instance. Name = John"
        )

    def test_drummer_get_instrument(self):
        ringo = Drummer("Ringo")
        self.assertEqual(ringo.get_instrument(), "instrument")

    def test_drummer_str_returns_name(self):
        ringo = Drummer("Ringo")
        self.assertEqual(str(ringo), "Ringo")

    def test_drummer_repr_includes_class_name_and_name(self):
        ringo = Drummer("Ringo")
