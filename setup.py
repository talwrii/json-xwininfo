import setuptools

setuptools.setup(
    name='json-xwininfo',
    version="1.1.0",
    author='@readwithai',
    long_description_content_type='text/markdown',
    author_email='talwrii@gmail.com',
    description='Various convenience functions to get json information similar to xwininfo',
    license='BSD with added link requirement',
    url='https://github.com/talwrii/json-xwininfo',
    packages=["json_xwininfo"],
    install_requires=["Xlib"],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': ['json-xwininfo=json_xwininfo.main:main']
    }
)
