from setuptools import find_packages,setup
from typing import List



hypen_E_dot='-e .'
def get_requirements(file_path:str)->List[str]:

    '''this function will return the list of components'''
    reqirements=[]
    with open('requirement.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[require.replace('/n',' ') for require in reqirements]
        if hypen_E_dot in requirements:
            requirements.remove(hypen_E_dot)

    return requirements        


setup( 
    name='MLprojectutube',
    author='judi',
    author_email='judi.rispah.123@gmail.com',
    install_requires=get_requirements('requirement.txt'),
    version='0.0.1',packages=find_packages()
    )