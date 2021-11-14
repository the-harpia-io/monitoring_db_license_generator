from setuptools import setup, find_packages
SERVICE_NAME = 'monitoring_db_license_generator'
SERVICE_NAME_NORMALIZED = SERVICE_NAME.replace('-', '_')

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

tests_require = ['test'],

setup(
    name=SERVICE_NAME,
    version='0.0.1',
    description="monitoring_db_license_generator service",
    url='',
    include_package_data=True,
    author='',
    author_email='',
    classifiers=[
    ],
    keywords=[],
    packages=find_packages(),
    install_requires=requirements,
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            f'{SERVICE_NAME} = {SERVICE_NAME_NORMALIZED}.app:main',
        ]
    },
    zip_safe=False,
    cmdclass={},
    data_files=[]
)
