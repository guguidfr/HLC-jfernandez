import csv
class Database:
    def __init__(self, source, content=[]):
        self.source = source
        self.content = content

    def load_db(self):       
        with open(self.source, 'r', newline="") as File:
            reader = csv.DictReader(File,)
            for line in reader:
                self.content.append(line)

    def get_register(self, ref_key, search):
        for register in self.content:
            if register[ref_key]==search:
                return register
    
    def delete_register(self, ref_key, search):
        register = self.get_register(ref_key, search)
        # print(objective)
        self.content.remove(register)

    def edit_register(self, ref_key, search):
        register = self.get_register(ref_key, search)
        print("Los campos del registro son: ")
        for i in register.keys(): # type: ignore -> hace que pylance ignore la línea
            field = 1
            print(f"{field}.{i}")
            field += 1

main_db = Database(source="./Obligatorios-P3/db.csv")
main_db.load_db()
# output = main_db.get_register("Responsable","Miguel")
# print(output)
# main_db.delete_register("ID", "5")
# for element in main_db.content:
#     print(element)
main_db.edit_register("Responsable","Miguel")
