from HERO import Hero
from HERO import monster
import unittest
class TestHero(unittest.TestCase):
    def test_init_hero(self):
        lisy = Hero(name = 'lisy', hp =100, ack = 10)
        self.assertEqual(lisy.hp, 100)
        self.assertEqual(lisy.ack, 10)
    def test_hero_ack(self):
        if lisy.ack > monster().ack:
            t = monster/(self.ack - monster().ack)
            return "击杀时间为{}".format(t)
        else:
            print(Hero().ack)
d = TestHero()
print(d.test_hero_ack())
unittest.main()
