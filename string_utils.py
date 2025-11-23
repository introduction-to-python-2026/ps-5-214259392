


def split_before_each_uppercases(formula):
  start_index = 0
  split_formula = [] 
  for end_index in range(1,len(formula)) :
    char = formula[end_index]

    if char.isupper():
        substring = formula [start_index:end_index]
        split_formula.append(substring)
        start_index = end_index 
  if start_index < len(formula):
        last_part = formula[start_index:]
        split_formula.append(last_part)    
       
  return split_formula

def split_at_first_digit(formula):
  digit_location= 0
  for Key in formula:
      if Key.isdigit():
        break
      digit_location += 1

      if digit_location == len(formula):
         return formula, 1
  prefix = formula[0:digit_location]
  number_str = formula[digit_location:]
  return prefix, int(number_str)

def count_atoms_in_molecule(molecular_formula):
  atoms_dict = {}
  parts = split_before_each_uppercases(molecular_formula)
  
  for part in parts:
    atom_name, count = split_at_first_digit(part)
    atom_dict[atom_name] = atom_dict.get(atom_name, 0) + count 
  
  return atoms_dict  



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
