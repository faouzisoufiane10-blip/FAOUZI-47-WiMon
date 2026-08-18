from setuptools import setup, find_packages

with open(\"README.md\", \"r\", encoding=\"utf-8\") as fh:
    long_description = fh.read()

setup(
    name=\"wimon\",
    version=\"0.1.0\",
    author=\"Faouzi\",
    description=\"FAOUZI-47 WiMon — Wireless Adapter Orchestrator & Automated Monitor Mode Engine with AI\",
    long_description=long_description,
    long_description_content_type=\"text/markdown\",
    url=\"https://github.com/faouzisoufiane10-blip/FAOUZI-47-WiMon\",
    packages=find_packages(),
    classifiers=[\n        \"Programming Language :: Python :: 3\",
        \"Programming Language :: Python :: 3.9\",
        \"Programming Language :: Python :: 3.10\",
        \"Programming Language :: Python :: 3.11\",
        \"License :: OSI Approved :: MIT License\",
        \"Operating System :: OS Independent\",
        \"Intended Audience :: Information Technology\",
        \"Topic :: System :: Networking\",
        \"Topic :: Security\",
    ],
    python_requires=\">=3.9\",
    entry_points={
        \"console_scripts\": [
            \"wimon=wimon.cli:main\",
        ],
    },
)
