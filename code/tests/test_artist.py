import unittest
import os
import glob
from wcartist.artist import WCArtist

class TestWCArtist(unittest.TestCase):

    def test_render_image(self):
        # input: image path
        # output: png file
        image_path = './test.png'
        input_text = 'test test test'
        bc = 'red'
        num = 3
        output_name = 'test_test'
        wca = WCArtist(image_path, input_text, num, bc, output_name)
        wca.render_image()
        cwd = os.getcwd()
        actual = os.path.splitext(cwd + '/' + 'test_test.png')[-1].lower()
        expected = '.png'
        names = glob.glob('*.png')
        actual_name = ''
        expected_name = 'test_test.png'
        for name in names:
            if name == 'test_test.png':
                actual_name = name
        # print(actual)
        # print(actual_name)
        # check file extension
        self.assertEqual(expected, actual)
        # check file name
        self.assertEqual(expected_name, actual_name)

if __name__ == '__main__':
    unittest.main()
