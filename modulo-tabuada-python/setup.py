from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Tabuleiro",
    version="0.0.2",
    author="Aclelino",
    author_email="aclelino@gmail.com",
    description="Tabuada simplificado",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aclelino/modulo-tabuada-python.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
)