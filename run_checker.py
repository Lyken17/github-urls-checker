import git, os
from utils import extract_urls, test_url_availability

# os.makedirs("temp", exist_ok=True)
# git.Repo.clone_from("https://github.com/mit-han-lab/proxylessnas.git", "temp")
# git.Repo.clone_from("https://github.com/mit-han-lab/AMC.git", "temp")
giturl = "https://github.com/mit-han-lab/AMC/blob/master/"

for url, fname, lidx in extract_urls(folder="."):
    print(url)
    print("\t", test_url_availability(url))
    print("\t", "%s%s#L%d" % (giturl, fname.replace("temp/", ""), lidx + 1))