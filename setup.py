import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="selenium-move-cursor",
    version="0.0.4",
    author="smirad91",
    author_email="smirad91@gmail.com",
    description="Move mouse cursor to element in browser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smirad91/SeleniumCursor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
	install_requires=["pywin32", "pyautogui"],
)