import os
import git
import re
import requests

EXCLUDE_EXT = (
    "gitignore",
    "pyc",
)

EXCLUDE_DIR = (".git")


def walk_folder(folder="temp"):
    for subdir, dirs, files in os.walk(folder, topdown=True):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIR]

        for filename in files:
            fpath = subdir + os.sep + filename
            if fpath.split(".")[-1] in EXCLUDE_EXT:
                continue
            yield fpath


URL_REGEX = '''((https|http):\/\/[^\t\s\)\(\[\]\"\'\>\<\{\}]*)'''
url_pattern = re.compile(URL_REGEX)


def extract_urls(folder="temp"):
    for fname in walk_folder(folder):
        with open(fname, "r") as fp:
            lines = fp.readlines()
        for lidx, line in enumerate(lines):
            matches = re.finditer(URL_REGEX, line, re.MULTILINE)
            for idx, match in enumerate(matches):
                url = match.group(0)
                if url[-1] == ".":
                    url = url[:-1]
                yield url, fname, lidx


def test_url_availability(url):
    try:
        with requests.get(url, timeout=10) as r:
            if r.status_code == 200:
                return True
            return False
    except requests.exceptions.ConnectTimeout:
        return False

