import markdown
import os

myfile='mymarkdown.md'
filename=os.path.basename(__file__)
path=os.path.abspath(__file__)
mainfolderPath=path.replace(filename,"")
#print(mainfolderPath)

output = markdown.markdown('''
# Step 1
## Step 2
* item 1
* item 2
''')
print(output)



with open(mainfolderPath+myfile,'w') as f:
   f.write(output)