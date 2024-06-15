from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

class DescribeImage:
    def __init__(self):
        # initialize any variables or resources here
        pass

    def invoke(self, image_path):
        try:
            # Analyze the image
            # image_path = '/Users/rishimadhok/Desktop/aircraft_carrier.png'
            description = _describe_image(image_path)
            
            return description

        except Exception as e:
            # Print error message if an exception occurs
            print(f"An error occurred while describing the image: {e}")
            return None

def _describe_image(image_path):
    """
    Generates a textual description of an image using the Moondream2 model.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The textual description of the image.
    """
    # Load the Moondream2 model
    model_id = "vikhyatk/moondream2"
    revision = "2024-05-20"
    model = AutoModelForCausalLM.from_pretrained(
        model_id, trust_remote_code=True, revision=revision
    )

    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

    # Open the image
    image = Image.open(image_path)

    # Encode the image
    enc_image = model.encode_image(image)

    # Generate the textual description of the image
    description = model.answer_question(enc_image, "Describe this image.", tokenizer)

    return description

