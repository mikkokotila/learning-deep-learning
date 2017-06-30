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

### Assignment 4 - A more serious way to train models and saving it for later use

So far what you have been doing is learn about training a model. But when we train the model, there is a lot of bias for all kinds of reasons. 

1) Randomize the sample you have 
2) Split it in to two equally sized datasets (A and B)
3) Do what you already know how to do with dataset (A)

So far you had not implemented a validation split, so let's do that now: 

    model.fit(X, Y, validation_split=0.33, epochs=50, batch_size=15)

This will split your dataset (A) in to two different sets 'train' and 'test'. In this case 'train' will be 1/3 and then 2/3 will be reserved for testing the model. This will take place during each epoch. 

This is the standard way of doing things, but we will go a step further now. 

4) Now you will have to learn to save the model you've trained, so that it can be used later with different datasets (where the truth is no longer available). This is where things get applicable as opposed to just having something run on your own computer. After this you can take any data, train a model, validate the results, and then have that model applied on another system to make predictions from different data (where the variables are the same). 

You can do this by adding the following at the end of your code:

	model_json = model.to_json()
	with open("saved_model.json", "w") as json_file:
	    json_file.write(model_json)
	model.save_weights("saved_model_weights.h5")
	print("Model have been saved.")

5) Check that once you've trained your model, that you have the two new files, one is .h5 and one is .json. 

We'll continue in the next assignement. Keep the dataset 'B' ready, as we will use it to make predictions next. This is where the "training wheels" come on, now we're going to see how everything we've learn will work in an actual prediction challenge. 

### Assignement 5 - Tying it all together in to a custom function

What we've done so far: 

- ingest a dataset 
- train a model with the data
- improve the model through an iterative process 
- learn about the importance of 'test' 
- validate our results using a custom numpy code 
- save the model so we can use it for predictions later 

Before moving on the next step, which is making predictions when we don't have the truth dataset, we need to do some housekeeping. Most importantly, we need take all our code and create a python function out of it so we can call it conviniently from a single line command.

You can learn more about functions (just want you need to know for now) [here](http://www.pythonforbeginners.com/basics/python-functions).

Once your function working, don't just stop there but add some conviniences. For example it will be very useful if we can change batch_size and epochs parameters directly from the command. 

For that, you'll need a slightly more involving outline of the custom function feature in python. You can read it [here](https://www.tutorialspoint.com/python/python_functions.htm).

Go ahead and add any parameters that you know you want to frequently change directly in to your custom function so that you can in most cases run your model from a single-line command.

Creating a function of a code you've been working is a fundamental skill that you will use virtually every time you are working with Python. Learn it well from the start, and you'll have much more fun later. 

### Assignement 6 - Dealing with outputs with functions

As the first part of this assignement, let's take the result evaluation we created already, as an output in addition to the standard outputs from keras, let's show the comparison of what keras gives with our validated result.

Then in addition to that, we would want to know: 

- train accuracy 
- train loss
- test accuracy 
- test loss 

So in total now we have 5 outputs we want to print. Also you can stop showing everything else (hint: there is a parameter 'verbose' where you can change the outputs in keras). 

To make it more useful though, let's add a few more that gives us an indication of the 'stability' of our model. 

- (train accuracy - train loss) 
- (test accuracy - test loss) 
- (test accuracy - test loss) / (train accuracy - train loss) 

So now we have 8 outputs in total. Also make sure that you show them in some nice way. The very simple way is to just use print()to do it. You can learn about outputs [here](https://docs.python.org/3/tutorial/inputoutput.html).

### Assignment 7 - Commenting your code and making it in to a your own package

Great job getting so far! This next one will be very quick and easy for you, but very important also. It is about commenting your code. There are two ways to comment code in python. One is the normal way: 

    # your comment comes here 
    
And the other is the way you do with function specific comments: 

    def my_function(data)
    
    '''
    USAGE: my_function(mortality.csv)
    NOTE:  the outcome variable should be the last column in the dataset
    '''

Comments play several important roles in your code and being a programmer: 

- comments help you to come back to your code after being away for a while
- comments help you to use your code even you don't see it (function as a module)
- comments help others to start using and improve your code

But don't over do it. In Python there is something referred to as "the python way". Part of that is to write code that is so simple, that it is more or less evident even though there would be a minimal amount of comments in the code itself. But it's better to always comment at the function level, at least to provide one use example and some possible "gatchas" about usage. 

Now I will share with you one very cool thing about Python. Once you save your function in a file and save it with .py ending, you can import it just like you would import a package you have installed. This is very useful, as it means we can easily create our own packages. 

Go ahead and do that with your newly commented code, and make sure that you can import it and that it works ok.  

### Assignment 8 - Putting everything we've learn together in to one reusable solution.

Without even knowing it, you're fast becoming a Python pro, and actually you thought you were just learning deep learning ;)

Now let's create another function, this time for making predictions using saved model. You will need to have a couple of things to be able to do that: 

- a dataset which has the same features (X variables) as when you created the model
- the saved model structure in a .json file 
- the saved model weights in a .h5 file 

Just to make sure that everything works right, what you can do is just separate the output variable (Y) from the diabetes dataset and use it to validate your predictions once you get it from your loaded model. 

You can get the example code for doing it [here](https://github.com/mikkokotila/learning-deep-learning/blob/master/predict-with-saved-model.py).

### Assignement 9 - Using a saved model to make predictions on data without ground truth.

### Assignement 10 - Contiributing code to Github

### Assignment 11 - Deep learning when you have text data 

In this assignement you will learn how to handle cases where you just have one feature which is unstructured data (text) and you want to make predictions based on that. More details soon...
