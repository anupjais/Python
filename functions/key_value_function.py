# TYPE 1
# def key_val(name, power):
#     print("Name:-",name,"Power:-",power)

# # print(key_val(name="Krishna",power="Sudarsan"))
# key_val(name="Kanhaiya",power="Kindness")
# key_val(power="Empowerment",name="Modi")

# TYPE 2
# def key_val(**kwargs):
#     for key, val in kwargs.items():
#         print(f"{key}:{val}")

# key_val(name="Hanuman", power="Infinity")
# key_val(name="Hanuman")
# key_val(name="Shaktiman",power="Chakra", enemy="Dr. Jackaal")


# TYPE 3
def key_val(**kwargs):
    for key, val in kwargs.items():
        print(f"Name:{key}, Power:{val}")

key_val(name="Hanuman", power="Infinity")
key_val(name="Hanuman")
key_val(name="Shaktiman",power="Chakra", enemy="Dr. Jackaal")
