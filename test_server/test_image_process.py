from unittest import TestCase
from server.image_process import ImageProcessor
import base64


class TestImageProcess(TestCase):
    def setUp(self) -> None:
        with open("img/bicycle_original.jpeg", "rb") as f:
            self.imgp = ImageProcessor(f.read())

    def test_b64_encoding(self):
        """Check that conversion of binary to base64 works"""
        self.assertEqual(base64.b64encode(self.imgp.image), self.imgp.b64_encoding)
        print(self.imgp.b64_encoding)
        print(type(self.imgp.b64_encoding))

    def test_describe(self):
        self.assertEqual(
            self.imgp.describe(),
            {
                "responses": [
                    {
                        "localizedObjectAnnotations": [
                            {
                                "mid": "/m/01bqk0",
                                "name": "Bicycle wheel",
                                "score": 0.9344855,
                                "boundingPoly": {
                                    "normalizedVertices": [
                                        {"x": 0.31457117, "y": 0.784883},
                                        {"x": 0.44048217, "y": 0.784883},
                                        {"x": 0.44048217, "y": 0.97049814},
                                        {"x": 0.31457117, "y": 0.97049814},
                                    ]
                                },
                            },
                            {
                                "mid": "/m/01bqk0",
                                "name": "Bicycle wheel",
                                "score": 0.9330148,
                                "boundingPoly": {
                                    "normalizedVertices": [
                                        {"x": 0.5049288, "y": 0.7552311},
                                        {"x": 0.62730235, "y": 0.7552311},
                                        {"x": 0.62730235, "y": 0.94430834},
                                        {"x": 0.5049288, "y": 0.94430834},
                                    ]
                                },
                            },
                            {
                                "mid": "/m/0199g",
                                "name": "Bicycle",
                                "score": 0.90417564,
                                "boundingPoly": {
                                    "normalizedVertices": [
                                        {"x": 0.31727585, "y": 0.6597069},
                                        {"x": 0.6291734, "y": 0.6597069},
                                        {"x": 0.6291734, "y": 0.96770996},
                                        {"x": 0.31727585, "y": 0.96770996},
                                    ]
                                },
                            },
                            {
                                "mid": "/m/06z37_",
                                "name": "Picture frame",
                                "score": 0.65698254,
                                "boundingPoly": {
                                    "normalizedVertices": [
                                        {"x": 0.7864568, "y": 0.16705626},
                                        {"x": 0.9639955, "y": 0.16705626},
                                        {"x": 0.9639955, "y": 0.31888378},
                                        {"x": 0.7864568, "y": 0.31888378},
                                    ]
                                },
                            },
                        ]
                    }
                ]
            },
        )
