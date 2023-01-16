import os
import tkinter as tk
from tkinter import *
from AnotherHuffman import AnotherHuffman
import time

root = tk.Tk()

root.geometry("400x600")
root.title("HUFFMAN ENCODING IMPLEMENTATION")

label=tk.Label(root, text="Let's Decode and Encode!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox_encode=tk.Text(root, height=3 ,font=('Arial', 14))
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

encode_button = tk.Button(root, text="Encode", font=('Arial', 14), command=click_encode)
encode_button.pack(padx=10, pady=10)

textbox_encoded=tk.Text(root, height=7 ,font=('Arial', 9))
textbox_encoded.pack(padx=10, pady=10)

decode_button = tk.Button(root, text="Decode", font=('Arial', 14), command=click_decode)
decode_button.pack(padx=10, pady=10)

textbox_decoded=tk.Text(root, height=4, font=('Arial', 14))
textbox_decoded.pack(padx=10, pady=10)

clear_btn=tk.Button(root, text="Clear", font=('Arial', 14), command=clear_all_fields)
clear_btn.pack(padx=10, pady=10)

anotherBtn=tk.Button

root.mainloop()


