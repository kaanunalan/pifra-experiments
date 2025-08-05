# Experiments for Perpetual Individualized Fair Rank Aggregation #
This repository contains the implementation used for the simulations presented in the Master's thesis provided in *master-thesis.pdf*, along with the corresponding results of the experiments. The system is implemented in Python3 and tested with version Python 3.10.12.

## Results ##
The results of the experiments are located in the directory *plots-and-data*. This includes the generated input data, output data, and scatter plots based on the output data.

## How to Run the Simulations? ##
After installing the dependencies specified in *requirements.txt*, the simulations can be run using the command 

```console
python3 experiment_manager.py
```

## Brief Explanation of Files ##
**data_generator.py**: Generates data based on the given specifications (hard-coded) regarding the instance size, distribution, etc..

**experiment_manager.py**: The central module responsible for the entire experiment workflow: from data generation and simulation to result processing and visualization.

**master-thesis.pdf**: The Master's thesis explaining the theory behind the experiments and discussing the results.

**pifra.py**: Used for testing purposes, not part of the main experiment. Useful for testing specific functions with specific data.

**requirements.txt**: Lists the dependencies.

**result_processor.py**: Analyzes the output with different metrics.

**tspf_runner.py**: Contains the implementation of different *temporal social preference functions (TSPFs)*.

**utils.py**: Provides useful functions used throughout different modules.

**visualizer.py**: Contains functions to plot the results.
