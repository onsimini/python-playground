import os
import sys

walk_dir = os.path.abspath('/mnt/c/work/TIL')
readme_file = f' # Today I Learned\n\n'

for root, subdirs, files in os.walk(walk_dir):
    # Do not go in .git folder
    subdirs[:] = [d for d in subdirs if not '.git' in d]
    # Do not list the root README.md file
    if root == walk_dir:
        files[:] =[f for f in files if not 'README' in f]
    # Print the folder if any
    if root.replace('/mnt/c/work/TIL', '') != '':
        readme_file += f' ### {root.replace("/mnt/c/work/TIL", "")}.\n\n'
    # Print the list of links to articles
    for f in files:
        readme_file += f' - [{f.replace(".md","")}]({root.replace("/mnt/c/work/TIL", "")}/{f})\n\n'

# Save it in the root README.md file
with open('./test.md', 'w') as f:
    f.write(readme_file)
