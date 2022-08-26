# DL_framework (Work in progres)

---
Basic framework and cheat sheets for Deep Learning experiments with PyTorch

The code structure is as follows:
```bash

├── configs                     # config files for train/eval runners
├── data                        # symbolic links to the data locations
├── datasets                    # scripts and loaders for specific dataset
├── models                      # models available for testing and training 
    └── resnet            
├── runners                     # definitions of runners for different training modes, evaluation, analysis and evaluation
    ├── evaluators.py           # definition of different evaluation objects
    ├── trainers.py             # definition of different training modes
    └── visualizers.py          # definition of different visualization and analysis modules
├── utils                       # different utils scripts for data manipulation, visualization and generic train or eval tasks
├── analyze.py                  # runs an analysis based on the chosen config file and analyzer
├── evaluate.py                 # starts an evaluation based on the chosen config file and evaluator
├── test_speed.py               # starts a speed test to measure inference and train speed in fps for resnet 50 classification task
├── train.py                    # starts a training of chosen config file
```
