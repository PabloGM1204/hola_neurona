import streamlit as st


# Título y descripción
st.title("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.header("Una neurona con una entrada y un peso")
    w = st.slider("Peso", min_value=0.00, max_value=10.0, value=5.0, step=0.01)
    x = st.number_input("Introduzca el valor de la entrada", value=0.0)

    if st.button("Calcular la salida", key="calcular_salida_tab1"):
        y = w * x
        st.write("La salida de la neurona es ", y)

with tab2:
    st.header("Una neurona con dos entradas y dos pesos")
    col1, col2 = st.columns(2)
    with col1:
        w0 = st.slider("Peso W0", min_value=0.00, max_value=10.0, value=5.0, step=0.01)
        x0 = st.number_input("Introduzca el valor de la entrada X0", value=0.0)
    with col2:
        w1 = st.slider("Peso W1", min_value=0.00, max_value=10.0, value=5.0, step=0.01)
        x1 = st.number_input("Introduzca el valor de la entrada X1", value=0.0)

    if st.button("Calcular la salida", key="calcular_salida_tab2"):
        y = w0 * x0 + w1 * x1
        st.write("La salida de la neurona es ", y)

with tab3:
    st.header("Una neurona con tres entradas, tres pesos y un sesgo")
    col1, col2, col3 = st.columns(3)
    with col1:
        w0 = st.slider("Peso W0 ", min_value=0.00, max_value=10.0, value=1.0, step=0.01)
        x0 = st.number_input("Introduzca el valor de la entrada X0 ", value=0.0)
    with col2:
        w1 = st.slider("Peso W1 ", min_value=0.00, max_value=10.0, value=2.0, step=0.01)
        x1 = st.number_input("Introduzca el valor de la entrada X1 ", value=0.0)
    with col3:
        w2 = st.slider("Peso W2 ", min_value=0.00, max_value=10.0, value=3.0, step=0.01)
        x2 = st.number_input("Introduzca el valor de la entrada X2 ", value=0.0)

    b = st.number_input("Introduzca el valor del sesgo", value=10.0)

    if st.button("Calcular la salida", key="calcular_salida_tab3"):
        y = w0 * x0 + w1 * x1 + w2 * x2 + b
        st.write("La salida de la neurona es ", y)
