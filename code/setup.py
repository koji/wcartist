from setuptools import setup

setup(name="wcartist",
      version="0.0.1",
      description="wcartist is a module to create a word cloud image.",
      long_description=open('readme.md').read(),
      long_description_content_type="text/markdown",
      url="https://github.com/koji/wcartist",
      author='koji kanao',
      author_email='koji.kanao@nyu.edu',
      license="MIT",
      packages=["wcartist"],
      scripts=["bin/wcartist"],
      install_requires=["docopt", "Pillow", "wordcloud", "numpy", "matplotlib"])
