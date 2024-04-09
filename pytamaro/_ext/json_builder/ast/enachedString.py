from typing import Optional


class EnhancedStr:
    content: str = ""

    images: list[tuple[str, str]] = []  # tuple( url: str, caption: str)

    def __init__(self, content: str):
        self.content = content

    def add_image(self, url: str, caption: str = ""):
        self.images.append((url, caption))
        self.content.join(f"< image = {len(self.images)} >")

    def __dict__(self):
        return {"content": self.content, "images": self.images}
