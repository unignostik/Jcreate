import os


class Jcreate(str):

    def __init__(self, name):  # create JSON file with object of specified name
        f = open(os.getcwd()+"/jcreate.json", 'w')
        f.write("{\n\t \"" + str(name) + "\": [\n")  #
        f.close()

    def addobject(self, dict):  # add an object to JSON file
        f = open(os.getcwd()+"/jcreate.json", 'a')
        f.write("\t\t{\n\t\t\t")
        for entry in dict:  # iterate though dictionary, separate last element as doesn't require comma after value
            if entry != list(dict.keys())[-1]:
                f.write("\""+str(entry)+"\": ")
                if str(dict[entry]).isnumeric():  # if value is numeric, ignore quotes around value
                    f.write(str(dict[entry])+",\n\t\t\t")
                else:
                    f.write("\""+str(dict[entry])+"\",\n\t\t\t")
            else:  # last element in dictionary
                f.write("\""+str(entry)+"\": ")
                if str(dict[entry]).isnumeric():
                    f.write(str(dict[entry])+"\n\t\t\t")
                else:
                    f.write("\""+str(dict[entry])+"\"\n\t\t\t")

                f.write("\n\t\t},\n\n")  # write trailing characters
        f.close()

    def endfile(self):  # open created JSON file and add trailing characters
        f = open(os.getcwd()+"/jcreate.json", 'a+')
        f.write("\n\t]\n}")
        f.close()
        self.finalize()

    def finalize(self):  # rewrite file with new endlines, needed for multiple calls on 'addObject' under single instance
        g = open(os.getcwd()+"/jcreate.json", 'r+')
        lines = g.readlines()
        g.close()
        lines = lines[:-6]
        lines.append("\n\t\t}\n\t]\n}")
        open(os.getcwd()+"/jcreate.json", 'w').writelines(lines)
