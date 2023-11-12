# DATATHON 2023

This project's aim is to advance towards a predictive system that ensures supplies on site preventing stockouts, as well as unified purchases for several months of supply and between several units, leading to less CO2 emissions due to transportation.



## Lets get started


### Prerequisites:

The project has been programmed in Python 3.11, and the following libraries need to be installed:

* `pandas`
* `scikit_learn`
* `matplotlib.pyplot`

to install the necessary libraries, use the following line:
```
py -m pip install <library_name>
```


## How does it work?

The project is based of two files: main.py and lm.py. The main file is used to read, purify and transform the data into a tractable data frame. 

The other file consists on the creation of a prediction model, trained with the previous purchases data. The goal of the project was to fully predict a whole year purchases, but it has not been achieved at all; there is a slight lost of data when fitting and predicting the model, leading to lost puntual purchases. This problem can be solved, but instead the accuracy of the model is deacreased. Considering this fact, we considered to maintain the accuracy while losing some data, thus we considered the issue to be more easily adressed in a near future.

Moreover, we can find three extra files: The fisrt one is the data set provided by NTTDATA. The second one is an excel file that compares real 2023 purchases to the predicted ones by the model, and the other one is a plot of the difference between real and predicted amounts.

### Warning!
In the main file, in the fuction read(), the path of the file must be modified ino order to guarantee a good fucntioning of the program.

## Done with:

* Python 3.11 (https://www.python.org/downloads/release/python-3110/)


## Authors
* **Oriol Monge Gironès** 
* **Miquel Roca Solé** 
* **Adrian Quirante González** 
* **Arnau Pons Oliván** 


