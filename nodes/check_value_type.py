class CheckValueTypeNode:
    """
    A custom node for ComfyUI to check the type of the input value.

    Class methods
    -------------
    INPUT_TYPES (dict):
        Defines input parameters of the node.
    
    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tuple.
    FUNCTION (`str`):
        The name of the entry-point method.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {"input_data": ("*", {}), }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "RXMT_Utility"
    OUTPUT_NODE = True

    def execute(self, input_data):
        """
        Checks the type of the input data and returns it as a string.
        
        Parameters:
            input_data: The input data whose type needs to be checked.
        
        Returns:
            output_type (str): A string representing the type of the input data.
        """
        if input_data is None:
            return ("No Input",)
        output_type = str(type(input_data).__name__)
        return (output_type,)



