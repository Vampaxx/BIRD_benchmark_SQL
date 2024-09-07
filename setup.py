import setuptools

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME           = "BIRD_benchmark_SQL"
AUTHOR_USER_NAME    = "Vampaxx"
SRC_REPO            = "Bird_bench_SQL"
AUTHOR_EMAIL        = "arjunappu1001@gmail.com"


setuptools.setup(
    name            = SRC_REPO,
    version         = __version__,
    author          = AUTHOR_USER_NAME,
    author_email    = AUTHOR_EMAIL,
    description     = "The Text-to-SQL model leverages a large language model (LLM) to automatically translate natural language queries into SQL statements, enabling non-technical users to interact with relational databases",
    long_description            = long_description,
    long_description_content    = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "text to SQL": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages    = setuptools.find_packages(where="src")
)