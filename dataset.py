import os
import shutil 
import random
import subprocess

# Making Necessary directories

os.mkdir('images')
os.mkdir('labels')
os.mkdir('images/train')
os.mkdir('images/val')
os.mkdir('labels/train')
os.mkdir('labels/val')
os.mkdir('test')
os.mkdir('Dataset_images')
os.mkdir('Dataset_labels')

#Automation Starts

print("Welcome to your new Project!!")

#Extract Images from Video to create dataset

subprocess.run(["python", "vid2imgs.py"])
# Input to wait for user to complete labelling and then continue with the program
Usr_input = input("Are youready to train the model?[y/n]: ")
if Usr_input.lower() == 'y':
    # Shuffling dataset

    print("Shuffling dataset")
    image_files = os.listdir("Dataset_images")
    random.shuffle(image_files)
    print("Shuffling complete")
    
    # keeping count of how many images move to which folder

    length = len(os.listdir("Dataset_images"))
    images = [f for f in image_files]
    count = 0
    count_train = 0
    count_val = 0
    count_test = 0

    #Moving files
    for image in images:
        if count < (0.8*length):
            current_image_path = os.path.join("Dataset_images",image)
            shutil.move(current_image_path, "images/train")
            count += 1
            count_train = count
            
            
        elif count > (0.8*length) and count < (0.95*length):
            current_image_path = os.path.join("Dataset_images",image)
            shutil.move(current_image_path, "images/val")
            count += 1
            count_val =  count - count_train

        elif count > (0.95 * length):
            current_image_path = os.path.join("Dataset_images",image)
            shutil.move(current_image_path, "test")
            count += 1
            count_test = count - (count_val + count_train)

            
    print(f"Transfered {count_train} images to training folder")
    print(f"Transfered {count_val} images to validation folder")
    print(f"Transfered {count_test} images to testing folder")










