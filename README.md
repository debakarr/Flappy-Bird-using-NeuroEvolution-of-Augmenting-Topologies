# Flappy Bird using NeuroEvolution of Augmenting Topologies
A simple implementation of Flappy Bird using NeuroEvolution of Augmenting Topologies.

***

### Introduction
In **NeuroEvolution of Augmenting Topologies** in short **NEAT**, we evolve an **Artificial Neural Network** (**ANN**) using **Genetic Algorithm**. Though this is a very old neuroevolution technique (developed in 2002), yet it is very powerful.

Over the internet, you will find a numerous number of resource related to Genetic Algorithm + Neural Network. For me, I refer to [**Chapter 9. The Evolution of Code**](http://natureofcode.com/book/chapter-9-the-evolution-of-code/
) from the book **The Nature of Code by DANIEL SHIFFMAN** for Genetic Algorithm basics. Here's a quote from the book:

>In order for natural selection to occur as it does in nature, all three of these elements must be present.

>* **Heredity**: There must be a process in place by which children receive the properties of their parents. If creatures live long enough to reproduce, then their traits are passed down to their children in the next generation of creatures.

>* **Variation**: There must be a variety of traits present in the population or a means with which to introduce variation. For example, let’s say there is a population of beetles in which all the beetles are exactly the same: same color, same size, same wingspan, same everything. Without any variety in the population, the children will always be identical to the parents and to each other. New combinations of traits can never occur and nothing can evolve.

>* **Selection**: There must be a mechanism by which some members of a population have the opportunity to be parents and pass down their genetic information and some do not. This is typically referred to as “survival of the fittest.” For example, let’s say a population of gazelles is chased by lions every day. The faster gazelles are more likely to escape the lions and are therefore more likely to live longer and have a chance to reproduce and pass their genes down to their children. The term fittest, however, can be a bit misleading. Generally, we think of it as meaning bigger, faster, or stronger. While this may be the case in some instances, natural selection operates on the principle that some traits are better adapted for the creature’s environment and therefore produce a greater likelihood of surviving and reproducing. It has nothing to do with a given creature being “better” (after all, this is a subjective term) or more “physically fit.” In the case of our typing monkeys, for example, a more “fit” monkey is one that has typed a phrase closer to “to be or not to be”.

Also, Daniel has a complete [playlist dedicated to Genetic Algorithm](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6bJM3VgzjNV5YxVxUwzALHV).

***

### Requirements
* python 2 or 3 ([official site](https://www.python.org/downloads/)).
* pygame (you can find the instructions on how to get it [here](http://www.pygame.org/download.shtml)).

***

### Example use

**Please install the dependencies first.**

```
git clone git@github.com:Dibakarroy1997/Flappy-Bird-using-NeuroEvolution-of-Augmenting-Topologies.git
cd Flappy-Bird-using-NeuroEvolution-of-Augmenting-Topologies/
```

##### To start a Normal game
```
cd "Normal Game"
python Game.py
```

###### Normal Game Demo
![](img/NormalGameDemo.gif)

##### To start NEAT implemented Game (The game will learn itself how to play)

```
cd "NEAT Implementation"
python Game.py
```

###### NEAT Demo

**No parent (red bird) alive**
![](img/NEATDemo2.gif) 

**One or some parent (red bird) alive**
![](img/NEATDemo3.gif)

***

### Milestone

- [x] Normal Game using pygame
- [x] Neural Network
- [x] Genetic Algorithm
- [ ] Troubleshoot