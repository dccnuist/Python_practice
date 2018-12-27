import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        formatted_name = get_formatted_name('dcc', 'sky')
        self.assertEqual(formatted_name, 'Dcc Sky')


unittest.main()
