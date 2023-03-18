from rembg import remove
from PIL import Image
import os

folder1 = "monster"
num_files1 = len(os.listdir(folder1))

folder2 = "no_monster"
num_files2 = len(os.listdir(folder2))

for i in range(num_files1):
    input_path = f"{folder1}/{i}.jpg"
    output_path = f"{folder1}_sem_fundo/{i}.png"

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)


for i in range(num_files2):
    input_path = f"{folder2}/{i}.jpg"
    output_path = f"{folder2}_sem_fundo/{i}.png"

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)