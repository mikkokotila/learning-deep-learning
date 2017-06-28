# Learning Deep Learning Assignements

### Assignement 1 - Introduction to Deep Learning

In your first assignment, you will deploy a neural network using a ready-made (and tested) example. 

You can find it [here](
http://machinelearningmastery.com/tutorial-first-neural-network-python-keras/)

You can find a cleaned up version of the code [here](https://github.com/mikkokotila/learning-deep-learning/blob/master/neural-net-with-keras.py) together with references to Keras manual also. After first running the model succesfully, you should use the manual as a reference to make sure you roughly understand what each line of code is doing. 

To be able to do that, you have to setup your Python environment with commands you can find [here](https://github.com/mikkokotila/learning-deep-learning/blob/master/create-python-env.sh).

### Assignment 2 - Find ways to improve your model 

In this assignement, you will continue from where you have started previously i.e. using the model to predict the Pima Indians diabetes cases. Your challenge is to make the result better than what you got in the first assignement. 

#### what will your learn

- how to improve your prediction 
- become more aware of the relationship between accuracy and loss
- get hands on with changing the structure of the neural net 
- gain experience with different losses, activations and optimizers

You can expriment with things like number of layers, adding different kinds of layers such as 'Dropout' layers, changing optimizer, activation, or loss, or any other thing you think that may make the model better. Don't change more than one thing at a time, as otherwise you might not know what is working and what is not.

It's a good idea to have the epoch number at where you start to get your current result, so you don't have to wait between each iteration. Once you have finished the assignement, you should be able to explain what type of things made the model better, and what made it worse.

And remember, as you have already learn from studying the supporting materials, if your accuracy goes up but your loss goes up too, that's not good. So you want your accuracy to go higher, and loss go lower. Then you know you are improving the current model. Even if the accuracy stays the same or becomes slightly lower, if loss becomes much lower, that is good also. 

#### tips and tricks

- each step when the result change, try to think why did it change
- reducing loss is sometimes better than improving accuracy (if your accuracy is ok, but loss is high)

### Assignment 3 - Putting it all together with predictions output and simple validation

Now that we have an idea of how accurate our model is, let's get the actual precictions out and then use Pandas to compare it with the actual data we have to make sure that our model is doing what it appars to do (e.g. if our accuracy is 82%, then by right for every 100 samples in the original dataset, we should have 18 errors in our predictions). 

Getting predictions from a Keras model is very simple: 

The first step is to get the actual predictions: 

    predictions = model.predict(X)
    
As you can see, this we do simply by invoking 'predict' on our model. We want to store it in a variable for convinience later, and also so we can convert it to 1 and 0 in the next step:

    rounded = [round(x[0]) for x in predictions]
    
Now after the model has run, we can call 'predictions' or 'rounded' and get the results. But also we can use this later for visualizing the results. 

The the next step is to take what we have in 'rounded' and compare it with 'Y' which is the actual results we have from the original dataset. The best way to do this is by using Numpy. Below you have an example code that will do the job, but make sure that you understand what each step does and why it's there. 

    import numpy as np 
    
    if len(Y) == len(rounded):
        
        accuracy = np.array(Y)==np.array(rounded)
        errors = np.count_nonzero(accuracy)
        print float(errors) / len(Y)
       
The number you get there, should be the actual acccuracy you are getting for your predictions :) 
      
EXTRA: If you have time, you can come up with another way to do the validation in Numpy as that will help you to learn a little bit more about Numpy. It is very powerful, and particularly useful when combined with something like Keras. 

Have fun! 

### Assignment 4 - A more serious way to train models

### Assignment 5 - A more serious way to valitate results 

### Assignement 6 - Contiributing code to Github

### Assignment 7 - Deep learning when you have text data 

In this assignement you will learn how to handle cases where you just have one feature which is unstructured data (text) and you want to make predictions based on that. More details soon...
