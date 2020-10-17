#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Akshat Kumar  
# DATE CREATED: 09/02/2020                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import os

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    #Creating empty dictionary named results_dic
    results_dic=dict()
    pet_labels=[]
    
    #Determines number of items in dictionary
    items_in_dic=len(results_dic)
    print("\n Empty Dictionary results_dic-n items=",items_in_dic)
    
    #Creating a list of petlabels
    
    filenames=listdir("pet_images/")
    for image in filenames:
        
        if image.startswith('.')==False:
            
            #removing .jpg from image and keeping only the filename
            extension_removed=os.path.splitext(image)[0]
            
            low_pet_image=extension_removed.lower()
            word_list_pet_image=low_pet_image.split("_")
            
            pet_label=""
            
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_label+=word+" "
            
            pet_label=pet_label.strip()
            
            pet_labels.append(pet_label)
    
    #Adding new key value pairs only if the key already doesn't exist in the dictionary
    
    for i in range(0,len(filenames),1):
        if filenames[i] not in results_dic:
            results_dic[filenames[i]]=[pet_labels[i]]
        else:
            print("** Warning: Key=", filenames[i],"already exists in results_dic with value=",results_dic[filenames[i]])

    return results_dic
