import os
from shutil import copyfile

def organize():
    images_dir = '/flickr_logos_27_dataset_images'
    training_images_dir = '/training_images'
    validation_images_dir = '/validation_images'
    training_annotations = os.listdir(os.getcwd()+'/training_labels')
    validation_annotations = os.listdir(os.getcwd()+'/validation_labels')
    cwd = os.getcwd()
    training_images = []
    validation_images = []
    for annot in training_annotations:
        temp = annot.rstrip('.txt')
        training_images.append(temp+'.jpg')
    for annot in validation_annotations:
        temp = annot.rstrip('.txt')
        validation_images.append(temp+'.jpg')
    print(len(training_images))
    print(len(validation_images))
    for image in training_images:
        copyfile(cwd+images_dir+'/'+image, cwd+training_images_dir+'/'+image)
    for image in validation_images:
        copyfile(cwd+images_dir+'/'+image, cwd+validation_images_dir+'/'+image)


if __name__ == '__main__':
    organize()
