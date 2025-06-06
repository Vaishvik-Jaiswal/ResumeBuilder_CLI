from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="resume-cli-generator",
    version="1.0.1",
    author="Vaishvik Jaiswal",
    author_email="vaishvikjaiswal05726@gmail.com",
    description="A CLI tool to generate professional resumes in PDF format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vaishvik-Jaiswal/resume-cli-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "jinja2>=3.0.0",
        "weasyprint>=54.0",
        "importlib-resources>=1.3.0; python_version<'3.9'",
    ],
    entry_points={
        "console_scripts": [
            "resume-generator=resume_generator.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "resume_generator": ["templates/*.html"],
    },
)