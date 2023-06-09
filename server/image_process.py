import base64
from dataclasses import dataclass

@dataclass
class ImageProcessor:

    image: bytes

    @property
    def b64_encoding(self):
        """Takes in a binary image, returns a base64 encoding"""
        return base64.b64encode(self.image)
