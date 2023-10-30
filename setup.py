from setuptools import setup, find_packages

setup(
    name='VPGen',
    version='0.9.5',
    author='Savvin Anton',
    author_email='anv.savvin@gmail.com',
    license='GPL-3.0 license',
    description='Generate porosity medium',
    long_description_content_type='text/markdown',
    long_description='long description',
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    platforms=['Windows', 'Unix'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Inteded Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
    ],
    include_package_data=True,
)
