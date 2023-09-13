import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup_info = {
    "name": "foxford",
    "version": "1.1",
    "author": "frostx",
    "author_email": "denialfrostiks589@gmail.com",
    "description": "foxford is a modern object-oriented asynchronous Python wrapper for the Foxford's web API.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/frostx-official/foxford",
    "packages": setuptools.find_packages(),
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Software Development :: Libraries"
    ],
    "project_urls": {
        "Issue Tracker": "https://github.com/frostx-official/foxford/issues",
        "GitHub": "https://github.com/frostx-official/foxford/"
    },
    "python_requires": '>=3.7',
    "install_requires": [
        "httpx>=0.21.0",
        "python-dateutil>=2.8.0"
    ]
}

setuptools.setup(**setup_info)