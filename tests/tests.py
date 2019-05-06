import unittest
import wave_operations.wave_operations as w_o


class Testing(unittest.TestCase):
    def test_freq_adapter(self):
        x = [1, 1, 1, 1, 3, 4, 5, 6, 1, 2, 3, 4, 0, 0, 0, 12]
        exp = [1,4.5,2.5,3]
        self.assertEqual(w_o.freq_adapter(3,x,12), exp)



if __name__ == '__main__':
    unittest.main()