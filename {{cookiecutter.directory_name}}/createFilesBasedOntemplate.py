import os
import yaml

# outline = yaml.load(open('PHDThesis.yml',encoding="utf-8"))

outline = yaml.load(open('./academicManuscript.yml',encoding="utf-8"))


for i,item in enumerate(outline):

        # print(type(item))

        if type(item) != type({}):
            fileName = str(i) + "_" + item.replace(" ","_") + ".md"
            with open(fileName,'w',encoding = "utf-8") as filehandler:
                filehandler.write("## " + item)
                filehandler.write("\n")

        else:
            for k,v in item.items():
                # print(k,v)
                fileName = str(i) + "_" + k.replace(" ","_") + ".md"
                with open(fileName,'w',encoding = "utf-8") as filehandler:
                    filehandler.write("## " + k)
                    filehandler.write("\n")
                    filehandler.write("\n")
                
                    for subchapter in v:
                        filehandler.write("### " + subchapter)
                        filehandler.write("\n")
                        filehandler.write("\n")
    # print(item,i)
# i=0
# for k,v in outline.items():

#     fileName = str(i) + "_" + k.replace(" ","_") + ".md"
#     print(fileName)
#     i += 1
#     # print(k,v)