# github-urls-checker

Check whether a repo contains invalid urls.

# How to use

Clone the project and in the main folder

```python
python main.py \
    --show-invalid-only \
    --url https://github.com/mit-han-lab/proxylessnas.git
```

and it yields logs as 

```bash
[invalid] https://hanlab.mit.edu/projects/proxylessNAS/
         It is in https://github.com/mit-han-lab/proxylessnas/blob/master/README.md#L2
[invalid] https://hanlab.mit.edu/files/proxylessNAS/figures/proxyless_bar.png
         It is in https://github.com/mit-han-lab/proxylessnas/blob/master/README.md#L27
[invalid] https://hanlab.mit.edu/files/proxylessNAS/figures/proxyless_compare.png
         It is in https://github.com/mit-han-lab/proxylessnas/blob/master/README.md#L32
[invalid] https://hanlab.mit.edu/files/proxylessNAS/figures/proxyless_vs_mobilenet.png
         It is in https://github.com/mit-han-lab/proxylessnas/blob/master/README.md#L40
[invalid] https://hanlab.mit.edu/files/proxylessNAS/figures/proxyless_vs_mobilenet.png
         It is in https://github.com/mit-han-lab/proxylessnas/blob/master/README.md#L64
[invalid] https://hanlab.mit.edu/files/proxylessNAS/figures/specialization.jpg
         It is in https://github.com/mit-han-lab/proxylessnas/blob/master/README.md#L73
......
```