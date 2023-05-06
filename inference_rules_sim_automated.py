"""Author: Mahmoud Mokhiamar
   This code is a simulation to the inference rules applied in Discrete mathematics course.
   -In this code some assumptions are made such as in modus ponens the second premise is always the first part in the first premise. 
   -premises order cannot be switched. 
   -For using of simplification rule, the other propostion that has been simplified is stored in always true dictionnary.
   -Premises variables are stored in the props dictionnary.
"""

props = {"T":"today is Tuesday","E":"I have a test in English","S":"I have a test in Science","A":"My English Professor is absent"}
text = "If today is Tuesday, then I have a test in English or Science. If my English Professor is absent, then I will not have a test in English. Today is Tuesday and my English Professor is absent. Therefore I have a test in Science."

premises1 = text.split('.')
premises1.pop() #remove space after last period
premises2 = []
always_true = {}

class Premise():
    def __init__(self,text) -> None:
        self.text = text

    def __repr__(self) -> str:
        return self.text
    
    def simplification(self):
        if "and" in self.text and "if" not in self.text:
            # obj = Premise(self.text[self.text.index("and"):])
            # premises2.append(obj)
            second_part = self.text[self.text.index("and")-3:]
            self.text = self.text[:self.text.index("and")-1]
            always_true[self.text] = second_part
        if "or" in self.text and "if" not in self.text:
            second_part = self.text[self.text.index("or")+3:]
            self.text = self.text[:self.text.index("or")-1]
            always_true[self.text] = second_part

    def modus_ponens(self,other):
        if isinstance(other,str):
            for pre in premises2:
                if other in str(pre):
                    other = pre
        if str(other) in str(self) and "not" not in str(self):
            idx = premises2.index(other)
            self.text = self.text[self.text.index("then")+5:]
            premises2.pop(idx)
        else:
            self.text = self.text[self.text.index("not"):]
    def disj_syllo(self,other):
        if self.text[:self.text.index(' ')] in str(other) and "not" in str(other):
            self.text = self.text[self.text.index("or")+3:]
            idx = premises2.index(other)
            premises2.pop(idx)
    def modus_tollens(self,other):
        if "not" in str(self) and self.text[self.text.index("not")+1:] in str(other):
            other.text = other.text[other.text.index("then")+1:]
            idx = premises2.index(self)
            premises2.pop(idx)
    def hypothetical_syllogism(self,other):
        if self.text[self.text.index("then")+1:] in str(other) and "then" in str(other) and other.text[other.index("then")+1:] not in str(self):
            other.text = other.text[:other.text.index(" ")] + " then " +self.text[self.text.index("then")+1:] #p from the first and r from the second
            idx = premises2.index(self)
            premises2.pop(idx)
    def resolution(self,other):
        if "or" in self.text and "or" in other.text and "not" in other.text and self.text[:self.text.index("or")] in other.text and other.text[other.text.index("or")+1:] not in self.text:
            self.text = self.text[self.text.index("or")+3:] + " or " + other.text[other.text.index("or")+3:]
            idx = premises2.index(other)
            premises2.pop(idx)

#automations
def run(premises,always_true):
        sz = len(premises)
        for i in range(sz):
            for j in range(sz):
                try:
                    if i!= j and str(premises[j]) in str(premises[i]) and "not" not in str(premises[i]):
                        print(str(premises[i]) + " " + str(premises[j]))    
                        premises[i].modus_ponens(premises[j])   
                        break
                except:
                    pass 
        for key,val in always_true.items():
            for pre in premises:
                if val in str(pre):
                    pre.modus_ponens(key)
        #disjunctive syllogism check
        for i in range(sz):
            for j in range(sz):
                try:
                    prem_j = str(premises[j])
                    if i!= j and "or" in str(premises[i]) and "not" in str(premises[j]) and prem_j[prem_j.index(" ")+1:] in str(premises[i]):
                        print(str(premises[i]) + " " + str(premises[j]))
                        premises[i].disj_syllo(premises[j])
                except:
                    pass
            
          
premises2.append(Premise("If T then E or S"))
premises2.append(Premise("If A then not E"))
premises2.append(Premise("T and A"))

print(premises2)
print(always_true)

premises2[2].simplification() #simplify T and A to T
# premises2[0].modus_ponens(premises2[2]) //replaced by run function
#T --> (E V S)
#T           
#------  Modus Ponens
#E V S 
run(premises2,always_true)

# premises2[1].modus_ponens(always_true['T']) //replaced by run function
#A --> ~E
#A (T and A always true ( simplification ))
#-----
#~E
print(premises2)
print(always_true)


# premises2[0].disj_syllo(premises2[1])
#E V S
#~E
#------
#S 
print("Conclusion: " + props[str(premises2[0])])


 




