from review_models.category import Category
categories =[]
c1 =Category("c1","Nước ngọt")
c2 =Category("c2","Bia")
c3 =Category("c3","Sữa")
categories.extend([c1,c2,c3])
for c in categories:
    print(c)