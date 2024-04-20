from typing import Optional


class EnhancedStr:
    content: str = ""

    images: list[tuple[str, str]]  # tuple( uri: str, caption: str)

    def __init__(self, content: str):
        self.content = content
        self.images = []

    def add_image(self, uri: str, caption: str = ""):
        self.images.append((uri, caption))

    def append_content(self, content: str):
        if self.content != "":
            self.content += "\n"
        self.content += content

    def __dict__(self):
        result: dict[str, str | list[dict]] = {"content": self.content}
        if self.images:
            result["images"] = []
            for img in self.images:
                result["images"].append({'uri': img[0], 'caption': img[1]})
        return result
