def AND_gate(inputs):
  return int(all(inputs))

def OR_gate(inputs):
  return int(any(inputs))

def NAND_gate(inputs):
  return int(not all(inputs))

def NOR_gate(inputs):
  return int(not any(inputs))

def XOR_gate(inputs):
  return int(inputs.count(1) % 2 == 1)

def ANDNOT_gate(inputs):
  return int(all(inputs[:-1]) and (not inputs[-1]))

def compute_result(gate, inputs):
  if gate == "AND":
    return AND_gate(inputs)
  elif gate == "OR":
    return OR_gate(inputs)
  elif gate == "NAND":
    return NAND_gate(inputs)
  elif gate == "NOR":
    return NOR_gate(inputs)
  elif gate == "XOR":
    return XOR_gate(inputs)
  elif gate == "ANDNOT":
    return ANDNOT_gate(inputs)
