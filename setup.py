from setuptools import setup


def read_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


setup(
    name="ankiwebify",
    version="0.0.1",
    description="Convert Markdown to the HTML accepted by AnkiWeb",
    author="Abdo",
    author_email="abd.nh25@gmail.com",
    py_modules=["ankiwebify"],
    keywords=["anki", "ankiweb", "markdown", "html"],
    long_description=read_file("README.md"),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["Markdown", "beautifulsoup4"],
)
