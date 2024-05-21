# Simplifying Python Code through the Lens of Functional Programming

A repo for my PyConIT talk:
https://2024.pycon.it/en/event/simplifying-python-code-through-the-lens-of-functional-programming

## Project Overview
This project is a collection of Python scripts demonstrating various approaches to data processing pipelines.
The main focus is on functional programming techniques and error handling in Python.
The scripts read data from a CSV file, perform various transformations, and compute the average score.

## Getting Started
To run the scripts, you need to have pixi installed. If you don't have pixi, you can install it following the instructions at:
https://pixi.sh/latest/

## Scripts

The `src/pipeline` directory contains several Python scripts, each demonstrating a different approach to building a
data processing pipeline:

* [pipeline_a_polars.py](./src/pipeline/pipeline_a_polars.py): Uses the Polars library to compute the average score.
* [pipeline_b_imperative.py](./src/pipeline/pipeline_b_imperative.py): An imperative approach to building the pipeline.
* [pipeline_c_imperative_with_one_thing.py](./src/pipeline/pipeline_c_imperative_with_one_thing.py): An improved version of the imperative approach.
* [pipeline_d_with_currying.py](./src/pipeline/pipeline_d_with_currying.py): Uses currying to build the pipeline.
* [pipeline_e_function_composition.py](./src/pipeline/pipeline_e_function_composition.py): Uses function composition to build the pipeline.
* [pipeline_f_error_handling.py](./src/pipeline/pipeline_f_error_handling.py): Focuses on error handling in the pipeline.
* [pipeline_g_pymonad.py](./src/pipeline/pipeline_g_pymonad.py): Uses the PyMonad library to build the pipeline.

## Contributing
Contributions are welcome. Please submit an issue if you have something to add or fix.

## Resources
