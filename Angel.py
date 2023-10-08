
import streamlit as st

# Functions
def func_velocity(distance, time):
    return ((distance * 1852) / (time * 60))/0.514

def func_distance(velocity, time):
    return ((velocity * 0.514) * (time * 60))/1852

def func_time(velocity, distance):
    return ((distance * 1852) / (velocity * 0.514))/60

# Application heading
st.title("Aerocalculadora")
st.markdown("**INSTRUCIONES** - Rellena dos de los apartados y deja una incógnita. La incognita vacía será la que se calculara. ")

st.title("Tabla")

velocity = st.text_input("Velocidad (Nudos)")
distance = st.text_input("Distancia (Millas Nauticas)")
time = st.text_input("Tiempo (minutos)")


if st.button("Calcular"):
    if not velocity:
        distance = float(distance)
        time = float(time)
        velocity = func_velocity(distance, time)
        velocityround = round(velocity, 2)
        st.success(f"Velocidad: {velocityround} Nudos")
    elif not distance:
        velocity = float(velocity)
        time = float(time)
        distance = func_distance(velocity, time)
        distanceround = round(distance, 2)
        st.success(f"Distancia: {distanceround} Millas Náuticas")
    elif not time:
        velocity = float(velocity)
        distance = float(distance)
        time = func_time(velocity, distance)
        timeround = round(time, 2)
        hours = time / 60
        hoursround = round(hours, 2)
        st.success(f"Tiempo: {timeround} minutos, {hoursround} horas")
                
    else:
        st.error("TRIPLE INPUT")
        st.info("Error: Debes dejar una incógnita vacía para el cálculo.")
        
