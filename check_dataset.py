import os

train_path = "dataset/crop_disease/train"
val_path = "dataset/crop_disease/val"

print("TRAIN DATA:")

for folder in os.listdir(train_path):
    path = os.path.join(train_path, folder)

    if os.path.isdir(path):
        print(folder, "=", len(os.listdir(path)), "images")


print("\nVALIDATION DATA:")

for folder in os.listdir(val_path):
    path = os.path.join(val_path, folder)

    if os.path.isdir(path):
        print(folder, "=", len(os.listdir(path)), "images")