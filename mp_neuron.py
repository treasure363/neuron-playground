import streamlit as st
import itertools
import pandas as pd
from truth_table import compute_result

def mp_neuron(x, w):
  return sum([x[i]*w[i] for i in range(len(x))])

def generate_diagram(inputs, weights, theta):
    weighted_sum = 0.0
    diagram = "Inputs       Weights         Neuron              Output\n"
    diagram += "                         ┌───────────┐\n"
    diagram += f"                         │           │\n"
    for i in range(len(inputs)):
      diagram += f"  {inputs[i]} ─────x{i+1}────[{weights[i]}]──────►│   {inputs[i]}*{weights[i]}={inputs[i]*weights[i]}   │\n"
      diagram += f"                         │           │\n"
      weighted_sum += inputs[i]*weights[i]
    diagram += f"                         │ Sum: {weighted_sum}  │\n"
    diagram += "                         └───────────┘\n"
    diagram += "                               │\n"
    diagram += f"                             θ: {theta}\n"
    return diagram

def main():
  st.header("MP Neuron")

  num_inputs = st.number_input("Enter number of inputs", min_value=1, max_value=10, value=1, step=1)

  st.subheader("Input Bits and Weights")

  input_bits = []
  weight_inputs = []

  for i in range(num_inputs):
    col1, col2 = st.columns(2)

    with col1:
      bit = st.number_input(f"Input Bit {i + 1}", min_value=0, max_value=10, value=0, step=1)
      input_bits.append(bit)

    with col2:
      weight_input = st.number_input(f"Weight {i + 1}", min_value=-10, max_value=10, value=1, step=1)
      weight_inputs.append(weight_input)

  with st.columns([1, 2, 1])[1]:
    theta = st.number_input("Enter Threshold (Theta)", min_value=-10, max_value=10, value=1, step=1)

  bit_combinations = list(itertools.product([0, 1], repeat=num_inputs))

  gate_type = st.selectbox("Select a logic gate:", ["AND", "OR", "NAND", "NOR", "XOR", "ANDNOT"])
  input_type = st.selectbox("Input Type", ["Binary Data (0, 1)", "Bipolar Data (-1, 1)"])

  if input_type == "Bipolar Data(-1, 1)":
    bit_combinations = [[1 if b else -1 for b in comb] for comb in bit_combinations]

  results = [mp_neuron(x, weight_inputs) for x in bit_combinations]
  if input_type == "Bipolar Data (-1, 1)":
    results = [-1 if r == 0 else 1 for r in results]

  st.subheader("MP Neuron Calculation")

  columns = []
  for i in range(num_inputs):
    columns.append(f"X{i+1}")
    columns.append(f"W{i+1}")
  columns.append("Weighted Sum")
  columns.append(f"{gate_type} GATE")

  data = []
  for comb, weighted_sum in zip(bit_combinations, results):
    temp = []
    for x, w in zip(comb, weight_inputs):
      temp.append(x)
      temp.append(w)
    temp.append(weighted_sum)
    temp.append(compute_result(gate_type, comb))
    data.append(temp)


  df = pd.DataFrame(data, columns=columns)

  st.table(df)


  st.subheader("MP Neuron Diagram")

  diagram_container = st.empty()

  diagram = generate_diagram(input_bits, weight_inputs, theta)
  diagram_container.code(diagram, language='python')

  st.subheader("Reference Truth Table")

  results = [compute_result(gate_type, comb) for comb in bit_combinations]
  if input_type == "Bipolar Data (-1, 1)":
    results = [-1 if r == 0 else 1 for r in results]

  columns = [f"Input {i+1}" for i in range(num_inputs)]
  columns.append("Output")
  data = [list(comb) + [res] for comb, res in zip(bit_combinations, results)]
  df = pd.DataFrame(data, columns=columns)

  st.table(df)

  st.markdown("""
  <style>
    .stButton > button {
        background-color: #f39c12;
        color: white;
        font-size: 16px;
    }
    .stNumberInput > div > div > input {
        background-color: #ecf0f1;
    }
  </style>
  """, unsafe_allow_html=True)
