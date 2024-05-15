from typing import Optional

from .image import Image


class EnhancedString:
    content: str = ""

    images: list[Image]

    def __init__(self, content: str):
        self.content = content
        self.images = []

    def add_image(self, uri: str, caption: Optional[str] = None):
        self.images.append(Image(uri, caption))

    def append_content(self, content: str):
        if self.content != "":
            self.content += "\n"
        self.content += content

    def __dict__(self):
        result: dict[str, str | list[dict]] = {"content": self.content}
        if self.images:
            result["images"] = []
            for img in self.images:
                result["images"].append(img.__dict__())
        return result
