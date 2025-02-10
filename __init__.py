from .nodes.node_check_value_type import CheckValueTypeNode
from .nodes.why_prompt_text_node import WhyPromptTextNode

NODE_CLASS_MAPPINGS = {
    "CheckValueTypeNode": CheckValueTypeNode,
    "WhyPromptTextNode": WhyPromptTextNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CheckValueTypeNode": "🏸 Check Value Type",
    "WhyPromptTextNode": "🏸 Why Prompt Text"
}
