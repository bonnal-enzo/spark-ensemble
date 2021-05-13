from setuptools import setup

setup(
    name='sparkensemble',
    version='0.0.1',
    packages=['sparkensemble'],
    url='https://github.com/pierrenodet/spark-ensemble',
    license='Apache License 2.0',
    author='Pierre Nodet <nodet.pierre@gmail.com>, Enzo Bonnal <enzobonnal@gmail.com>',
    description='Ensemble Learning for Apache Spark',
    install_requires=['pyspark>=3.1.1']
)