from .nodes.check_value_type import CheckValueTypeNode
from .nodes.why_prompt_text_node import WhyPromptTextNode
from .nodes.text_combine_with_comma import TextCombineWithCommaNode
from .nodes.convert_str_to_int import ConvertStrToIntNode

NODE_CLASS_MAPPINGS = {
    "CheckValueTypeNode": CheckValueTypeNode,
    "WhyPromptTextNode": WhyPromptTextNode,
    "TextCombineWithCommaNode": TextCombineWithCommaNode,
    "TextCombineWithCommaNode": TextCombineWithCommaNode,
    "ConvertStrToIntNode": ConvertStrToIntNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CheckValueTypeNode": "🏸:RXMT Check Value Type",
    "WhyPromptTextNode": "🏸:RXMT Why Prompt Text",
    "TextCombineWithCommaNode": "🏸:RXMT Text Combine with Comma",
    "ConvertStrToIntNode": "🏸:RXMT Convert Str to Int",
}
