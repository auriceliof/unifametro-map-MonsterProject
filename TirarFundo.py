from rembg import remove
from PIL import Image
import os

folder = "imagens_capturadas"
num_files = len(os.listdir(folder))

for i in range(num_files):
    input_path = f"imagens_capturadas/{i}.jpg"
    output_path = f"imagens_sem_fundo/{i}.png"

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)