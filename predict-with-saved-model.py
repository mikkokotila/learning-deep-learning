from keras.models import model_from_json
import numpy
import os

# SECTION 1 - Load the model
# By now all of this should be pretty clear for you. 
# Still, check out the relevant Keras manual entry 
# https://keras.io/models/about-keras-models/

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
 
# SECTION 2 - Run the model on the dataset
# Once you see how the output is, youc an adjust it 
# so that it gives the same output as you get from
# your training function. 

loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

# That's it, it is a simple as that! 
