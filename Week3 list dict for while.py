#!/usr/bin/env python
# coding: utf-8

# In[9]:


list1=["hello", "python",2018,814]


# In[10]:


list2=[1,2,3,4,5,6,7]


# In[188]:


print("list1[0]:",list1[0])


# In[18]:


print("list2[1；5]:",list2[1:5])


# In[19]:


list1+list2


# In[20]:


list1*2


# In[23]:


2018 in list1


# In[25]:


list2[3:]


# In[27]:


list2[:2]


# In[31]:


list2=[1,2,3,4,5,6,7]


# In[33]:


len(list2)


# In[35]:


max(list2)


# In[37]:


min(list2)


# In[40]:


list=['hello','python',2018,814]


# In[41]:


list1.append(2049)


# In[42]:


print(list1)


# In[43]:


list2=[23,2018,814,2049,2018]


# In[44]:


list2.count(2018)


# In[45]:


list.extend(list2)


# In[47]:


print("Extended list:",list1)


# In[48]:


print("Index dor pytho:",list1.index('python'))


# In[51]:


list =['hello', 'python', 2018, 814, 2049]
list.insert(3,2009)
print("New list:",list)


# In[52]:


vowels=['e','a','u','o','i']


# In[53]:


vowels.sort()


# In[54]:


vowels


# In[55]:


my_list=['chico',419,'Ri',52,0]


# In[56]:


'Ri'in my_list


# In[58]:


dict1={
    "apple":"green",
    "banana":"yellow",
    "cherry":"red"}
print(dict1)


# In[68]:


person_dict={"Chico":24,"Ivy":20,"Ri":29}


# In[70]:


print{'Chico:',person_dict["Chico"]}


# In[72]:


person_dict = {'Chico': 24, 'Ivy': 20, 'Ri': 29}


# In[73]:


print('Chico : ',person_dict['Chico'])


# In[85]:


person_dict["Ri"]=19


# In[88]:


print("Ri:",person_dict["Ri"])


# In[89]:


person_dict["Frank"]=31


# In[90]:


print("Frank:",person_dict["Frank"])


# In[91]:


del person_dict["Ivy"]


# In[92]:


print("new_dict:",person_dict)


# In[93]:


person_dict={"Chico":24,"Ri":19,"Frank":31}


# In[94]:


len(person_dict)


# In[97]:


print("To string:%s"%str(person_dict))


# In[107]:


seq=["Chico","Ivy","Ri"]


# In[117]:


dict = dict.fromkeys(seq)


# In[126]:


print("New_dict%s"%str(dict))


# In[134]:


dict=dict.fromkeys(seq, "A+")


# In[135]:


print("New_dict:%s"% str(dict))


# In[136]:


dict={"Name":"Chico","Gender":"Male","Age":"23"}


# In[137]:


print("Age:%s"% dict.get("Age"))


# In[141]:


dict={"Name":"Chico","Gender":"Male","Age":"23"}
print("dict_values:%s"% dict.items())


# In[145]:


dict={"Name":"Chico","Gender":"Male","Age":"23"}
print("dict_keys:%s"% dict.keys())


# In[152]:


dict={"Name":"Chico","Gender":"Male","Age":"23"}
print("has_key:%s"% dict.__contains__("Age"))


# In[156]:


dict={"Name":"Chico","Gender":"Male","Age":"23"}
pop_value=dict.pop("Gender")


# In[157]:


print("pop_value")


# In[160]:


print(dict)


# In[163]:


dict1={"Name":"Chigo","Age":"23"}


# In[170]:


dict2={'Gender':'Male'}
dict1.update(dict2)
print("new_dict1:%s"% dict1)


# In[171]:


for i in range(1,11):
    print(i)


# In[183]:


total= 0 
for i in range(1,101):
     total=total+i
print(total)


# In[184]:


i=1
while i<6:
    i=i+1
    print(i)


# In[186]:


i=1
while i<6:
    print(i)
    i=i+1
    if i== 3:
        break


# In[187]:


Fixed_cost=30000
Content_cost=70000

member_ff=15
convert_rate=0.1
ad_revenue_each_person=1

num=float(input('please input your estimate number of subscribers:'))
for i in range(0,int(num)):
    if i<50000:
        Total_cost=Fixed_cost+Content_cost
    else:
        Total_Cost=Fixed_Cost+Content_Cost+0.1*(i-50000)
        
    Revenue=(1*i)+(0.1*15*i)
    Net_Income=Revenue-Total_cost
    
    if Net_Income>=0:
        print("subscriber=",i)
        break
        
    if Net_Income<0:
        print("Net_Income=",Net_Income)


# In[ ]:




