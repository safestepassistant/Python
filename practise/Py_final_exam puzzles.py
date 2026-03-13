


# ----- Python Final Exam -----

# task 1
# ----------------------------------------------------------------------------------------------------
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

# Misollar:
# Kiritish:
# 24
# Natija:
# 6
# (Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)

# Kiritish:
# 502
# Natija:
# 7
# (Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)
# ----------------------------------------------------------------------------------------------------

# task 2
# -----------------------------------------------------------------------------------------------------
#  Define a function `is_prime(n)` which returns `True` if the given n (n > 0) is prime number, otherwise returns `False`.

# ----------------------------------------------------------------------------------------------------

# task 3
# ----------------------------------------------------------------------------------------------------
# 1) Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.

# 2)  Populate your new table with the following values:

# | Name            | Species      | Age |
# |-----------------|--------------|-----|
# | Benjamin Sisko  | Human        |  40 |
# | Jadzia Dax      | Trill        | 300 |
# | Kira Nerys      | Bajoran      |  29 |


# 3)  Display the Name and Age of everyone in the table classified as Bajoran.

# task 4
# -----------------------------------------------------------------------------------------------------

# Update employees.json file by adding new worker's info. (Use Input command to get info)


# task 5
# -----------------------------------------------------------------------------------------------------
# You have a dataset (customer_orders.csv) containing information about customer orders. The dataset has the following columns:

# OrderID: Unique identifier for each order.
# CustomerID: Unique identifier for each customer.
# Product: Name of the product ordered.
# Quantity: Number of units ordered.
# Price: Price per unit.
# Tasks:

# 1)Group the data by CustomerID and filter out customers who have made less than 20 orders.
# 2)Identify customers who have ordered products with an average price per unit greater than $120.   







"""
1. Berilgan butun sonlar massivi nums.
   Agar massiv ichida bir xil son kamida 2 martta uchrasa True, aks holda False qaytaring.

Input: [1,2,3,1]
Output: True

Input: [1,2,3,4]
Output: False
"""



""" 
2. Navbatda odamlarning ro'yxati yani ismi Yoshi va imtiyozi beriladi. Siz esa bu ro'yxatni tartiblashingiz kerak, bunda Yoshi 60 dan kam bo'lmagan yoki imtiyozi borlar oldinga o'tadi , qolganlar esa o'z joyida qolaveradi.

Input:
people = [
    {"ism": "Ali", "yosh": 20, "imtiyoz": False},
    {"ism": "Vali", "yosh": 65, "imtiyoz": False},
    {"ism": "Guli", "yosh": 18, "imtiyoz": True}
]

Output:
Vali Guli Ali

"""


"""
3. Sizga do‘kon tranzaksiyalari saqlangan df DataFrame berilgan.

Har bir chek raqami ketma-ket tartibda bo‘lishi kerak. Ammo ma’lumotlarda ba’zi chek raqamlari yo‘q (missing) bo‘lishi mumkin.

Task:
Python (Pandas) yordamida ketma-ketlikda yetishmayotgan barcha receipt raqamlarini aniqlang.

Rules:
Receipt raqamlari eng kichik receipt dan eng kattasigacha ketma-ket bo‘lishi kerak.
Agar ketma-ketlikda yo‘q raqamlar bo‘lsa, ularni topib qaytaring.
Natijani list yoki DataFrame ko‘rinishida chiqarish mumkin.


df = pd.DataFrame({
    "receipt_no": [1001,1002,1003,1004,1006,1006,1007,1008,1009,1010],
    "amount":     [  10,  15,  20,   5,  50,  50,  10,  25,  30,  40]
})

Expected output: [1005]
"""

"""
4. Python (Pandas) yordamida muzlatkichdagi ingredientlar bilan to‘liq tayyorlash mumkin bo‘lgan barcha taomlarni aniqlang.
   Agar biror taom uchun kerakli ingredientlardan bittasi ham yetishmasa, u taom natijaga kiritilmasin.

recipe = pd.DataFrame({
    "recipe_name": ["hotdog","hotdog","pilov","pilov","pilov","pizza","pizza","pizza"],
    "ingredient_id": [1,2,3,4,5,6,7,8],
    "ingredient_name": ["sausage","bread","rice","carrot","meat","flour","tomato","cheese"]
})

fridge = pd.DataFrame({
    "ingredient_id": [1,2,3,4,6],
    "ingredient_name": ["sausage","bread","rice","carrot","flour"]
})

Expected output: [hotdog]
"""

"""
5. Task: 

Berilgan string s. 
Faqat harf va raqamlarni reverse qiling. 
Belgilar (masalan: !, @, # va boshqalar) o‘z joyida qolishi kerak. 
 
Misol: 
Input: "a!1b@2c" 
Output: "c!2b@1a"
"""



# ----- Python Final Exam -----

# task 1
# ----------------------------------------------------------------------------------------------------
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

# Misollar:
# Kiritish:
# 24
# Natija:
# 6
# (Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)

# Kiritish:
# 502
# Natija:
# 7
# (Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)
# ----------------------------------------------------------------------------------------------------

# task 2
# -----------------------------------------------------------------------------------------------------
#  Define a function is_prime(n) which returns True if the given n (n > 0) is prime number, otherwise returns False.

# ----------------------------------------------------------------------------------------------------

# task 3
# ----------------------------------------------------------------------------------------------------
# 1) Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
# The Name and Species columns should be text fields, and the Age column should be an integer field.

# 2)  Populate your new table with the following values:

# | Name            | Species      | Age |
# |-----------------|--------------|-----|
# | Benjamin Sisko  | Human        |  40 |
# | Jadzia Dax      | Trill        | 300 |
# | Kira Nerys      | Bajoran      |  29 |


# 3)  Display the Name and Age of everyone in the table classified as Bajoran.

# task 4
# -----------------------------------------------------------------------------------------------------

# Update employees.json file by adding new worker's info. (Use Input command to get info)


# task 5
# -----------------------------------------------------------------------------------------------------
# You have a dataset (customer_orders.csv) containing information about customer orders.
# The dataset has the following columns:

# OrderID: Unique identifier for each order.
# CustomerID: Unique identifier for each customer.
# Product: Name of the product ordered.
# Quantity: Number of units ordered.
# Price: Price per unit.
# Tasks:

# 1)Group the data by CustomerID and filter out customers who have made less than 20 orders.
# 2)Identify customers who have ordered products with an average price per unit greater than $120.