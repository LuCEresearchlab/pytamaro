from typing import Optional


class Image:
    uri: str = ""

    caption: Optional[str]

    def __init__(self, uri: str, caption: Optional[str] = None):
        self.uri = uri
        self.caption = caption

    def __dict__(self):
        result: dict[str, str] = {"uri": self.uri}
        if self.caption:
            result["caption"] = self.caption
        return result
