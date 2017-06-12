# Troubleshooting 

Troubleshooting is one of the most common tasks a practical computer scientists (e.g. programmer or data scientist) will perform on daily basis. Without having the skills and confidence to handle various 'obstacles', working will be very frustrating. Usually it's better to ask someone only when you've depleted all other options. This is a very important point. 

### 1. Standard protocol

1) Always start by making sure that you are not making some obvious mistake 

2) Make sure that you have the latest / most up-to-date version of the solution you have a problem with. 

2) Next check from Google / Stackoverflow.com what kind of results you find for the problem 

3) If you still can't find anything after spending some time trying different things, ask someone you know 

It is very important to learn the process of troubleshooting this way, as otherwise it will be hard to work indepedently. Even experienced programmers face multiple obstacles on a given day, so it's very important to have an effective and self-sustained way to overcome any obstacle.

### 2. Kinds of Problems - Problem specific protocols

#### 2.1. How to perform something you don't know how to do

Most typical troubleshooting relates with "how to do x with y" for example "how to generate a random number with numpy", which is actaully really not troubleshooting, but the process is exactly the same. 

#### 2.2. Something that worked, stopped working

For example if you get an issue with Jupyter Notebook, you would follow the sequence as below. Typically you will find that the first or second might work, so you don't have to go further and do the more involving things.  

1) Restart the kernel 

2) Close the notebook (from the file menu) and start it again

3) Shutdown Jupyter entirely from the open shell (ctrl+c and then 'y')

4) Start a new shell and then start Jupyter there

5) Restart your machine 

6) Try creating a new notebook where you try to do the same thing

7) Try upgrading your the related packages (note below is a generic example)

##### Upgrade for pip package 

    pip install packagename --upgrade 

##### Upgrade for apt package 

    sudo apt-get upgrade
    sudo apt-get --only-upgrade install packagename

#### 2.3. You can't make something work even though it "should work"

Almost all this type of problems are human error i.e. it is you that is making the mistake. Or the instructions you have for doing something are not working, which means that you have find new instructions and treat the case as in 2.1. 

