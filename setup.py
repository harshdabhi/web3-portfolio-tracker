from setuptools import setup

def find_packages():
    with open('./requirements.txt','r+') as f:
        packages=f.read()
        f.close()
        return packages.split()

setup(
	name='yourDebank',
	version='0.1.0',
	description='web3 project to get wallet address holding and its latest transaction activity',
	author='Harsh dabhi',
	author_email='harshdabhi@yahoo.com',
	packages=['yourDebank'],
	install_requires=find_packages()
)
