import m12_2
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.first = m12_2.Runner('Усэйн', 10)
        self.second = m12_2.Runner('Андрей', 9)
        self.third = m12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        for x, all_value in self.all_results.items():
            list = {}
            for key, value in all_value.items():
                z = {key: value.name}
                list.update(z)
            print(list)

    def test_1(self):
        dist = m12_2.Tournament(90, self.first, self.third)
        self.distance = dist.start()
        self.all_results['Первый забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

    def test_2(self):
        dist = m12_2.Tournament(90, self.second, self.third)
        self.distance = dist.start()
        self.all_results['Второй забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

    def test_3(self):
        dist = m12_2.Tournament(90, self.first, self.second, self.third)
        self.distance = dist.start()
        self.all_results['Третий забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')