from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    with open(file_path, 'r') as f:
        requirements = [line.strip() for line in f.readlines() if line.strip() != HYPEN_E_DOT]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Kevin',
    author_email='kevinbecker91@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)