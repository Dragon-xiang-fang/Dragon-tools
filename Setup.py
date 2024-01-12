from setuptools import setup, find_packages

setup(
    name='dragon-tools',
    version='0.1',
    packages=find_packages(),
    author='DragonXiang',
    author_email="dragonxiangfang@163.com",
    description="A small package od tools",
    url='https://github.com/Dragon-xiang-fang/Dragon-tools',
    install_requires=[
        'numpy',
        'pandas',
        'pymupdf',
        'matplotlib'
    ],
)