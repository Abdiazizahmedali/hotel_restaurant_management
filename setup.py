from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='hotel_restaurant_management',
    version='1.0.0',
    description='Comprehensive Restaurant and Hotel Management for ERPNext v15',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
) 