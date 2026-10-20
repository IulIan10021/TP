import hashlib
import tempfile
import unittest
from pathlib import Path
from PIL import Image
from arsenal.forensics.decode import desfa, decodeaza_straturi, sparge_hash, sparge_xor
from forensics import grade_zecimale, tip_real
from stego import ascunde, dezvaluie


# Itemul 15
def test_base64():
    strat, date = desfa("U2FsdXQ=")
    assert strat == "base64"
    assert date == b"Salut"


class TestLaborator(unittest.TestCase):
    def test_base64(self):
        test_base64()

    def test_straturi(self):
        straturi, date = decodeaza_straturi("NTM1OTU3NTk=")
        self.assertEqual(straturi, ["base64", "hex", "base64"])
        self.assertEqual(date, b"I\x85\x98")
        self.assertEqual(decodeaza_straturi("Salut!"), ([], b"Salut!"))

    def test_url(self):
        self.assertEqual(desfa("%53%61%6C%75%74"), ("url", b"Salut"))

    def test_xor(self):
        clar = b"The secret message is FLAG{xor_demo}."
        rezultat = sparge_xor(bytes(c ^ 42 for c in clar))
        self.assertTrue(any(c["cheie"] == 42 and c["rezultat"] == clar.decode()
                            for c in rezultat))

    def test_hash(self):
        with tempfile.TemporaryDirectory() as folder:
            cale = Path(folder) / "wordlist.txt"
            cale.write_text("gresit\nstudent265\n")
            for nume in ("md5", "sha1", "sha256"):
                tinta = hashlib.new(nume, b"student265").hexdigest()
                self.assertEqual(sparge_hash(tinta, cale), (nume, "student265"))

    def test_stego(self):
        with tempfile.TemporaryDirectory() as folder:
            sursa = Path(folder) / "foto.png"
            tinta = Path(folder) / "stego.png"
            Image.new("RGB", (40, 40), (100, 120, 140)).save(sursa)
            ascunde(sursa, "Salut, țară! FLAG{test}", tinta)
            self.assertEqual(dezvaluie(tinta), "Salut, țară! FLAG{test}")
            self.assertEqual(tip_real(tinta), "png")
            with self.assertRaises(ValueError):
                ascunde(sursa, "a" * 1000, tinta)

    def test_gps(self):
        self.assertAlmostEqual(grade_zecimale((28, 30, 0), "W"), -28.5)


if __name__ == "__main__":
    unittest.main()
