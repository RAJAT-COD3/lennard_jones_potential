import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def lennard_jones_potential(r, ε, σ):
    return 4 *ε * ((σ / r)**12 - (σ / r)**6)

def funr_values(r_start_value , r_end_value):
    increment = 0.05e-10
    r_values = []
    current_value = r_start_value
    while current_value <= r_end_value:
        r_values.append(current_value)
        current_value += increment
    
    return r_values

def main():
    
    give_answer = "Yes"

    st.markdown("<h1 style='text-align: center; color: black;'>Made with ❤️ by Rajat Goyal</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Lennard-Jones Potential Energy </h2>", unsafe_allow_html=True)
    
    roll = st.number_input("Enter your roll number", step = 1)
    sgrp = st.text_input("Enter your subgroup")
    name = st.text_input("Enter your name")

    if roll == 702200065:
        give_answer = "Rhoda"
    
    elif roll == 702200092:
        give_answer = "Shagun"

    elif (roll>=702200001 and roll<=702200010):
        cfrm = "Ar"
        σ = 0.354e-9
        ε = 6.76e-22

    elif (roll>=702200011 and roll<=702200020):
        cfrm = "He"
        σ = 0.255e-9
        ε = 7.41e-23
    elif (roll>=702200021 and roll<=702200030):
        cfrm = "Kr"
        σ = 0.365e-9
        ε = 1.30e-21

    elif (roll>=702200031 and roll<=702200040):
        cfrm = "Ne"
        σ = 0.282e-9
        ε = 2.38e-22

    elif (roll>=702200041 and roll<=702200050):
        cfrm = "Xe"
        σ = 0.405e-9
        ε = 1.67e-21
    elif (roll>=702200051 and roll<=702200060):
        cfrm = "CH30H"
        σ = 0.362e-9
        ε = 3.49e-21
    elif (roll>=702200061 and roll<=702200070):
        cfrm = "CH4"
        σ = 0.376e-9
        ε = 1.08e-21
    elif (roll>=702200071 and roll<=702200080):
        cfrm = "CO"
        σ = 0.369e-9
        ε = 6.65e-22
    elif (roll>=702200081 and roll<=702200090):
        cfrm = "CO2"
        σ = 0.394e-9
        ε = 1.41e-21
    else:
        cfrm = "Air"
        σ = 0.371e-9 
        ε = 5.65e-22

    # σ = 2.63e-10
    # ε = 6.04e-22

    st.write("value of sigma",σ,"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","Chemical formula:-",cfrm,"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" ,"value of epsilen",ε )
    
    st.write("Roll number :- ",roll,"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","Name:-",name,"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","subgroup:-",sgrp)
   

    r_start_value = 1e-10
    r_end_value = 7.45e-10
    if give_answer == "Rhoda":
        st.title("RHODA🍵")
    
    elif give_answer =="Shagun":
        st.title("KHUD KRLE APNA, hehehe")
        
        
    else:
        r_values = funr_values(r_start_value , r_end_value)
        U_values = [lennard_jones_potential(r, ε, σ) for r in r_values]
        min_energy_index = np.argmin(U_values)
        most_likely_distance = r_values[min_energy_index]

        #st.pyplot(plot_potential_energy(r_values, U_values, most_likely_distance))

        st.write("Most Likely Distance:", most_likely_distance, "nm")
        #st.write(r_values[1],r_values[30],r_values[100])
        st.write("minimun energy",U_values[min_energy_index])

        

    def plot_potential_energy(r_values, U_values, most_likely_distance):
        plt.figure()
        plt.plot(r_values, U_values)
        plt.xlabel("Distance (nm)")
        plt.ylabel("Potential Energy (J)")
        plt.title("Lennard-Jones Potential Energy")
        plt.axvline(x=most_likely_distance, color='r', linestyle='--', label=f"Most Likely Distance: {most_likely_distance:.3f} nm")
        plt.ylim(bottom=min(U_values) - 1e-30)
        plt.legend()
        plt.grid()
        return plt
    st.pyplot(plot_potential_energy(r_values, U_values, most_likely_distance))

if __name__ == "__main__":
    main()
