# Understanding JAMs

# Codebase

### Using Virtual Enviroments

A good [primer](https://realpython.com/python-virtual-environments-a-primer/) on the uses of venv.

```bash
python3 -m venv venv # to create new venv in directory
source venv/bin/activate # to activate it
pip install -r requirements.txt
deactivate # to deactivate
```

### Using venv in Jupyter notebook

```bash
$ python -m venv projectname
$ source projectname/bin/activate
(venv) $ pip install ipykernel
(venv) $ ipython kernel install --user --name=projectname
```

#
Then install requirements 
pip install -r requirments.txt