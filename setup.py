import glob
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

binfiles = glob.glob('bin/*')

setuptools.setup(
    name='pptitles',
    version='1.0.0',
    scripts = binfiles,
    author='phx',
    author_email='phx@example.com',
    description='Extract the slide number and title from all slides in a PowerPoint presentation.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/phx/pptitles',
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)
