from distutils.core import setup

setup(
    name="magicForElsa",
    packages=["Magic", "task1", "talk1"],
    version="1.15",
    license="MIT",
    description="A package for the personal assistant Elsa",
    author="George Rahul",
    author_email="georgerahul24@gmail.com",
    url="https://github.com/georgerahul24/MagicForElsa",
    keywords=["program", "automate", "task", "magic"],
    install_requires=["pyttsx3", "win10toast"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)
