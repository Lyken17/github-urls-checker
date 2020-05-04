import os, sys, shutil
import os.path as osp

import git

def main():
    pass


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser("Git URLs Check")
    parser.add_argument("--folder", type=str, default="temp", help="The place to temporally store git repos.")
    parser.add_argument("--url", type=str, help="The link to the repo that you want to check")
    parser.add_argument("--show-invalid-only", action="store_true", help="By default, only invalid urls are printed.")

    args = parser.parse_args()

    url = args.url
    if url.endswith(".git"):
        url = url[:-4]
    giturl = osp.join(url, "blob/master")
    shutil.rmtree("temp/")
    git.Repo.clone_from(url, "temp")

    from utils import extract_urls, test_url_availability

    for url, fname, lidx in extract_urls(folder="temp/"):
        available = test_url_availability(url)
        if available and args.show_invalid_only:
            continue
        status = "valid" if available else "invalid"
        print("[%s]" % status, url)
        rel_path = "/".join(fname.split("/")[1:])
        print("\t", "It is in %s#L%d" % (osp.join(giturl, rel_path) , lidx + 1))
