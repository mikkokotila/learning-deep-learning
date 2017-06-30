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

1) Did you do your imports already

2) Restart the kernel 

3) Close the notebook (from the file menu) and start it again

4) Shutdown Jupyter entirely from the open shell (ctrl+c and then 'y')

5) Start a new shell and then start Jupyter there

6) Restart your machine 

7) Try creating a new notebook where you try to do the same thing

8) Try upgrading your the related packages (note below is a generic example)

##### Upgrade for pip package 

    pip install packagename --upgrade 

##### Upgrade for apt package 

    sudo apt-get upgrade
    sudo apt-get --only-upgrade install packagename

#### 2.3. You can't make something work even though it "should work"

Almost all this type of problems are human error i.e. it is you that is making the mistake. Or the instructions you have for doing something are not working, which means that you have find new instructions and treat the case as in 2.1. 

#### 2.4. What if a module is not working

The most common reason for a module suddenly not working, or not found after you install it, is becaues you've messed something up with environments. 

- maybe you install the package in global but try to import in env
- maybe you install the package in env but try to import in global
- maybe you install the package in env-a but try to import in env-b 

For the sake of completeness, you would know this from the shell you are in. 

Global looks like:

    Mikkos-Air:dev mikko$

Env looks like: 

    (env_name) Mikkos-Air:dev mikko$

This is why troubleshooting for missing packages is best done in the python console (and not Jupyter). First make you are in the shell/env where you are expecting to import the module and then: 

    python 
    
You can get out with ctrl+d. 

Few important pointers:  

- you should not have to edit your path EVER 
- it's better to install nothing on global and all to the env you are using it

Lear more about python environments [here](http://www.simononsoftware.com/virtualenv-tutorial-part-2/)

### 3. What to do when everything else fails 

Before following this step, make sure you've tried "everything else". 

Most of the popular open source software have their own 'gitter' channel: 

https://gitter.im

You can login easily with your Github account, and then find the relevant chat channel and ask for help. People tend to be very helpful in the open source community. 

Also you might consider [creating a github issue](https://help.github.com/articles/creating-an-issue/) on the relevant Github page for the software you are having problems with. 
