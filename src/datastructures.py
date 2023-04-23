
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self,last_name):
     
        self._members = []                        # Los miembros de la familia sera lista de objetos 
        
        self.last_name = last_name              
       

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):                          # Funcion que genera una id random a los id de la familia 
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["last_name"] = self.last_name       # Control del apellido solo el resto de campos se añadiran en app.py
        if "id" not in member: member["id"] = self._generateId()    # Si el miembro no existe lo creas 
        self._members.append(member)
        return member
            
    

    def delete_member(self, id):
       for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"msg":"Miembro borrado correctamente!","error":False,"satus":200}
            return {"msg":"Error al borrar miembro de la familia!","error":True,"satus":400}

    def get_member(self, id):
        for member in self._members:
            if memeber["id"] == id :
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
