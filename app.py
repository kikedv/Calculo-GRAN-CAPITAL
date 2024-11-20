# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:48:06 2024

@author: valde
"""

import streamlit as st

def calculate_savings(target_capital, initial_capital, years, annual_rate, inflation_rate, tax_rate):
    """
    Calcula el ahorro/inversión anual necesario ajustando por inflación y considerando impuestos.
    """
    # Ajustar el capital objetivo por inflación
    inflation_rate = inflation_rate / 100
    target_capital_adjusted = target_capital * (1 + inflation_rate) ** years

    # Calcular el ahorro/inversión anual necesario
    annual_rate = annual_rate / 100
    tax_rate = tax_rate / 100
    effective_rate = annual_rate * (1 - tax_rate)  # Ajuste por impuestos

    numerator = target_capital_adjusted - (initial_capital * (1 + effective_rate) ** years)
    denominator = ((1 + effective_rate) ** years - 1) / effective_rate if effective_rate != 0 else 0
    
    if denominator != 0:
        annual_savings = numerator / denominator
    else:
        annual_savings = 0
    
    return round(annual_savings, 2), round(target_capital_adjusted, 2)

# Configuración de la página
st.title("Calculadora de Gran Capital (Ajustada por Inflación e Impuestos)")
st.markdown("Calcule cuánto necesita ahorrar o invertir anualmente para alcanzar su **Gran Capital**, ajustado por inflación y considerando impuestos.")

# Formulario de entrada
target_capital = st.number_input("Gran Capital Deseado", min_value=0.0, step=1000.0)
initial_capital = st.number_input("Capital Inicial", min_value=0.0, step=1000.0)
years = st.number_input("Número de Años", min_value=1, step=1)
annual_rate = st.number_input("Tasa de Rentabilidad Anual (%)", min_value=0.0, step=0.1)
inflation_rate = st.number_input("Tasa de Inflación Esperada Anual (%)", min_value=0.0, step=0.1)
tax_rate = st.number_input("Tasa de Impuestos sobre las Ganancias (%)", min_value=0.0, step=0.1)

# Botón para calcular
if st.button("Calcular"):
    if target_capital > 0 and years > 0:
        annual_savings, adjusted_capital = calculate_savings(
            target_capital, initial_capital, years, annual_rate, inflation_rate, tax_rate
        )
        st.success(f"El ahorro/inversión anual necesario es: ${annual_savings}")
        st.info(f"El Gran Capital ajustado por inflación será: ${adjusted_capital}")
    else:
        st.error("Por favor, asegúrese de ingresar valores válidos para todos los campos.")

st.markdown("---")
st.markdown("Desarrollado por **Tu Nombre**")
