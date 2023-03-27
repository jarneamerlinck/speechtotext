# Python-sphinx-documentation

Template to document code with sphinx

## Create documentation

1. Update files to fit the new package

- Change ```packagename``` to the new packagename
- Change version in ```packagename/version``` and ```setup.py```
- Update ```setup.py```
- Update sources for Sphinx
  - ```docs/source/conf.py```
  - rst files


2. Install package with conda

```conda env create -f environment.yml```

3. Make documentation

- ```cd docs```
- ```make html```
  - alternatives ```make help```

## Add new python files

1. Add files in package folder ```packagename``` (or the new name)
2. Add links to the python files in ```docs/source/```
3. Make [Documentation](#create-documentation) (see above)

