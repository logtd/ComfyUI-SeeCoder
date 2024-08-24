from .nodes.load_seecoder_node import LoadSeeCoderNode
from .nodes.seecoder_encode_node import SeecoderEncodeNode
from .nodes.load_seecoder_uncond_node import LoadSeeCoderUncondNode


NODE_CLASS_MAPPINGS = {
    'LoadSeeCoder': LoadSeeCoderNode,
    'SeecoderEncode': SeecoderEncodeNode,
    'LoadSeeCoderUncond': LoadSeeCoderUncondNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'LoadSeeCoder': 'Seecoder Load Model',
    'SeecoderEncode': 'Seecoder Encode Latent',
    'LoadSeeCoderUncond': 'Seecoder Load Uncond',
}
