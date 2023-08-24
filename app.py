import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


def set_theme():
    # Add custom CSS to set the background color to white
    st.markdown(
        """
        <style>
        body {
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )



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

def plot_potential_energy(r_values, U_values, most_likely_distance, info_text, y_lim):
    plt.figure()
    plt.plot(r_values, U_values)
    plt.xlabel("Distance (m)")
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1e'))
    plt.ylabel("Potential Energy (J)")
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1e'))
    #plt.title("Lennard-Jones Potential Energy")
    plt.axvline(x=most_likely_distance, color='r', linestyle='--', label='Most Likely Distance (r₀)')
    plt.ylim(bottom=min(U_values)-(y_lim), top=max(U_values))
    
    #plt.ylim(bottom=min(U_values) - 1e-30)
    plt.legend()
    plt.grid()
    plt.annotate(info_text, xy=(0.5, 1.02), xycoords="axes fraction", ha="center", fontsize=10, color='black')
    return plt

def fun_delta_U(U_values):
    delta_U = []
    for i in range(1, len(U_values)):
        diff = U_values[i] - U_values[i-1]
        delta_U.append(diff)
    return delta_U

def fun_force(delta_U):
    force = []
    for num in delta_U:
        force.append(-1* (num / 5e-12))
    return force




def plot_force(r_values, F_values,most_likely_distance_force,info_text_force):
    plt.figure()
    plt.plot(r_values, F_values)
    plt.xlabel("Distance (m)")
    #plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1e'))
    plt.ylabel("Force (N)")
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1e'))
    plt.axvline(x=most_likely_distance_force, color='r', linestyle='--', label='Most Likely Distance (r₀)')
    plt.ylim(bottom= None)
    plt.grid()
    #plt.title("Lennard-Jones Force")
    plt.annotate(info_text_force, xy=(0.5, 1.02), xycoords="axes fraction", ha="center", fontsize=10, color='black')
    return plt


def main():
    set_theme()
    
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
        r_start_value = 3.3e-10
        y_lim =1e-22

    elif (roll>=702200011 and roll<=702200020):
        cfrm = "He"
        σ = 0.255e-9
        ε = 7.41e-23 
        r_start_value = 2.4e-10
        y_lim = 1e-23
    elif (roll>=702200021 and roll<=702200030):
        cfrm = "Kr"
        σ = 0.365e-9
        ε = 1.30e-21
        r_start_value = 3.5e-10
        y_lim =1e-22

    elif (roll>=702200031 and roll<=702200040):
        cfrm = "Ne"
        σ = 0.282e-9
        ε = 2.38e-22
        r_start_value = 2.7e-10
        y_lim =1e-23

    elif (roll>=702200041 and roll<=702200050):
        cfrm = "Xe"
        σ = 0.405e-9
        ε = 1.67e-21
        r_start_value = 3.7e-10
        y_lim =5e-22
    elif (roll>=702200051 and roll<=702200060):
        cfrm = "CH30H"
        σ = 0.362e-9
        ε = 3.49e-21
        r_start_value = 3.5e-10
        y_lim =1e-22
    elif (roll>=702200061 and roll<=702200070):
        cfrm = "CH4"
        σ = 0.376e-9
        ε = 1.08e-21
        r_start_value = 3.5e-10
        y_lim =1e-22
    elif (roll>=702200071 and roll<=702200080):
        cfrm = "CO"
        σ = 0.369e-9
        ε = 6.65e-22
        r_start_value = 3.5e-10
        y_lim =1e-22
    elif (roll>=702200081 and roll<=702200090):
        cfrm = "CO2"
        σ = 0.394e-9
        ε = 1.41e-21
        r_start_value = 3.7e-10
        y_lim =1e-22
    else:
        cfrm = "Air"
        σ = 0.371e-9 
        ε = 5.65e-22
        r_start_value = 3.3e-10
        y_lim =1e-22

    #r_start_value = 1e-10
    r_end_value = 6.45e-10
    if give_answer == "Rhoda":
        st.title("RHODA🍵")
    
    elif give_answer =="Shagun":
        st.title("KHUD KRLE APNA, hehehe")
        
        
    else:
        # σ = 2.63e-10
        # ε = 1.51e-10
        # r_start_value = 2.5e-10
        r_end_value = 7.45e-10
        r_values = funr_values(r_start_value, r_end_value)
        U_values = [lennard_jones_potential(r, ε, σ) for r in r_values]
        min_energy_index = np.argmin(U_values)
        most_likely_distance = r_values[min_energy_index]

        ## Calculating force
        delta_U = fun_delta_U(U_values)
        force = fun_force(delta_U)

        ## Plotting the Potential vs r curve.
        info_text = f"Chemical Formula: {cfrm}\nSigma: {σ}\nEpsilon: {ε}\n Most likely distance:-{most_likely_distance}m\nName: {name}\nRoll Number: {roll}\nSubgroup: {sgrp}"

        plot = plot_potential_energy(r_values, U_values, most_likely_distance, info_text,y_lim)
        st.pyplot(plot)  # Display the plot using st.pyplot()

        ##Implementing psswd for Q2
        st.markdown("<h3 style='text-align: center; color: black;'>Enter password to access Q2 </h3>", unsafe_allow_html=True)
        
        psswd = st.text_input("Enter password")

        st.markdown("<h3 style='text-align: center; color: black;'>To find password click <a href='https://github.com/RAJAT-COD3/lennard_jones_potential' style='color: blue;'>here</a>:</h3>", unsafe_allow_html=True)

        if psswd == "Star the repo":
         

            if (roll>=702200001 and roll<=702200010):
                cfrm = "Ar"
                σ = 0.354e-9
                ε = 6.76e-22
                r_start_value = 3.8e-10
                r_end_value = 7.5e-10

            elif (roll>=702200011 and roll<=702200020):
                cfrm = "He"
                σ = 0.255e-9
                ε = 7.41e-23 
                r_start_value = 2.4e-10
                r_end_value = 6.5e-10
            elif (roll>=702200021 and roll<=702200030):
                cfrm = "Kr"
                σ = 0.365e-9
                ε = 1.30e-21
                r_start_value = 3.6e-10
                r_end_value = 7.5e-10

            elif (roll>=702200031 and roll<=702200040):
                cfrm = "Ne"
                σ = 0.282e-9
                ε = 2.38e-22
                r_start_value = 2.7e-10
                r_end_value = 6.5e-10

            elif (roll>=702200041 and roll<=702200050):
                cfrm = "Xe"
                σ = 0.405e-9
                ε = 1.67e-21
                r_start_value = 4e-10
                r_end_value = 7.5e-10
            elif (roll>=702200051 and roll<=702200060):
                cfrm = "CH30H"
                σ = 0.362e-9
                ε = 3.49e-21
                r_start_value = 3.6e-10
                r_end_value = 6.5e-10
            elif (roll>=702200061 and roll<=702200070):
                cfrm = "CH4"
                σ = 0.376e-9
                ε = 1.08e-21
                r_start_value = 3.9e-10
                r_end_value = 6.5e-10
            elif (roll>=702200071 and roll<=702200080):
                cfrm = "CO"
                σ = 0.369e-9
                ε = 6.65e-22
                r_start_value = 3.5e-10
                r_end_value = 7.5e-10
            elif (roll>=702200081 and roll<=702200090):
                cfrm = "CO2"
                σ = 0.394e-9
                ε = 1.41e-21
                r_start_value = 3.7e-10
                r_end_value = 6.5e-10
            else:
                cfrm = "Air"
                σ = 0.371e-9 
                ε = 5.65e-22
                r_start_value = 3.7e-10
                r_end_value = 6.5e-10
            #r_end_value = 7.5e-10

            # r_start_value = 2.5e-10
            # σ = 2.63e-10
            # ε = 1.51e-10
            

            r_values = funr_values(r_start_value, r_end_value)
            U_values = [lennard_jones_potential(r, ε, σ) for r in r_values]
            delta_U = fun_delta_U(U_values)
            force = fun_force(delta_U)
            
            min_force_index = np.argmin(force)
            most_likely_distance_force = r_values[min_force_index+1]

            info_text_force = f"Minimum force is at:-{most_likely_distance_force}m"
            

            
            
            plot_F = plot_force(r_values[1:], force,most_likely_distance_force,info_text_force)

            st.text("")
            st.text("")
            st.text("")
            st.text("")

            st.markdown("<h3 style='text-align: center; color: black;'>Force vs distance curve</h3>", unsafe_allow_html=True)
            st.pyplot(plot_F)
    
            #st.write(force[min_force_index])

        elif psswd != "Star the repo":
            st.markdown("<h4 style='text-align: center; color: black;'>Incorrect password, try agin</h4>", unsafe_allow_html=True)

        




        
       
        

        
if __name__ == "__main__":
    main()
