d={
    "name":"ayush",
    "course":'bca',
    "roll_no":"MRT25UGBCA14",
    "language":{
        "html":"known",
        "css":"known",
        "c":"known",
        "python":"known"
    }
}

d["enroll"]=250110492
d["subjects"]=["maths","english"]
d["fav_movies"]='fight club'
d["fav_place"]="delhi"
print(d["name"])
print(d["language"].keys())

print(d.items())
print(d["language"].items())

print(d.get("fav_place"))
d["year"]="2nd"
pair=list(d.items())
print(pair[8])
d.update({"name": "arnav"})
print(d)
d.update({"year":"3rd"})
print(d)

new_d={"name":"aman",
       "fav_place":"gurugram"}
d.update(new_d)
print(d)