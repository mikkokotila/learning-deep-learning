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

### Assignment 8 - Using a saved model to make predictions on data without ground truth.

Without even knowing it, you're fast becoming a Python pro, and actually you thought you were just learning deep learning ;)

Now let's create another function, this time for making predictions using saved model. You will need to have a couple of things to be able to do that: 

- a dataset which has the same features (X variables) as when you created the model
- the saved model structure in a .json file 
- the saved model weights in a .h5 file 

Just to make sure that everything works right, what you can do is just separate the output variable (Y) from the diabetes dataset and use it to validate your predictions once you get it from your loaded model. 

You can get the example code for doing it [here](https://github.com/mikkokotila/learning-deep-learning/blob/master/predict-with-saved-model.py).

### Assignement 9 - Posting your code to Github 

Github is by far the most reasonable and useful tool for sharing your code with others, and making sure that you have tested and stable version that you can access yourself easily anytime. 

Read the basic instruction for creating your first repository [here](https://help.github.com/articles/create-a-repo/)

Before you submit code to your repository, make sure that you provide at least the most basic information on the README.md, for example if there are some configurations that need to be done in some special cases. The minimum is to explain what the code does, and how to use it, and what is the expected output. 

Github .md files, such as the README, have it's own syntax language, so take a moment to learn about it [here](https://help.github.com/articles/basic-writing-and-formatting-syntax/).

Once your README.md file is done, you can then post your code in to files in the repository. The easiest is to just do it from from the Github.com interface. You can learn about creating new files [here](https://help.github.com/articles/creating-new-files/) and about editing those files [here](https://help.github.com/articles/editing-files-in-your-repository/).

Because we are working with Python, as long as you name the file ending with .py, it will be automatically considered as python and the syntax specific highlighting is activated. The other point about naming files is that they should be named in a way that's roughly saying what they are doing, for example keras-train.py and keras-predict.py. 

Github is the most important tool for open source programmers, it is great that now you've learn the basics of that too! :) 

### Assignement 10 - Testing your solution with a different dataset

Because of the fantastic progress you have made so far, and the code you have developed, your actually to take on some actual prediction challenges. To get to test your code and your ability to tweak models under different conditions, you'll have three different kinds of datasets to work on. I will share the datasets accross the next assignements.

#### Challenge 1 - Unemployment Rates and Monthly Polls 

DATAFILE: You can download it here [here](https://github.com/autonomio/datasets/raw/master/autonomio-datasets/parties_and_employment)

FEATURES: monthly support for 10 or so political parties in Finland, and unemployment rate 

OBJECTIVE: You have two in this case. One is first to show which party's popularity is most closely connected with unmemployment rate i.e. you have the highest accuracy in predicting it (once you find the right configuration for your model). The other is where you use the unemployment rate, and all the other party's popularity to predict the popularity of of one of the top parties. You can choose any you like, as long as it's one of the most popular ones. 

This file is in .msgpack format, so you will need Pandas to open it. Once you have open it, you can use it as you would use any other file. If you want, you can export to csv from Pandas, then you can directly use with your current code. 

Msgpack is a really great way to store datafiles, as it retains the format just like a csv file would do it, but because it's stored in binary format, it becomes very small. The other benefit is that it's really fast to compress data in to msgpack format, and even faster to read it. 

Have fun! :) 

### Assignement 11 - Overcoming common issues with data

Well well, as you had found I'm sure, there were some small wrinkles along the way. It is quite common that the data you get is not uniform / clean. The most common issues include: 

- wrong decimal (',' instead of '.')
- data type issues (e.g. strings instead of numbers)
- thousand separtors 
- missing values 
- other garbage mixed with values 
- etc. etc. 

First thing when you get a hold of a dataset, is to make sure that you've catched the most obvious issues in the data. The best way to do that is just to have a visual look of the data first. Genrally a Pandas dataframe is a good format for doing visual checks of data, and Pandas has a bunch of useful tools (as does Numpy) to check for issues such as the above mentioned ones in a programmatic manner. 

The other thing that you will often do is, is transform variables to some other mode, for example you might have a ranged feature (from 0 to 100 for example) and you want to make it in to a binary variable of True or False instead (to say if the value increased or decreased for example). 

#### Four kinds of variables / data:

- boolean categorical (True or False)
- multi categorical (more than two categories)
- ranged (e.g. 0-100)
- continuous (to infinity)

Another common situation is that you might have more than one outcome variable, so you have to handle them each separately in a different test. Maybe you even want to use all together different for each, you have the flexibility to do that so why not if it gives you better result in the end. 

To help you get right back in to action applying what you already know, I've prepared a [code example](https://github.com/mikkokotila/learning-deep-learning/blob/master/simple-data-preparation-examples.py) which you can use to get back on track. As usual, make sure you understand everything the code does before moving on to using it. 

Sometimes the best way to understand what code does and/or validate that it does what it should do, is to execute it line by line where you can always see the output. 

Some useful tips:

- datasets often have formatting issues (e.g. wrong decimal / separators / etc)
- if you're not clear with the columns, ask for more information 
- before doing anything else, make sure you understand each column
- before starting the actual work, drop columns you don't want or need

### Assignement 12 - What to do when a given model does not work 

Sometimes you will find that there is no reasonable way to make a given approach (e.g. plain vanilla dense layer neural net) work on a specific problem. Usually this is due to one of few issues: 

- you have a very small dataset 
- you have very few dependent variables (features you use for predicting) 
- your output layer is continuous (as opposed to categorical)

In such cases, you need to look for a different type of model to work with. Going back to the challenge of predicting the popularity of political parties in Finland, as you had found out, unemployment rate as a single predictor using a simple neural net is not going to give a good result. Sometimes when you just can't get past 60% or so, you probably should try to do something else. 

#### Good artist copy, great artists steal 

This is something Pablo Picasso said, and programming is not too much different. The good thing though, is that we don't have to steal as we can just use open source codes to learn, and sometimes to do things also by minimally changing the code. I don't recommend doing that too much though, as you don't really learn how to program by just copy-pasting code. Much better is to follow a process something like: 

1) Find a few examples
2) See what they do without any changes
3) See how you can plug in your own data 
4) Compare the results you get with different approaches 
5) Make sure you understand the code in each example 
6) Try to figure out why one example performs better than other with your data 
7) Also consider things like how fast they run etc. 
8) Write your own code based on your understanding

#### Types of models you'll commonly use 

Basically there are just two types of predictions you need to make: 

- classifying something i.e. saying that something belongs to a given category
- predicting a future value i.e. saying that some value will change to something else 

One of the key distinctions between the two is related with time. In the case of 'classifications' you can do it without time-series data (where each sample follows the previous over a period of time), but in some cases you can also use time as depedent variable to make your model better. With predicting a future value, you clearly need to have a time-series data, otherwise you can't do it.  

You have now learn how to make classifications, and also learned how that approach is not suitable for all kinds of data for two reasons: 

1) You might want to predict an actual value (e.g. popularity of a party) 
2) The features (e.g. unemployment rate) you have might not be useful for what you are trying to do

The very nice thing about the prediction (as opposed to classification) side of things, is that often all you need is the value itself to predict the value! Yes, that's right, often the strongest predictor for a given value is the predictor itself. Depending on the data and model, sometimes you can accurately predict one step ahead, sometimes you can predict many steps. A single step constitutes the sampling time interval, for example in the politcal poll data we have a timestep of one month i.e. each sample is a month, followed by the next month, and so forth. 

In this assignement, using the data you already have, your job is to build a suitable model based on examples that will accurately predict a given party's popularity in the future. Let's see how many months ahead in time you can predict! 

Instead of having to go through many example models, which often don't work and are messy code, I will provide you with something that I know will work, and also is already tested with the data you are working with. 

Get the code example [here](https://github.com/botlabio/keras-deep-learning-models/tree/master/lstm_regression)

It will also introduce you with the concept of LSTM. Make sure you understand what LSTM is, it's one of the hottest topics of discussion in the deep learning world and have wide-ranging applications. The mode is a regression model, which is one of the most common statistical methods, so it's good to learn a little bit about that as well.  

Read a very nice overview of LSTM [here](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

Read a brief history of regression models [here](https://en.wikipedia.org/wiki/Regression_analysis#History). 

### Assignement 13 - ?

### Assignement 14 - ?

### Assignment 15 - Deep learning when you have text data 

In this assignement you will learn how to handle cases where you just have one feature which is unstructured data (text) and you want to make predictions based on that. More details soon...
