from turtle import update


dic={"fast":"in a quick mannaer",
"harry":"a coder",
"marks":[1,3,5],
"anotherdic":{"shayan":"a player"},
1:2
}
dic["marks"]=[1,8,8]
print(dic["harry"])
print(dic["marks"])
print(dic["anotherdic"]["shayan"])
newdic={
    "lovish":"freind"
    }
dic.update(newdic)
print(dic)
print(list(dic.keys()))
print(list(dic.values()))
print(list(dic.items()))
print(dic.get("harryi"))