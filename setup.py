from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as f:
        lines = f.readlines()
    # strip newlines and skip empty lines
    return [req.strip() for req in lines if req.strip()]

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Vikas',
    author_email='edutechverse@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
