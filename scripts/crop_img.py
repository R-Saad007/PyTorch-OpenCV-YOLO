import cv2 as cv
import os

train_img_path = r'/home/adlytic/datasets/Validation_Data/images/' # Path for all training images
train_label_path = r'/home/adlytic/datasets/Validation_Data/labels/' # Path for all training labels (annotations)
img_save_path = r'/home/adlytic/datasets/Validation_Data/crops/' # Path for saving the drawn BBox

# Function to crop images on bbox coordinates
def crop_img(train_img_path):
    train_images = sorted(os.listdir(train_img_path)) # All training images
    train_labels = sorted(os.listdir(train_label_path)) # All training labels
    counter = 0 # To store the number of crop images for naming convention
    for x in range(0, len(train_images)):
        # Read Image
        img = cv.imread(os.path.join(train_img_path, train_images[x]))
        dimension = img.shape # (height, width, depth)
        with open(os.path.join(train_label_path, train_labels[x]), 'r') as f:
            file_data = [line.strip() for line in f]
        # For each object detected
        for y in range(0,len(file_data)):
            box_coords = file_data[y].split(' ')
            # Converting all string elements to floating point
            box_coords = [float(element) for element in box_coords] 
            startx = int((box_coords[1]*dimension[1]) - ((box_coords[3]/2)*dimension[1]))
            starty = int((box_coords[2]*dimension[0]) - ((box_coords[4]/2)*dimension[0]))
            endx = int((box_coords[1]*dimension[1]) + ((box_coords[3]/2)*dimension[1]))
            endy = int((box_coords[2]*dimension[0]) + ((box_coords[4]/2)*dimension[0]))
            # Increment counter to show a successfull coordinate for cropping ahead
            counter += 1
            # Cropping an image
            cropped_image = img[starty:endy, startx:endx]
            # Saving cropped image
            cropped_img_path = os.path.join(img_save_path, f"{str(counter)}.jpg")
            cv.imwrite(cropped_img_path, cropped_image)
    print("Images Cropped!")

if __name__ == "__main__":
    crop_img(train_img_path=train_img_path)
