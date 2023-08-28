import random

def generate_fake_name():
  """Generates a fake name."""
  first_name_list = ["John", "Jane", "Mary", "Peter", "Paul", "David","Jonas"]
  last_name_list = ["Smith", "Jones", "Williams", "Brown", "Davis", "Wilson"]
  first_name = random.choice(first_name_list)
  last_name = random.choice(last_name_list)
  return first_name + " " + last_name

if __name__ == "__main__":
  print(generate_fake_name())
