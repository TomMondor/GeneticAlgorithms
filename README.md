# Genetic Algorithms
This small project allowed me to explore the concept of genetic algorithms. 

I discovered this topic after watching a YouTube video : 
[Genetic Algorithms Explained By Example](https://www.youtube.com/watch?v=uQj5UNhCPuo&list=PLmBnuS4i2Esinvn9aFcyd2w3rjZrgmsCH&index=6&ab_channel=KieCodes).

## Contents of the repository
A simple genetic algorithm that solves a simplified version of the Knapsack problem, in which each object's weight equals its value. 
The goal is to maximize the total weight of selected objects, without exceeding the knapsack's capacity.

The algorithm's parameters (see `constants.py`) still need some fine-tuning for optimal results.

It would be interesting to update the project to use the real Knapsack problem, in which each object has a weight and a value 
(the goal is to maximize the total value of the selected objects, without exceeding the knapsack's capacity).

## What are genetic algorithms
Genetic algorithms - and more generally, evolutionary algorithms - offer good (but not necessarily the best) solutions to optimization problems.
They are particularly interesting for optimization problems whose _best_ solution is too long and complex to calculate with regular algorithms.  

They rely on mechanisms inspired by biology and evolution, such as reproduction and mutation, to obtain a generation of better solutions from a previous generation.

Genetic algorithms are even used by Nasa to create antennas with very particular requirements (see [Wikipedia](https://en.wikipedia.org/wiki/Evolved_antenna) or [Nasa](https://ntrs.nasa.gov/citations/20030067398)).
<p align="center">
  <img src="http://www.lunar.org/docs/nasa/images/antenna.jpg" atl="Image of the evolved antenna" width="500" />
</p>
