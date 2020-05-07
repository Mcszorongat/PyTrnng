import xml.etree.ElementTree as et

tree = et.parse("qa_Power_Storage_MK5.xml")
print(type(tree))
root = tree.getroot()
print(root.tag)
print("\n ---- \n")
l = list(list(list(list(root)[1])[0])[0])
print(l)
length = len(l)
print("length: ", length)
