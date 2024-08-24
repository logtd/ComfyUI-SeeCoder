import comfy.model_management


class SeecoderEncodeNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seecoder": ("SEECODER",),
                "image": ("IMAGE",),
            },
        }
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"
    CATEGORY = "seecoder"

    def encode(self, 
               seecoder, 
               image):
        
        intermediate_device = comfy.model_management.intermediate_device()
        torch_device = comfy.model_management.get_torch_device()
        
        seecoder.to(torch_device)
        # latent = latent_image['samples'].to(torch_device)
        embed = seecoder(image.permute(0,3,1,2).to(torch_device)).to(intermediate_device)
        seecoder.to(intermediate_device)

        return ([[embed, {}]], )