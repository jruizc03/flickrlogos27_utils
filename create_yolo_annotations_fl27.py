import os
import cv2

def get_class_index(class_name):
    classes=['Adidas','Apple','BMW','Citroen','Cocacola','DHL','Fedex','Ferrari','Ford','Google','HP','Heineken','Intel','McDonalds','Mini','Nbc','Nike','Pepsi','Porsche','Puma','RedBull','Sprite','Starbucks','Texaco','Unicef', 'Vodafone','Yahoo']
    counter = 0
    for name in classes:
        if(name==class_name):
            return counter
        counter+=1


def get_xcenter_normalized(x1, x2, img_width):
    box_width = get_width(x1, x2)
    x_center = x1+(box_width/2)
    x_center_norm = x_center/img_width
    return round(x_center_norm,6)


def get_ycenter_normalized(y1, y2, img_height):
    box_height = get_height(y1, y2)
    y_center = y1+(box_height/2)
    y_center_norm = y_center/img_height
    return round(y_center_norm,6)


def get_width(x1, x2):
    return x2-x1


def get_height(y1, y2):
    return y2-y1


def get_box_width_normalized(box_width, img_width):
    return round(box_width/img_width,6)


def get_box_height_normalized(box_height, img_height):
    return round(box_height/img_height,6)


def convert_training_annotations():
    training_labels_dir = '/training_labels'
    current_dir = os.getcwd()
    images_dir = '/flickr_logos_27_dataset_images'
    with open('train_annotations.txt','r') as infile:
        for line in infile:
            params = line.split(' ')
            image_filename = params[0]
            filename = params[0].rstrip('.jpg')+'.txt'
            class_index = get_class_index(params[1])
            img = cv2.imread(current_dir+images_dir+'/'+image_filename)
            img_height,img_width,channels = img.shape
            x1 = int(params[2])
            y1 = int(params[3])
            x2 = int(params[4])
            y2 = int(params[5])
            box_width = get_width(x1, x2)
            box_height = get_height(y1, y2)
            x_center = get_xcenter_normalized(x1, x2, img_width)
            y_center = get_ycenter_normalized(y1, y2, img_height)
            box_width_norm = get_box_width_normalized(box_width, img_width)
            box_height_norm = get_box_height_normalized(box_height, img_height)
            label_filename = current_dir+training_labels_dir+'/'+filename
            with open(label_filename, 'a') as label:
                label.write(str(class_index)+' '+str(x_center)+' '+str(y_center)+' '+str(box_width_norm)+' '+str(box_height_norm)+'\n')


def convert_validation_annotations():
    validation_labels_dir = '/validation_labels'
    current_dir = os.getcwd()
    images_dir = '/flickr_logos_27_dataset_images'
    with open('val_annotations.txt','r') as infile:
        for line in infile:
            params = line.split(' ')
            image_filename = params[0]
            filename = params[0].rstrip('.jpg')+'.txt'
            class_index = get_class_index(params[1])
            img = cv2.imread(current_dir+images_dir+'/'+image_filename)
            img_height,img_width,channels = img.shape
            x1 = int(params[2])
            y1 = int(params[3])
            x2 = int(params[4])
            y2 = int(params[5])
            box_width = get_width(x1, x2)
            box_height = get_height(y1, y2)
            x_center = get_xcenter_normalized(x1, x2, img_width)
            y_center = get_ycenter_normalized(y1, y2, img_height)
            box_width_norm = get_box_width_normalized(box_width, img_width)
            box_height_norm = get_box_height_normalized(box_height, img_height)
            label_filename = current_dir+validation_labels_dir+'/'+filename
            with open(label_filename, 'a') as label:
                label.write(str(class_index)+' '+str(x_center)+' '+str(y_center)+' '+str(box_width_norm)+' '+str(box_height_norm)+'\n')


if __name__ == '__main__':
    convert_training_annotations()
    convert_validation_annotations()

