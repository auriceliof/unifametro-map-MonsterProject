import cv2
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

images = []
labels = []

folder1 = "monster_sem_fundo-gray"
folder2 = "no_monster_sem_fundo-gray"

for i in range(51):
    image = cv2.imread(f'{folder1}/{i}.png')
    if image is None :
        print(f'Não foi possível abrir a imagem {i} da pasta monster,')
    images.append(image)
    labels.append(1)


for i in range(51):
    image = cv2.imread(f'{folder2}/{i}.png')
    if image is None :
        print(f'Não foi possível abrir a imagem {i} da pasta no_monster,')
    images.append(image)
    labels.append(0)

print(len(images))
print(len(labels))

x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size=0.2)

def extract_features(imagem):

   color_hist = cv2.calcHist([image], [0,1,2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
   color_hist = cv2.normalize(color_hist, color_hist).flatten()
   return color_hist

x_train_features = [extract_features(image) for image in x_train]
x_test_features = [extract_features(image) for image in x_test]

clf = SVC(kernel='linear', C=1000)

clf.fit(x_train_features, y_train)

acuracia = clf.score(x_test_features, y_test)

print(acuracia)

joblib.dump(clf, 'modelo_monster.joblib')