#!/usr/bin/env python
# coding: utf-8

# In[76]:


class Documentation:
    packing_num = ""
    gasket_num = ""
    seal_num = ""
    washer_num = ""
    def __init__(self, part):
         self.part = part
    def replace(self):
         print("Discard the {packing_num} packings, {gasket_num} gaskets, {seal_num} seals, and {washer_num} washers from {part}.".format(packing_num=self.packing_num, gasket_num=self.gasket_num, seal_num=self.seal_num,washer_num=self.washer_num, part=self.part))


# In[77]:


class Engine_head(Documentation):
    packing_num = "3"
    gasket_num = "2"
    seal_num = "6"
    washer_num = "12"

Cylinder_Head = Engine_head("Cylinder Head")
Cylinder_Head.replace()

class brake(Documentation):
    packing_num = "2"
    gasket_num = "4"
    seal_num = "8"
    washer_num = "16"

brake_shoe = brake("Brake Shoe")
brake_shoe.replace()


# In[87]:


class Pressure:
    psi_num = ""
    def __init__(self, part):
         self.part = part
    def replace(self):
        #1 BAR is equal to 14.5038 PSI.    
        print("Extra load: A class of {part} tyre designed to carry a heavier maximum load at {psi_num} psi ({bar_num} bar) for {part}s. Increasing the inflation pressure beyond this pressure will not increase the {part}'s load carrying capability of tyre.\n".format( part=self.part, psi_num=self.psi_num, bar_num= self.bar_num))            


# In[88]:


class Tyre(Pressure):
    psi_num = "43"
    bar_num = round((int(psi_num)/14.5038), 1)

P_Metric = Tyre("P-Metric")
P_Metric.replace()

class Tyre(Pressure):
    psi_num = "41"
    bar_num = round((int(psi_num)/14.5038), 1)

Metric = Tyre("Metric")
Metric.replace()


# In[ ]:




