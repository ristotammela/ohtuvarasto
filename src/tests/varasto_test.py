import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_sallii_tasmalleen_vapaan_tilan_maaran(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.lisaa_varastoon(2)

        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_negatiivista_maaraa_ei_lisata_varastoon(self):
        self.varasto.lisaa_varastoon(4)

        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, 4)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_ei_ylita_varaston_tilavuutta(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.lisaa_varastoon(5)

        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_otto_palauttaa_nollan_eika_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(4)

        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 4)

    def test_otto_palauttaa_koko_saldon_jos_pyynto_on_liian_suuri(self):
        self.varasto.lisaa_varastoon(4)

        saatu_maara = self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(saatu_maara, 4)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_otto_tyhjentaa_varaston_kun_maara_on_tasmalleen_saldo(self):
        self.varasto.lisaa_varastoon(4)

        saatu_maara = self.varasto.ota_varastosta(4)

        self.assertAlmostEqual(saatu_maara, 4)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijono_esittaa_saldon_ja_vapaan_tilan(self):
        self.varasto.lisaa_varastoon(4)

        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")
