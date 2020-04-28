import os
import git
import re



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

import requests
def test_url_availability(url):
    try:
        with requests.get(url, timeout=10) as r:
            if r.status_code == 200:
                return True
            return False
    except requests.exceptions.ConnectTimeout:
        return False


os.makedirs("temp", exist_ok=True)
# git.Repo.clone_from("https://github.com/mit-han-lab/proxylessnas.git", "temp")
# git.Repo.clone_from("https://github.com/mit-han-lab/AMC.git", "temp")
giturl = "https://github.com/mit-han-lab/AMC/blob/master/"
for url, fname, lidx in extract_urls():
    print(url)
    print("\t", test_url_availability(url))
    print("\t", "%s%s#L%d" % (giturl, fname.replace("temp/", ""), lidx + 1))
