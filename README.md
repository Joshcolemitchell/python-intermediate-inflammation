# Inflam
Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:
- [Python 3]
- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

# Inflam

![Continuous Integration build in GitHub Actions](https://github.com/<your_github_username>/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

## Installation/deployment: 
- First clone the repo 
```
git clone URL
```
- install prerequisites
```
pip install -r requirements.txt
```
- setup the environment
```
python3 -m venv venv
source venv/bin/activate
```
- run the code in record mode to see if its working. 
- Run the setup file via python ``python3 setup.py build`` and ``python3 setup.py install``
- Check everything runs by running ``pytest`` in the root directory

```
python --view", "loadJSON", "--patient", "4", "python-intermediate-inflammation/data/inflammation-01.csv","--outfile","Alice.json"]
```


## Basic usage: step-by-step instructions that cover using the software to accomplish basic tasks
To access records for a given patient,enter the following in bash:

```python3 inflammation-analysis.py --view record --patient ## data/inflammation-##.csv```

where ## is the 2-digit patient number.



## Contributing: 

- Create an issue [here](https://github.com/Joshcolemitchell/python-intermediate-inflammation) 
- Please open an issue if you spot any problems


## Contact information/getting help: 




## Credits/Acknowledgements: 
- Thanks to Matthew Bluteau and the helpful demonstrators for teaching the Intermediate Python course. 
- The Carpentries Incubator provided the platform for the course material.


## Citation: 
- Please cite [J. F. W. Herschel, 1829, MmRAS, 3, 177](https://ui.adsabs.harvard.edu/abs/1829MmRAS...3..177H/abstract) if you used this work in your day-to-day life.  
- Please cite [C. Herschel, 1787, RSPT, 77, 1](https://ui.adsabs.harvard.edu/abs/1787RSPT...77....1H/abstract) if you actually use this for scientific work.
- [The Carpentries Incubator](https://github.com/carpentries-incubator/proposals/#the-carpentries-incubator)



## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, Josh Mitchell and Co. has waived all copyright and related or neighboring rights to this work.
