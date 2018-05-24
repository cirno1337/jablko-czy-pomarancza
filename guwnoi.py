from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
x = input("Podaj wage w gramach")
y = input("gladkie czy nie? (y/n)")

if (y == "y" or y =="Y"):
    y = True
elif (y == "n" or y == "N"):
    y = False
z = [x, y]
print(clf.predict([z]))