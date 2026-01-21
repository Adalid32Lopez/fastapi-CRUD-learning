import pathlib
import json

class ManageDb:
    __addres_file = "{0}/src/db/dbContacs.json".format(pathlib.Path().absolute())
    
    def read_contact(self):
        with open(self.__addres_file, "r") as data:
            return json.loads(data.read())

md = ManageDb()
print(md.read_contact())
 