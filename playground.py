import streamlit as st
import mp_neuron

st.title("Neuron Experiment Playground")

option = st.sidebar.selectbox(
  "Choose a Neuron Type",
  ("MP Neuron", "Perceptron", "Adding More...")
)

if option == "MP Neuron":
  mp_neuron.main()
elif option == "Perceptron":
  st.header("Perceptron")
  st.text("Coming Soon...")
else:
  st.text("Coming Soon...")
