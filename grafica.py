import customtkinter  as ctk

root = ctk.CTk()

root.minsize(600,500)

frame = ctk.CTkFrame(root)

frame.grid(column=0, row=0, sticky="nsew",padx = 10,pady = 10)

frame.columnconfigure([0,1],weight=1)

frame.rowconfigure([0,1,2,3,4,5],weight=1)

root.columnconfigure(0,weight=1)

root.rowconfigure(0,weight=1)
ctk.CTkLabel(frame, text="Hestia",height=40,width=25).grid(columnspan = 2, row = 0)

text = ctk.CTkEntry(frame)
text.grid(columnspan = 2, row=1,padx = 4, pady = 4)
root.mainloop()