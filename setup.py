from setuptools import setup, find_packages

setup_args = dict(
    name='genderbr',
    version='0.0.3',
    description='Predict gender from Brazilian first names',
    long_description='A method to predict and report gender from Brazilian first names using the Brazilian '
                     'Institute of Geography and Statistics Census data.',
    license='MIT',
    packages=find_packages(),
    author='Guilherme Colodetti G Silveira',
    keywords=['gender', 'brasil', 'nome', 'ibge'],
    url='https://github.com/guilhermecgs/genderBR',
    download_url='https://pypi.org/project/genderbr/'
)

install_requires = [

]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
