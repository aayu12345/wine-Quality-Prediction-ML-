##this code will help in setting up the src as my local directory
## this step is done after the making template.py => this is step 2

import setuptools
with open("README.md", "r" ,encoding="utf-8") as fh:
    Long_description = fh.read()

__version__ = "0.0.1"
REPO_NAME= "wine-Quality-Prediction-ML-"
AUTHOR_USER_NAME = "aayu12345"
SRC_REPO= "ml_project"
AUTHOR_EMAIL ="kayasthayush123@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for wime quality prediction using ml",
    long_description=Long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)
