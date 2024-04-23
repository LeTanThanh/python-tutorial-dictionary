if __name__ == "__main__":
  # Introduction to the Python Dictionary type
  empty_dict = {}
  print(empty_dict)
  print(type(empty_dict))

  person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True
  }
  print(person)

  # Accessing values in a Dictionary

  ## 1. Using square bracket notation
  """
  dict[key]
  """

  person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True
  }
  print(person["first_name"])
  print(person["last_name"])

  ## 2. Using the get() method

  person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True
  }
  # ssn = person["ssn"]
  # KeyError

  ssn = person.get("ssn")
  print(ssn)

  ssn = person.get("ssn", "000-00-0000")
  print(ssn)

  # Adding new key-value pairs

  person["gender"] = "Female"
  print(person)

  # Modifying value in a key0value pair

  """
  dict[key] = new_value
  """

  person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True
  }
  person["age"] = 26
  print(person)

  # Removing key-value pairs

  """
  del dict[key]
  """

  person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True
  }
  del person["active"]
  print(person)

  # Looping through a dictionary

  ## 1. Looping all key-value pairs in a dictionary

  person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True
  }
  print(person.items())

  for key, value in person.items():
    print(f"{key}: {value}")

  ## 2. Looping all keys in a dictionary

  person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True
  }

  for key in person.keys():
    print(key)

  for key in person:
    print(key)

  ## 2. Looping all values in a dictionary

  person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True
  }

  for value in person.values():
    print(value)
