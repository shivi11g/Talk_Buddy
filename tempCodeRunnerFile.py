# right frame
right_frame = customtkinter.CTkFrame(main_frame, bg_color = "#FFD700")
right_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

#label of right frame
labelright = customtkinter.CTkLabel(right_frame, text="Output Window", fg_color="transparent",  width=50 , height= 20, font=("Arial", 15))
labelright.pack(padx=20, pady = 20)

#childScrollabeFrame
rightchild_frame = customtkinter.CTkScrollableFrame(right_frame)
rightchild_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

#label of scrollableFrame
scrollableRightContent = customtkinter.CTkLabel(rightchild_frame, text = "hello world", fg_color="transparent",  width=50 , height= 20, font=("Arial", 15), wraplength=300)
print("checking error")
scrollableRightContent.pack(padx=10, pady = 10)