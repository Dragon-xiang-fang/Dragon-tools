from setuptools import setup, find_packages

setup(
    name='dragon-Tools',
    version='0.1.2',
    packages=find_packages(),
    author='Dragon-xiang-fang',
    author_email="dragonxiangfang@163.com",
    description="A small package od tools",
    url='https://github.com/Dragon-xiang-fang/Dragon-tools',
    install_requires=[
        'numpy',
        'pandas',
        'pymupdf',
        'matplotlib'
    ],
    py_requires=["dragonTools"],
)