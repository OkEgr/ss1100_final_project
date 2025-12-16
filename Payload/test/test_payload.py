import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Moved the following from main() due to TestCase altering name and code note running
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from payload_script import (load_and_combine_bands,
                              convert_radiance_to_reflectance,
                              rescale_to_8bit)

class TestPayload(unittest.TestCase):

    def setUp(self):
        """Set up test data."""
        self.red_file = 'dummy_red.csv'
        self.green_file = 'dummy_green.csv'
        self.blue_file = 'dummy_blue.csv'

    def test_load_and_combine_bands(self):
        """Tests the loading and stacking of image bands."""
        image = load_and_combine_bands(self.red_file, self.green_file, self.blue_file)
        self.assertIsNotNone(image)
        self.assertEqual(image.shape, (2, 2, 3))
        # Check a pixel value to ensure correct stacking
        # Pixel (0,0) should be (0.1, 0.5, 0.9)
        np.testing.assert_array_almost_equal(image[0, 0], [0.1, 0.5, 0.9])

    def test_convert_radiance_to_reflectance(self):
        """Tests the radiance to reflectance conversion."""
        # R = k * L + b  (k=0.8, b=0.1)
        radiance_image = np.array([[[0.1, 0.5, 0.9]]]) # 1x1 pixel image
        reflectance = convert_radiance_to_reflectance(radiance_image)
        expected = np.array([[[0.18, 0.5, 0.82]]]) # (0.8*0.1+0.1, 0.8*0.5+0.1, 0.8*0.9+0.1)
        np.testing.assert_array_almost_equal(reflectance, expected)

    def test_rescale_to_8bit(self):
        """Tests the rescaling to 8-bit integers."""
        reflectance_image = np.array([0.0, 0.5, 1.0])
        rescaled = rescale_to_8bit(reflectance_image)
        expected = np.array([0, 127, 255]) # or 128 depending on rounding
        # Check if the values are close, allowing for rounding differences
        np.testing.assert_allclose(rescaled, expected, atol=1)
        self.assertEqual(rescaled.dtype, np.uint8)


if __name__ == '__main__':
    # Change directory to the test file's location to find the dummy CSVs
    unittest.main()
