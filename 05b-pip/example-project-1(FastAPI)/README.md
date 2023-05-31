# Example-1

Using FastAPI

## Steps:

- Create virtual env
```shell
conda -V # validate conda is installed, else install
conda env list # list all the conda env
conda create -n <name-of-conda-env> python=3.11 # create new conda virtual env
```

- validate the virtual env
```shell
python --version
pip list
```

- Create the requirements.txt
```shell
touch requirements.txt

# enter the below in requirements.txt
# validate format
## foo
## foo>=5
## foo>=5.6
## foo==5.6.1
## foo>5
## foo>5,<5.7
## foo>0, <5.7
fastapi
unicorn

# install the above packages
pip install -r requirements.txt

# optionally you can update the version
pip list # list the packates in the virtual env
# update requirements.txt with the version like below
fastapi==0.95.2
uvicorn[standard]==0.22.0
```

- write hello world with FastApi
```shell
uvicorn main:app --reload # --reload option restart when there is a change detected in the code
```

-- access the app from browser
```shell
http://localhost:8000/
http://localhost:8000/docs
```