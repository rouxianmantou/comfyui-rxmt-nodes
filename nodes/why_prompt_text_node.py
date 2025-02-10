class WhyPromptTextNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "dynamicPrompts": True, "tooltip": "The text to be encoded."}), 
            }
        }
    RETURN_TYPES = ("TEXT",)
    
    FUNCTION = "execute"

    CATEGORY = "RXMT_Utility"

    def execute(self, text):
        return (text, )