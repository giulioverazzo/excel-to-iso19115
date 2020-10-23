
def camelize(string):
  # remove leading and trailing white space
  string = string.strip()

  # lowercase everything
  string = string.lower()

  # Split on all spaces
  string = string.split(" ")

  # capitalize first letter of all except first item
  capitalized = list(map((lambda x: x.capitalize()),string[1:]))

  camelized = string[0]+"".join(capitalized)
  return camelized
