import os
import yaml

# outline = yaml.load(open('./outlines/PHDThesisOutlineTemplate.yml',encoding="utf-8"), Loader=yaml.FullLoader)

outline = yaml.load(open('./outlines/academicManuscriptOutlineTemplate.yml',encoding="utf-8"), Loader=yaml.FullLoader)


for i,item in enumerate(outline):

        # print(type(item))

        if type(item) != type({}):
            fileName = "./drafts/" + str(i) + "_" + item.replace(" ","-") + ".md"
            with open(fileName,'w',encoding = "utf-8") as filehandler:
                filehandler.write("## " + item)
                filehandler.write("\n")

        else:
            for k,v in item.items():
                # print(k,v)
                fileName = "./drafts/" + str(i) + "_" + k.replace(" ","-") + ".md"
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
