#!/bin/bash

IMAGE_PATH='ref_images'
IMAGE_NAME='weak.png'        
PATH_NAME=$IMAGE_PATH'/'$IMAGE_NAME

LANG='kor'
OUTPUT_NAME='weak.txt'
FILE_OUTPUT=$LANG'>'$OUTPUT_NAME


PRESERVE_SPACES=1




tesseract -c preserve_interword_spaces=$PRESERVE_SPACES $PATH_NAME stdout -l $LANG>$OUTPUT_NAME
    
