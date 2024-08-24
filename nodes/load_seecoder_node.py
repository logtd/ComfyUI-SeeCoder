import os

from safetensors.torch import load_file

from folder_paths import models_dir

from ..modules.seecoder import SemanticContextEncoder


SEECODER_PATH = os.path.join(models_dir, 'seecoder')
os.makedirs(SEECODER_PATH, exist_ok=True)


class LoadSeeCoderNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "checkpoint": (os.listdir(SEECODER_PATH), )}}

    RETURN_TYPES = ("SEECODER",)
    FUNCTION = "load"

    CATEGORY = "seecoder"

    def load(self, checkpoint):
        checkpoint_path = os.path.join(SEECODER_PATH, checkpoint)
        state_dict = load_file(checkpoint_path)
        cleaned_state_dict = {}
        has_pe =  False
        for key in state_dict.keys():
            cleaned_key = key.replace('ctx.image.', '')
            if 'pe_layer' in cleaned_key:
                has_pe = True
            cleaned_state_dict[cleaned_key] = state_dict[key]
        seecoder = SemanticContextEncoder(has_pe)
        seecoder.load_state_dict(cleaned_state_dict)
        return (seecoder,)