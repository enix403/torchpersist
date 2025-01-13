from setuptools import setup, find_packages

setup(
    name="torchpersist",
    version="0.1.0",
    description="A caching decorator for PyTorch computations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="enix403",
    url="https://github.com/enix403/torchpersist",
    packages=find_packages(),
    install_requires=["torch"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
