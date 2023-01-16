import os
import tkinter as tk
from tkinter import *
from AnotherHuffman import AnotherHuffman
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.resizable(False, False)

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label=customtkinter.CTkLabel(master=frame, text="Huffman Encoding")
label.pack(pady=12, padx=10)
root.title("HUFFMAN ENCODING IMPLEMENTATION")

textbox_encode=customtkinter.CTkTextbox(master=frame, height=50, width=300 ,font=('Arial', 14))
textbox_encode.pack(padx=10, pady=10)

H=AnotherHuffman()

def click_encode():
    H.heap.clear()
    H.reverse_mapping.clear()
    H.codes.clear()
    sampleFile=os.path.isfile("sample.txt")
    binFile=os.path.isfile("sample.bin")
    outputFile=os.path.exists("output.txt")

    if(sampleFile):
        os.remove("sample.txt")
    if(binFile):
        os.remove("sample.bin")
    if(outputFile):
        os.remove("output.txt")

    clear_field()
    text = textbox_encode.get("1.0", END)
    create_files(text)

    H.define_path("sample.txt")
    H.compress()

    res=H.get_encoded_string()
    textbox_encoded.insert("1.0", res)

    textbox_encode.delete("1.0", END)

def click_decode():
    H.decompress("sample.bin")
    dec_sring=H.get_decompressed_string()

    textbox_decoded.insert("1.0", dec_sring)
    textbox_encoded.delete("1.0", END)

def create_files(text):
    f = open("sample.txt", "w")
    f.write(text)
    f.close()

    fb= open("sample.bin", "wb")
    fb.close()

    fo=open("output.txt", "w")
    fo.close()

def clear_field():
    textbox_encoded.delete("1.0", END)

def clear_all_fields():
    textbox_encode.delete("1.0", END)
    textbox_encoded.delete("1.0", END)
    textbox_decoded.delete("1.0", END)
    H.heap.clear()
    H.reverse_mapping.clear()
    H.codes.clear()

def delete_all_files():
    os.remove("sample.txt")
    os.remove("sample.bin")
    os.remove("output.txt")

encode_button = customtkinter.CTkButton(master=frame, text="Encode", font=('Arial', 14), command=click_encode)
encode_button.pack(padx=10, pady=10)

textbox_encoded=customtkinter.CTkTextbox(master=frame, height=50, width=300 ,font=('Arial', 9))
textbox_encoded.pack(padx=10, pady=10)

decode_button = customtkinter.CTkButton(master=frame, text="Decode", font=('Arial', 14), command=click_decode)
decode_button.pack(padx=10, pady=10)

textbox_decoded=customtkinter.CTkTextbox(master=frame, height=50, width=300, font=('Arial', 14))
textbox_decoded.pack(padx=10, pady=10)

clear_btn=customtkinter.CTkButton(master=frame, text="Clear", font=('Arial', 14), command=clear_all_fields)
clear_btn.pack(padx=10, pady=10)

root.mainloop()


