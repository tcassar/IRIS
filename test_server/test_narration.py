from unittest import TestCase
from server.image_process import ImageProcessor
from server.narration import Narrator


class MockImgp(ImageProcessor):
    def describe(self) -> dict | str:
        return {
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
        }


class TestNarrator(TestCase):
    def setUp(self) -> None:
        with open("./img/PXL_20230609_172701248.MP.jpg", "rb") as f:
            self.imgp = ImageProcessor(f.read())

        self.narrator = Narrator(self.imgp)

    def test__generate_av_desc(self):
        print(self.narrator._generate_av_desc())

    def test__get_av_audio(self):
        self.narrator._get_av_audio()

    # def test_narrate(self):
    #     self.narrator.narrate()
