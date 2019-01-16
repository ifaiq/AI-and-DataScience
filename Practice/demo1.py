from sklearn import tree

x=[[180,70,44],[177,70,43],[167,60,38],[160,60,38],[179,70,44],[185,75,47],[157,60,35],[190,80,48]]
y=['male','male','female','female','male','male','female','male']
clf = tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
p =clf.predict([[190,73,43]])
print(p)