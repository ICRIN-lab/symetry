# Symmetry Task 

## CONTENTS OF THIS FILE

* Introduction
* Symmetry Task
* Task design example
* Requirements
* Contributions
* More informations
* Contact


## INTRODUCTION

Our research team is studying different aspects of psychiatric disorders. Our present project is all about exploring obssessive compulsive disorders' secret garden. For that matter, we designed original home-made cognitive tasks, fresh out of the oven!

## Symmetry Task

*Symmetry* is a tricky cognitive task where we display an image of two bars on a 1920 x 1080 pixels widescreen monitor, and the participant is asked whether the bars are parallel or not.
Simple, isn't it ? Don't be so confident, we weighed our words before calling it *"tricky"*.

The images are stored in the file "img". 
The bars are generated with this [code](gen_parallel.py).

A training session is launched including 3 trials. 
Afterward, the task begins and contains 100 trials. 

The task starts with instructions written in french, and are designed for "Trackpad" response.

The questions are also written in french "Les barres sont elles parallèles" which means "Are the bars parallel?" *in english*.


## Task Design example

Here is an example of the task. 

![barres](https://user-images.githubusercontent.com/92592951/168606045-01ce3c6e-7b7e-4635-94b2-4e01ff422234.png)

![question_sym](https://user-images.githubusercontent.com/92592951/168606048-16f813df-97f2-4821-ae1a-e0396b788017.png)

## REQUIREMENTS

### Imports :

We use the package PsychoPy under Python 3.6 to run the tasks. Furthermore, Symmetry Task requires the import of time, as the time spent by the participants is a valuable data.
```python
import time
from psychopy import core
from Template_Task_Psychopy.task_template import TaskTemplate
from list_images import images
```

In order to import TaskTemplate, here are our recommendations. :

* **Step 1** : Clone Template_Task_Psychopy repository from GitHub 


Here's the <a href="https://github.com/ICRIN-lab/Template_Task_Psychopy.git"> link </a>


* **Step 2**: Create a symbolic link locally with Template_Task_Psychopy :

```python
  yourtask_directory % ln -s ../Template_Task_Psychopy Template_Task_Psychopy
```  



### Specificities :

If you want to try this cognitive task using your keyboard, don't forget to the response_pad to False

```python
class Symmetry(TaskTemplate):
    nb_ans = 2
    response_pad = False  # has to be set on "True" if a trackpad is used.
```

## Contributions

To contribute, please fork the repository, hack in a feature branch, and send a pull request.

## More informations

Homepage: [iCRIN Lab](http://icrin.fr/)

## Contact us

Mail : contact@icrin.fr

Twitter : https://twitter.com/RedwanMaatoug
