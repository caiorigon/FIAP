from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my_investpy-package",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="lib investpy aula FIAP IA",
    author="Caio Rigon",
    author_email="caiorigon@fiap.aluno.com",
    url="https://github.com/caiorigon/my_investpy",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.13",
)
