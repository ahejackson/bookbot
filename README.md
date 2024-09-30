# bookbot

A very simple book analysis script written in Python.

Given a plain text file, it will output the word count and the counts of the alphanumeric characters that make up the text.

Originally submitted to complete the ["Build a Bookbot"](https://www.boot.dev/courses/build-bookbot) exercise on [Boot.dev](https//boot.dev/).


## Extensions to the original exercise

The script developed for the Boot.dev exercise has been extended with extra features:

- Support for [Type Hint](https://peps.python.org/pep-0484/)
- Support for command line arguments using the built in [`argparse` module](https://docs.python.org/3/library/argparse.html)


## Usage

Clone the repository. From the directory containing the repository (not the repository itself), use:

```python
$ python3 bookbot file
```

Or for help:

```python
$ bookbot --help
```