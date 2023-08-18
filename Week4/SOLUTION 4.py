#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 as sq
import datetime


# In[2]:


con = sq.connect("contactmanagementsystem216.db")


# In[3]:


cur = con.cursor()


# In[4]:


cur.execute("""create table if not exists contact
               ( cid int primary key,
                 fname text,
                 lname text,
                 contact number,
                 email text,
                 city text
                 check ( email like '%_@_%._%')
                );""")


# In[5]:


cur.execute("""create table if not exists details_log
                (
                    
                    fname text,
                    lname text,
                    newcontact number,
                    oldcontact number,
                    datetime text,
                    operation text
                    
                )""")


# In[6]:


cur.execute("""create trigger if not exists insertdata
               after insert on contact
               begin
                   insert into details_log
                   values(new.fname,new.lname,new.contact,'NULL',datetime('now'),'insert');
               end;
                   """)


# In[7]:


cur.execute("""create trigger if not exists deletedata
               after delete on contact
               begin
                   insert into details_log
                   values(old.fname,old.lname,'NULL',old.contact,datetime('now'),'delete');
               end;
                   """)


# In[8]:


cur.execute("""create trigger if not exists updatedata
               after update on contact
               begin
                   insert into details_log
                   values(new.fname,new.lname,new.contact,old.contact,datetime('now'),'update');
               end;
                   """)


# In[9]:


def updaterecord(cd):
    newcon=int(input("Enter new Contact Number:"))
    cur.execute(f"Update contact set contact={newcon} where cid={cd};")


# In[10]:


def deleterecord(cd):
    cur.execute(f"delete from contact where cid={cd}")


# In[11]:


def searchrecord(cd):
    cur.execute(f"select * from contact where cid={cd}")
    row=cur.fetchall()
    print(row)


# In[12]:


cur.execute("""insert into contact values
                (1,'rudra','solanki',9316203288,'rudra1718@gmail.com','chalthan'),
                (2,'veer','solanki',9034567898,'sunil9090@gmail.com','bardoli'),
                (3,'dev','rathod',8970564789,'dev666@gmail.com','vyara'),
                (4,'shiv','shaikh',8976620101,'shiv3455@gmail.com','bardoli'),
                (5,'farhan','tai',9987120302,'tai5344@gmail.com','madhi');""")


# In[ ]:


updaterecord(2)


# In[ ]:


deleterecord(3)


# In[ ]:


cur.execute("select * from contact")
row=cur.fetchall()
for i in row:
    print(f"\nID:{i[0]}\nFname:{i[1]}\nLname:{i[2]}\nContact:{i[3]}\nEmail:{i[4]}\ncity:{i[5]}")


# In[ ]:


cur.execute("select * from details_log")
row1=cur.fetchall()
print(row1)
for i in row1:
    print(f"\nFname:{i[0]}\nLname:{i[1]}\nNew-contact:{i[2]}\nOld-Contact:{i[3]}\nDatetime:{i[4]}\nOpera


# In[ ]:




