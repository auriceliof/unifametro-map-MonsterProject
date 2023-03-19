import cv2
import numpy as np
import os
import shutil

class ModelFactory:
    @staticmethod
    def imagesNormalizer(image_input_path, image_output_path):
        # Conta o numero de arquivos na pasta
        folder = image_input_path
        num_files = len(os.listdir(folder))

        # Carregar imagens
        images = []
        for i in range(num_files):
            image = cv2.imread('{}/{}.png'.format(image_input_path, i)) #lê a imagem

            #Se a imagem não for carregada
            if image is None:
                print('Não foi possível ler a imagem: {}/{}.png'.format(image_input_path, i))

            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converte a imagem para escala de cinza
            resized_image = cv2.resize(gray_image, (64, 128))   #Redimensiona a imagem
            images.append(resized_image) #adiciona a imagem redimensionada a lista images[]

        # Normalizar intensidade de cada pixel
        images = np.array(images) / 255.0

        # Armazenar as imagens pré-processadas
        for i in range(num_files):
            cv2.imwrite('{}/{}.png'.format(image_output_path, i), images[i] * 255)

factory = ModelFactory()

while True:
    input_images_folder_name = input("Write the folder name of the input images: ").lower()
    output_images_folder_name = input("Write the folder name of the output images: ").lower()
    shutil.rmtree(output_images_folder_name, ignore_errors=True)
    os.mkdir(output_images_folder_name)
    factory.imagesNormalizer(input_images_folder_name, output_images_folder_name)
    if input("Do you have another folder to normalize the image? (1-SIM/2-NÃO) >>> ")=='2':
        break