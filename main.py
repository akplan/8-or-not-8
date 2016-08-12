# Assignment 4: Perceptron


# reads an image file.
def read_image_file(filename):

    return


# returns the sums of weights of an image.
def sum_of_weights(image):

    return


# Copying down the pseudo-code from the pdf
weights [ HEIGHT * WIDTH + 1] = 0
#The learning rate is a parameter
LEARNING_RATE = 0.1
#The bias is a parameter.
#MAX_ITERATIONS is a parameter.
epoch = 0

while epoch++ < MAX_ITERATIONS:
    for i = 0; i < TRAINING_SIZE; ++i:
        img_array = read_image_file(i)
        label = read_label(i)

        #multiply weights with pixel values.
        #for all p, sum = sum + weight[p]*img_array[p]
        #If sum > 0, output = +1, ie. +ve detection
        #else output = -1, ie. -ve detection
        output = sum_of_weights(img_array)
        #We are trying to train for 8
        if label == 8:
            actual_output = 1
        else:
            actual_output = -1

        ERROR = actual_output - output
        #For every weight index, p,
        #weight[p] = weight[p] + LEARNING_RATE  img_array[p] * ERROR
        update_weights(img_array,ERROR)

#EVALUATION
FILENAME = user_input()
test_img = read_image_file(FILENAME)
output = sum_of_weights (test_img)
