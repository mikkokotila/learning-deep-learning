## learn more about keras at http://keras.io/ 
## learn more about numpy at http://www.numpy.org/

# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

# SECTION 3 - Create model
# learn about keras layers at https://keras.io/layers/about-keras-layers/
# learn about keras models at https://keras.io/models/about-keras-models/

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# SECTION 4 - Compile model
# learn about keras losses at https://keras.io/losses/
# learn about keras optimizers at https://keras.io/optimizers/
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# SECTION 5 - Fit the model
model.fit(X, Y, epochs=150, batch_size=10)

# SECTION 6 - Evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
