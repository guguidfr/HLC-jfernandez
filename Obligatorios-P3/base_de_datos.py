import csv
# database = "./Obligatorios-P3/db.csv"
# db = []
# with open(database, 'r', newline="") as File:
#     reader = csv.DictReader(File,)
#     for line in reader:
#        db.append(line)

# def get_register(ref_key,search):
#     if ref_key=="ID" or ref_key=="N-Horas":
        
#     for register in db:
#         if register[ref_key] == search:
#             return register
# print(get_register("ID","3"))
# for element in db:
#     print("El responsable es: " + element["Responsable"]) 
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
        # if ref_key=="ID" or ref_key=="N-Horas":
        #     search = int(search)
        for register in self.content:
            if register[ref_key]==search:
                print(register)
          
main_db = Database(source="./Obligatorios-P3/db.csv")
main_db.load_db()
main_db.get_register("Responsable","Miguel")