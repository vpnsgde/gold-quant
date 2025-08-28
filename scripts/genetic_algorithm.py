#!/usr/bin/env python3
"""
scripts/genetic_algorithm.py

Illustrative Genetic Algorithm simulation for learning purposes.
- Maximizes a simple fitness function.
- Includes logging for all steps.
- Does not require external dataset.
"""

import logging
import random
import os

# Setup logging
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "genetic_algorithm_log.txt")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [INFO] %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, mode='w')
    ]
)

# --- Genetic Algorithm Parameters ---
POPULATION_SIZE = 20
CHROMOSOME_LENGTH = 10
GENERATIONS = 10
MUTATION_RATE = 0.1

# --- Fitness function ---
def fitness(chromosome):
    """Simple fitness: sum of genes"""
    return sum(chromosome)

# --- GA Operations ---
def create_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

def create_population():
    return [create_chromosome() for _ in range(POPULATION_SIZE)]

def select_pair(population):
    sorted_pop = sorted(population, key=fitness, reverse=True)
    return sorted_pop[0], sorted_pop[1]

def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# --- Main GA Loop ---
def main():
    population = create_population()
    logging.info(f"Initial population: {population}")

    for gen in range(1, GENERATIONS + 1):
        logging.info(f"--- Generation {gen} ---")
        new_population = []

        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = select_pair(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population[:POPULATION_SIZE]
        best = max(population, key=fitness)
        logging.info(f"Best chromosome: {best}, Fitness: {fitness(best)}")

    logging.info("Genetic algorithm simulation completed.")

if __name__ == "__main__":
    main()
