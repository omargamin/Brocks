from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='brocks',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # أضف المكتبات التي تعتمد عليها، مثلاً:
        'PyQt5'
    ],
    author='Omar Dev',
    author_email='omargaminghanud12@gmail.com',
    description='GUI/UI Maker Library For Python',
    long_description=long_description,
    long_description_content_type='text/markdown',  # تم التصحيح هنا
    url='https://github.com/omargamin/Brocks',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
