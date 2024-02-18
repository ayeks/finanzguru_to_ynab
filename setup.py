from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='finanzguru_to_ynab',
    version='0.1',
    author='Lars Luehr',
    author_email='lars.luehr@posteo.de',
    description='Reads a Finanzguru XLSX Export File and writes one YNAB CSV import file per account.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ayeks/finanzguru_to_ynab',  # Replace with your GitHub repository URL
    packages=find_packages(),
    install_requires=[
        'pandas',
        'pyarrow'
    ],
    entry_points={
        'console_scripts': [
            'finanzguru_to_ynab = finanzguru_to_ynab.run:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
