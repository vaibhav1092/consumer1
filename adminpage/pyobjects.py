


class Movie:
    def __init__(self,id,nm,rw,ct):
        self.id=id
        self.mvname=nm
        self.mvreviews=rw
        self.mvcategory=ct
        self.active='Y'

    def __str__(self):
        return f'''
                ---------- Movie Information ------
                ID : {self.id}
                Name : {self.mvname}
                Reviews : {self.mvreviews}
                Category : {self.mvcategory}
            '''
    def __repr__(self):
        return str(self)

class Director:
    def __init__(self,id,nm,exp):
        self.id=id
        self.dname=nm
        self.dexprc=exp
        self.active = 'Y'
    def __str__(self):
        return f'''
                ---------- Director Information ------
                ID : {self.id}
                Name : {self.dname}
                EXP : {self.dexprc}
            '''
    def __repr__(self):
        return str(self)

class Actor:
    def __init__(self,id,nm,exp):
        self.id=id
        self.aname=nm
        self.aexprc=exp
        self.active = 'Y'
    def __str__(self):
        return f'''
                ---------- Actor Information ------
                ID : {self.id}
                Name : {self.name}
                EXP : {self.aexprc}
            '''
    def __repr__(self):
        return str(self)

class Address:
    def __init__(self,id,ct,pin):
        self.id=id
        self.city=ct
        self.pincode=pin
        self.active = 'Y'
    def __str__(self):
        return f'''
                ---------- Address Information ------
                ID : {self.id}
                CITY : {self.city}
                PINCODE : {self.pincode}
            '''
    def __repr__(self):
        return str(self)

