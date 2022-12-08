import unittest
import pencil

class TestDegrade(unittest.TestCase):

    def test_degrade(self):
        result = Pencil(4)
        self.assertEquals(result, '4')

    def test_paper(self):
        result = Paper('Sea shells')
        self.assertEquals(result, 'Sea shells')

if __name__ == '__main__':
    unittest.main()