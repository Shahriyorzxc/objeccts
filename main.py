#1
def invert(la):
    d = dict(zip(la.values(), la.keys()))
    return d



print(invert({ "z": "q", "w": "f" }))
# ➞ { "q": "z", "f": "w" }
print(invert({ "a": 1, "b": 2, "c": 3 }))
# ➞ { 1: "a", 2: "b", 3: "c" }
print(invert({ "zebra": "koala", "horse": "camel" }))
# ➞ { "koala": "zebra", "camel": "horse" }

# 2 yoli
def invert(dc2):
    a = []
    b = []
    for k,v in dc2.items():
        a.append(k)
        b.append(v)

    x = dict(zip(b,a))

    return x


print(invert({ "z": "q", "w": "f" }))  #---> {'q': 'z', 'f': 'w'}
print(invert({ "a": 1, "b": 2, "c": 3 })) # {1: 'a', 2: 'b', 3: 'c'}
print(invert({ "zebra": "koala", "horse": "camel" })) # {'koala': 'zebra', 'camel': 'horse'}

#2
def lgs12(lp):
    s = 0
    for x in lp:
        for x ,y in x.items():
            if type(y) == list:
                s += y[-1]
    for x in lp:
        x.update({'notes':s})
    return lp

print(lgs12([
  {'name': "John", 'notes': [3, 5, 4]}]))  #➞ [{ name: "John", avgNote: 4 }]]))


#3
def items_purchase(l,list2):
    list = []
    for x, y in l.items():
        if x > list2:
            pass
        elif list2 > y:
            list.append(y)
    return list


print(items_purchase({
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}, "$300"))
print(items_purchase({
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
  }, "$100"))
print(items_purchase({
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"},
"$1"))


#4
def get_frequencies(l1):
    l2 = {}
    for l in l1:
        a = l1.count(l)
        l2.update({l:a})
    return l2


print(get_frequencies(["A", "B", "A", "A", "A"]))
print(get_frequencies([1, 2, 3, 3, 2]))
print(get_frequencies([True, False, True, False, False]))
print(get_frequencies([]))


#5
def maximum_score(l):
    s = 0
    for x in l:
        for x, y in x.items():
            if type(y) == int:
                s += y
    return s


print(maximum_score([
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]))
print(maximum_score([
  { "tile": "B", "score": 2 },
  { "tile": "V", "score": 4 },
  { "tile": "F", "score": 4 },
  { "tile": "U", "score": 1 },
  { "tile": "D", "score": 2 },
  { "tile": "O", "score": 1 },
  { "tile": "U", "score": 1 }
])) #yigindisi yigish


#6
def top_note(c):
    for x, y in c.items():
        if x == 'notes':
            for _ in y:
                c.update({'notes':max(y)})

    return c


print(top_note({ "name": "John", "notes": [3, 5, 4] }))  #notes dictdagi valuesidagi eng yirik sonni chiqarish
print(top_note({ "name": "Max", "notes": [1, 4, 6] }))
print(top_note({ "name": "Zygmund", "notes": [1, 2, 3] }))


#7
def organize(l1):
    l2 = {}
    if len(l1) == 0:
        return {}
    else:
        b = l1.split(",")
        l2.update({'name': b[0]})
        l2.update({'age': b[1]})
        l2.update({'occupation': b[-1]})
        return l2



print(organize("Jameel Saeb, 15, CEO of facebook")) #--->{"name": "Jameel Saeb","age": 15,"occupation": "CEO of facebook"}
print(organize("John Mayer, 41, Singer")) #{'name': 'John Mayer', 'age': ' 41', 'occupation': ' Singer'}
print(organize("")) #{}



#8
def convert_to_number(d):
    lst = []
    lst2 = []
    for k,v in d.items():
        if type(v) == str:
            b = int(v)
            lst.append(b)

    for x, y in d.items():
        b1 = dict(zip(x,lst))
        lst2.append(b1)
    return lst2


print(convert_to_number({"piano": "200"})) #[{'p': 200}]
print(convert_to_number({"piano": "200", "tv": "300"})) #--->{'p': 200, 'i': 300}, {'t': 200, 'v': 300}
print(convert_to_number({"piano": "200", "tv": "300", "stereo": "400"})) #[{'p': 200, 'i': 300, 'a': 400}, {'t': 200, 'v': 300}, {'s': 200, 't': 300, 'e': 400}]


#9
def expensive_orders(d,i):
    dc1 = {}
    for x, y in d.items():
        if y > i:
            dc1.update({x:y})
    return dc1


print(expensive_orders({ "a": 3000, "b": 200, "c": 1050 }, 1000))
print(expensive_orders({ "Gucci Fur": 24600, "Teak Dining Table": 3200, "Louis Vutton Bag": 5550, "Dolce Gabana Heels": 4000 }, 20000))
print(expensive_orders({ "Deluxe Burger": 35, "Icecream Shake": 4, "Fries": 5 }, 40)) #Valuelar qaytishi


#10
def get_total_price(l):
    h = 0
    for x in l:
        for a, b in x.items():
            if a == 'price':
                h += b
    return h
print(get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 }
]))

print(get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Cereals", "quantity": 1, "price": 2.50 }
]))
print(get_total_price([
  { "product": "Milk", "quantity": 3, "price": 1.50 }
]))
print(get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Eggs", "quantity": 12, "price": 0.10 },
  { "product": "Bread", "quantity": 2, "price": 1.60 },
  { "product": "Cheese", "quantity": 1, "price": 4.50 }
]))
print(get_total_price([
  { "product": "Chocolate", "quantity": 1, "price": 0.10 },
  { "product": "Lollipop", "quantity": 1, "price": 0.20 }
])) #pricelardi qoshish > 0.30000000000000004


#11
def to_list(l):
    list1 = []
    for x, y in l.items():
        list1.append([x, y])
    return list1


print(to_list({ "a": 1, "b": 2 }))  # ➞ [["a", 1], ["b", 2]]
print(to_list({ "shrimp": 15, "tots": 12 })) #[['shrimp', 15], ['tots', 12]]
print(to_list({})) #[]


#12
def get_student_top_notes(l):
    list5 = []
    list6 = []

    for x in l:
        for d, k in x.items():
            if type(k) == list:
                list6.append(k)

    for z in l:
        list5.append(max(z))
    return list6


print(get_student_top_notes([
  {
    "id": 1,
    "name": "Jacek",
    "notes": [5, 3, 4, 2, 5, 5]
  },
  {
    "id": 2,
    "name": "Ewa",
    "notes": [2, 3, 3, 3, 2, 5]
  },
  {
    "id": 3,
    "name": "Zygmunt",
    "notes": [2, 2, 4, 4, 3, 3]
  }
]))  #➞ [5, 5, 4]


#13
def count_repetitions(lst):
    l = {}
    for x in lst:
        d = lst.count(x)
        l.update({x:d})
    return l

print(count_repetitions(["cat", "dog", "cat", "cow", "cow", "cow"])) #{'cat': 2, 'dog': 1, 'cow': 3}
print(count_repetitions([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0])) #{1: 1, 5: 3, 12: 2, 0: 6}
print(count_repetitions(["Infinity", "null", "Infinity", "null", "null"])) #{'Infinity': 2, 'null': 3}


#14
def checkout(l):
    s = 0
    for x in l:
        for x, y in x.items():
            if type(x) == int and bool:
                s += y
    return s

print(checkout([
  {"desc": "potato chips", "prc": 2, "qty": 2, "taxable": False},
  {"desc": "soda", "prc": 3, "qty": 2, "taxable": False},
  {"desc": "paper plates", "prc": 5, "qty": 1, "taxable": True}
]))  # 15



#15
def keys_and_values(lg10):
    lst = []
    lst1 = []
    lst2 = []
    for x, y in lg10.items():
        lst2.append(y)
        lst1.append(x)
    lst.append(lst1)
    lst.append(lst2)
    return lst


print(keys_and_values({ "a": 1, "b": 2, "c": 3 }))  #➞ [["a", "b", "c"], [1, 2, 3]]
print(keys_and_values({ "a": "Apple", "b": "Microsoft", "c": "Google" })) #[['a', 'b', 'c'], ['Apple', 'Microsoft', 'Google']]
print(keys_and_values({ "key1": True, "key2": False, "key3": True })) # [['key1', 'key2', 'key3'], [True, False, True]]




