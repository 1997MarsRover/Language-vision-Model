from setuptools import setup, find_packages

setup(
    name='moondream',
    version='1.0.1',
    description='1.6B parameter model built by @vikhyatk using SigLIP, Phi-1.5 and the LLaVa training dataset. ',
    author='1997marsrover',
    author_email='antonygithinji11156@gmail.com',
    packages=find_packages(),
    install_requires=[
        'transformers'
    ],
)