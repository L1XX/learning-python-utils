import os

for root, dirs, files in os.walk("."):
    for f in files:
        p = os.path.join(root, f)
        if os.path.getsize(p) > 10_000_000:
            print(p)
