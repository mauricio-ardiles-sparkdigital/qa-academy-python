import unittest
import clase1


class MyTestCase(unittest.TestCase):
    def test_get_age_range_return_menor(self):
        self.assertEqual('menor', clase1.get_age_range(17))

    def test_get_age_range_return_mayor(self):
        self.assertEqual('mayor', clase1.get_age_range(18))

    def test_get_age_range_return_mayor_boundary_max_limit(self):
        self.assertEqual('mayor', clase1.get_age_range(64))

    def test_get_age_range_return_jubilado(self):
        self.assertEqual('jubilado', clase1.get_age_range(65))

    def test_get_age_range_return_jubilado_boundary_max_limit(self):
        self.assertEqual('jubilado', clase1.get_age_range(120))

    def test_get_age_range_return_cadaver(self):
        self.assertEqual('cadaver', clase1.get_age_range(121))

    def test_person_to_string_return_person_status(self):
        result = clase1.person_to_string('Mauricio', 'Ardiles', 'mayor')
        expected = 'Su nombre es: Mauricio Ardiles y usted es: mayor'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
