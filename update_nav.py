import glob
import os

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the navigation link
    content = content.replace('<a href="group.html">Research Group</a>', '<a href="research.html">Research</a>')
    content = content.replace('<a href="group.html" class="active">Research Group</a>', '<a href="research.html" class="active">Research</a>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# Rename group.html to research.html if it exists
if os.path.exists('group.html'):
    os.rename('group.html', 'research.html')
