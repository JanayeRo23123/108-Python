

def about_me():
    me = {
        "first": "Janaye",
        "last": "Rouser",
        "age": 31,
        "address":{
            "street": "Sunflower ln",
            "number": "4444",
            "city": "San Antonio",
            "zip": "78245",
        }
    }

    print(me)
    #read values
    print(me["first"] +""+ me ["last"])
    print(f"I'm + {me ['age']} + years old")

    #read the address 
    print(me["address"]["street"])

    address = me["address"]
    street = address["street"]
    num = address["number"]
    city = address["city"]
    print(street)

    # a) Return to: street #numb, city, zip.
    print(f"Return to: {street} #{num}, {city}, {"zip"}.")




# fn calls
about_me()