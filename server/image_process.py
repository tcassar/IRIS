import base64
from dataclasses import dataclass
import json
import requests
import os


class PhotoDescriptionError(Exception): ...


@dataclass
class ImageProcessor:
    image: bytes
    max_results: int = 5

    @property
    def b64_encoding(self):
        """Takes in a binary image, returns a base64 encoding"""
        return base64.b64encode(self.image)

    @property
    def json(self):
        """Returns image as json body for request"""
        return {
                "requests": [
                    {
                        "image": {"content": str(self.b64_encoding, encoding='ascii')},
                        "features": [
                            {
                                "maxResults": self.max_results,
                                "type": "OBJECT_LOCALIZATION",
                            },
                        ],
                    }
                ]
            }


    @property
    def bearer_token(self):
        """Generate bearer token for gcloud api"""
        # TODO: do this properly via os.environ
        return os.system("gcloud auth print-access-token")

    def describe(self) -> str:
        """Uses Google Vision API to return a description of the scene.

        Vision API returns name, mid, score, bounds for each object.
            name - object name
            mid - ID in Google's knowledge graph
            score - likelihood of being classified object
            bounds - 4 corners (coordinates) of box containing object

        """

        response = requests.post("https://vision.googleapis.com/v1/images:annotate",
                                 json=self.json,
                                 headers={
                                     "Authorization": f"Bearer ya29.a0AWY7Cknbv2gPr_qh3ykWTlUzw3ppqxwomOuRz5jxAwuFmvriKm3iapdHSt0DQb0Hs_x7bQu8J_sEVo-uiG44iuTbTaxRNTAFP5KrxHdiyuzvEMCnFpTb0g-_LXquE37AKisf7DGzTDqalAWb7luAqrjpdU2TKQ3_48JQaCgYKASMSARMSFQG1tDrpdCWPkKdyF0Gw4opdjcC_Bg0171",
                                     "x-goog-user-project": "sunny-truth-389311",
                                     "Content-Type": "application/json; charset=utf-8",
                                    }
                                 )

        if response.status_code == 200:
            return response.json()

        else:
            raise PhotoDescriptionError(response.json())
