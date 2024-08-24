import os

import torch

from folder_paths import models_dir


SEECODER_PATH = os.path.join(models_dir, 'seecoder')
os.makedirs(SEECODER_PATH, exist_ok=True)


class LoadSeeCoderUncondNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "pth": (os.listdir(SEECODER_PATH), )}}

    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "load"

    CATEGORY = "seecoder"

    def load(self, pth):
        checkpoint_path = os.path.join(SEECODER_PATH, pth)
        conditioning = torch.load(checkpoint_path).unsqueeze(0)
        return ([[conditioning, {}]],)