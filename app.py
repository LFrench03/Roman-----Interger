import streamlit as st
from IntergerToRoman import intToRoman
from RomanToInterger import romanToInt

st.set_page_config(page_title="Roman Translator", page_icon="img/roman.jpg", layout='centered')


with st.container(border=True):
    with st.expander("**Lore**"):
        tab1, tab2, tab3 = st.tabs(["Origin and Development", "Structure and Rules", "Significance and Legacy"])
        with tab1:
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">The Roman numeral system originated from the Etruscan numerical system, which was later adopted and adapted by the ancient Romans.</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family: sans-serif;font-size:13px;font-weight:bold;">Key points:</p>', unsafe_allow_html=True)
            st.markdown('- <p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">The Etruscans used symbols like I, Λ, X, Ψ, and ⊕ to represent 1, 5, 10, 50, and 1000.</p>', unsafe_allow_html=True)
            st.markdown('- <p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">The Romans took similar-looking letters from their alphabet to represent these values.</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family: sans-serif;font-size:13px;font-weight:bold;">Evolution of the System:</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">The Roman numeral system evolved through several stages. Initially, it was an additive system, similar to the Etruscan system. Around the 3rd century BC, it developed subtractive capabilities, allowing for a more concise representation of numbers. This evolution allowed for abbreviations like IV (4) instead of IIII.</p>', unsafe_allow_html=True)
            st.image("img/imag3.png", use_column_width=True) 
        with tab2:
            st.markdown('<p style="font-family: sans-serif;font-size:13px;font-weight:bold;">The Roman numeral system consists of seven symbols with fixed values:</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">- I (1)</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">- V (5)</p>', unsafe_allow_html=True)    
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">- X (10)</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">- L  (50)</p>', unsafe_allow_html=True)            
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">- C (100)</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">- D (500)</p>', unsafe_allow_html=True)            
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">- M (1000)</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family: sans-serif;font-size:13px;font-weight:bold;">Rules for using these symbols:</p>', unsafe_allow_html=True)
            st.markdown('- <p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">Numbers are composed by adding symbols from right to left.</p>', unsafe_allow_html=True)
            st.markdown('- <p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">When a smaller value symbol appears before a larger one, it means subtraction.</p>', unsafe_allow_html=True)
            st.markdown('- <p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">No symbol can be repeated more than three times in succession.</p>', unsafe_allow_html=True)
            st.image("img/img2.jpg", use_column_width=True) 
            
        with tab3:
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">The Roman numeral system remained in use long after the fall of the Roman Empire. It continued to be used for centuries until it was eventually replaced by Arabic numerals during the Middle Ages due to the influence of Arab empires.</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">In modern times, Roman numerals are still used in certain contexts such as book titles, clock faces, and some formal situations.</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family: sans-serif;font-size:12px;font-weight:bold;color:gray;">This system represents an important milestone in the development of mathematical notation systems, showcasing how cultures adapt and refine numerical representations over time.</p>', unsafe_allow_html=True)
            st.image("img/img4.jpg", use_column_width=True) 
            
                        


    st.image("img/img.jpg", use_column_width=True)
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    with col2:
        subcol1, subcol2, subcol3 = st.columns(3)
        with subcol2:
            st.markdown("")
            toggle = st.toggle("")           
    def cases(toggle):
        if toggle:
            with col1:
                st.markdown('<p style="font-size:20px;text-align:center;font-weight:bold;color:gray;">Interger</p>', unsafe_allow_html=True)                
                input1 = st.text_input("**Enter an interger**", max_chars=4)
            
            with col3:
                st.markdown('<p style="font-size:20px;text-align:center;font-weight:bold;color:gray;">Roman</p>', unsafe_allow_html=True)
                if input1:
                    input1 = int(input1)
                input1 = intToRoman(input1)                   
                st.text_input("**Result**", value=f"{input1}", disabled=True)
        
        else:
            with col1:
                st.markdown('<p style="font-size:20px;text-align:center;font-weight:bold;color:gray;">Roman</p>', unsafe_allow_html=True)
                input2 = st.text_input("**Enter a roman numeral**", max_chars=15)
            
            with col3:
                st.markdown('<p style="font-size:20px;text-align:center;font-weight:bold;color:gray;">Interger</p>', unsafe_allow_html=True)
                input2 = str(input2)
                input2 = romanToInt(input2)                        
                st.text_input("**Result**", value=f"{input2}", disabled=True)
    cases(toggle)