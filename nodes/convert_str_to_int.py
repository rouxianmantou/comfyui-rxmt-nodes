class ConvertStrToIntNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "default_val": ("INT", {"default": 0}),
                "str_number": ("STRING", {"default": "0"}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("output",)

    FUNCTION = "execute"
    CATEGORY = "RXMT_Utility"
    OUTPUT_NODE = True

    def execute(self, default_val, str_number):
        try:
            result = int(str_number)
        except (ValueError, TypeError):
            result = default_val
        return (result,)
