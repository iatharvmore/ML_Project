from setuptools import setup, find_packages, setup
from typing import List
def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file path.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    requirements = [req.replace("\n", "") for req in requirements]
    if '-e .' in requirements:
        requirements.remove('-e .')

setup(
    name="MLProject",
    version="0.1",
    author="Atharv_More",
    author_email="atharvmore1634@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
