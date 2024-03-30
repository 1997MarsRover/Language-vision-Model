from transformers import TextIteratorStreamer, AutoModelForCausalLM, CodeGenTokenizerFast as Tokenizer
from PIL import Image
import argparse
from PIL import Image
import logging
class Moon(object):
    """Small Multimodal Model."""
    def __init__(self):
        super(Moon, self).__init__()
        self.logger = logging.getLogger(__name__)
        self.model_id = "vikhyatk/moondream1"
        self.model = AutoModelForCausalLM.from_pretrained(self.model_id, trust_remote_code=True)
        self.tokenizer = Tokenizer.from_pretrained(self.model_id)
        self.parser = argparse.ArgumentParser()
        

    def main(self, text):
        self.parser.add_argument("--image", type=str, required=True)
        self.parser.add_argument("--interactive", action="store_true")
        args = self.parser.parse_args()

        image = Image.open(args.image)
        self.logger.info
        enc_image = self.model.encode_image(image)

        if args.interactive:
            while True:
                print(self.model.answer_question(enc_image, "<QUESTION>", self.tokenizer))
