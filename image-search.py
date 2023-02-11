import os
from datetime import datetime
from PIL import Image
import shutil

def is_image(filename):
    image_extensions = [".jpeg", ".jpg", ".png", ".bmp", ".gif", ".tiff"]
    return any(filename.endswith(ext) for ext in image_extensions)

def get_image_files(dir_path, max_width, max_height):
    image_files = []
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                if is_image(file_path):
                    with Image.open(file_path) as img:
                        width, height = img.size
                        if width <= max_width and height <= max_height:
                            image_files.append(file_path)
            except:
                print(f'Failure for {file_path}')
    return image_files

if __name__ == "__main__":
    print('Enter the path of the directory to search i.e. C:/Users/[name]/Downloads')
    print('You will be prompted to enter the maximum width, then height (in px)')
    print('Matching files will be copied into a new folder, using the same folder structure as the directory searched.')
    print('---------------------------')


    file_path = input("Enter the directory to search -  ")
    
    max_width = int(input("Enter the maximum width: "))
    max_height = int(input("Enter the maximum height: "))

    
    #max_width = max_height = 200
    
    emotes_folder = os.path.join(file_path, "emotes")
    
    if not os.path.exists(emotes_folder):
        os.makedirs(emotes_folder)
        
    image_files = get_image_files(file_path, max_width, max_height)
    
    for image_file in image_files:
        relative_folder = os.path.relpath(os.path.dirname(image_file), file_path)
        destination_folder = os.path.join(emotes_folder, relative_folder)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        shutil.copy2(image_file, destination_folder)
        
    print(f"{len(image_files)} matching images copied to {emotes_folder}")
