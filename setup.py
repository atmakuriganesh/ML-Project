from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    excluding the -e . used for local package installation
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "").strip() for req in requirements]
        
        # Remove -e . if present in requirements
        requirements = [req for req in requirements if req != '-e .' and req != '']
    
    return requirements

setup(
name='ML-PROJECT',
version='0.0.1',
author='Ganesh',
author_email='atmakuriganesh1234@gmail.com',
packages=find_packages(where="src"), 
package_dir={"": "src"},
install_requires=get_requirements('requirements.txt')

)