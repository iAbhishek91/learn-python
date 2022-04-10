# Anaconda

```sh
# check if conda is installed in your path
conda -V

# update conda environment
conda update conda

# create virtual env
conda create -n tf-project python=3.6

# install package in a virtual env
conda install -n tf-project pyhcl
# OR
# activate a vEnv and pip install package name
pip install pyhcl

# activate a virtual env
conda activate tf-project

# deactivate a virtual env
conda deactivate

# delete a virtual env
conda remove -n tf-project -all
```
