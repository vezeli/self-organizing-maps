.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/vezeli/self-organizing-maps/master?filepath=notebooks

===========================================
Primers of using Self-Organizing Maps (SOM)
===========================================

To start working with notebooks on a remote server (without cloning the
repository locally) follow the link at Binder_.

Self-Organizing Map (SOM) is a type of artificial neural network trained
using unsupervised learning. It is useful for solving problems of
dimensional reduction and simplifying visualisation of complex and
high-dimensional data. This project doesn't implement it's own SOM
algorithm, instead it adopts SOM implementation from `MiniSOM package`_.

.. _minisom package: https://github.com/JustGlowing/minisom

Two examples of using SOM are

* ``notebooks/animals_som.ipynb``
* ``notebooks/students_som.ipynb``

The first example is training the network to reduce the high-dimensional
input from ``data/animals.csv`` on a plane and group animals with
similarities close to each other. The dataset was taken from Kaggle_.
The example is very simple and shows how to use `MiniSOM package`_. The
second example looks at similarities between students according to the
data in ``data/students.csv`` which is generated with ``gendata.py``.

.. _Kaggle: https://www.kaggle.com/agajorte/zoo-animals-extended-dataset

Generate data
-------------

Data ``data/students.csv`` is a result of semi-randomly generated
algorithm in ``gendata.py``. The script simulates a survey for students
where each student answers a list of yes-or-no questions related to four
topics: sport, science, art and random. The students belong to either
sport, science or art club and they answer with a value between 0 and 1
where 0 means "no" and 1 means "yes". Results are semi-random because
students that are members of sport club are hard-coded to answer with
higher interest on sport-related questions and lower on all others,
similarly goes for student from other groups. Random topic is added to
introduce more entropy to the data. The script for generating data can
be easily extended.

Questions:

#. Do you like sports? (sport)
#. Do you like art? (art)
#. Do you like science? (science)
#. Do you read books? (science)
#. Are you well coordinated? (sport)
#. Are you an indoor person? (random)
#. Do you consider yourself creative? (art)
#. Do you like physical activities? (sport)
#. Do you consider yourself above-average social? (random)
#. Do you enjoy watching scientific documentary movies? (science)
#. Do you like puzzles? (science)
#. Do you enjoy building things? (art)
#. Do you like camping? (random)
#. Are you tidy and organized? (random)

Usage
-----

The notebooks can be ran on a remote server at Binder_. Following the
link starts a jupyter notebook session in a browser. This is the
simplest way to reproduce the results as there are no requirements from
the user other than having an internet connection.

Alternatively, the project can be cloned and used locally. In this case
make sure to use Python 3.7, or newer, and install project requirements
by typing ``pip install -r requirements.txt`` (use ``-u`` flag in case
you don't have administrator permissions).

If you would like to regenerate student data run ``python gendata.py``.
It is relatively simple to make changes such as including more students,
changing questions, modifying the weights with which they answer the
questions (in ``gen_rand_answers`` function), just to name a few.

.. _Binder: https://mybinder.org/v2/gh/vezeli/self-organizing-maps/master?filepath=notebooks
