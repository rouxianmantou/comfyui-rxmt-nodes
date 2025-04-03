class TextCombineWithCommaNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "include_text_1": ("BOOLEAN", {"default": True}),
                "text_1": ("STRING", {"multiline": True}),
                "text_2": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    FUNCTION = "execute"
    CATEGORY = "RXMT_Utility"
    OUTPUT_NODE = True

    def execute(self, include_text_1, text_1, text_2):
        if include_text_1:
            return (f"{text_1}, {text_2}",)
        return (text_2,)
