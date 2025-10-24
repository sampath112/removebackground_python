from rembg import remove 
from PIL import Image
import io   
# Load an image from file, remove its background, and save the result

input_path = 'input.jpg'
output_path = 'output.png'
input_image = Image.open(input_path)
output = remove(input_image)
output.save(output_path)

#pip install rembg 
#pip install onnxruntime 