from unittest import TestCase
from server.image_process import ImageProcessor

import base64


class TestImageProcess(TestCase):

    def test_b64_encoding(self):
        """Check that conversion of binary to base64 works"""
        with open('img/bicycle_original.jpeg', 'rb') as f:
            imgp = ImageProcessor(f.read())

        self.assertEqual(
            base64.b64encode(imgp.image), imgp.b64_encoding)

