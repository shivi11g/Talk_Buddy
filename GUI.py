import tkinter
import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image




customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

purple = "#8a2be2"


def button_callback():
    print("button clicked")

#---root---

app = customtkinter.CTk()

app.title("Virtual assistant")
app.geometry("1100x600")
#-------------

#--------label---------
label = customtkinter.CTkLabel(app, text="Virtual Assistant", fg_color="transparent",  width=150 , height= 50, font=("Arial", 30))
label.pack(padx=20, pady = 20)
#-------------

#main frame
main_frame = customtkinter.CTkFrame(master=app)
main_frame.pack(pady=20, padx=60, fill="both", expand=True)



# left frame
left_frame = customtkinter.CTkFrame(main_frame)
left_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

#label of frame
labelleft = customtkinter.CTkLabel(left_frame, text="Command Window", fg_color="transparent",  width=50 , height= 20, font=("Arial", 15))
labelleft.pack(padx=10, pady = 10)

#childScrollabeFrame
leftchild_frame = customtkinter.CTkScrollableFrame(left_frame)
leftchild_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)




# right frame
right_frame = customtkinter.CTkFrame(main_frame, bg_color = "black")
right_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

#label of right frame
labelright = customtkinter.CTkLabel(right_frame, text="Output Window", fg_color="transparent",  width=50 , height= 20, font=("Arial", 15))
labelright.pack(padx=10, pady = 10)

#childScrollabeFrame
leftchild_frame = customtkinter.CTkScrollableFrame(right_frame)
leftchild_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)



# Load the microphone image
mic_image = Image.open("assets/microphone2.png")
mic_image = mic_image.resize((40, 40))  # Resize the image as needed
mic_icon = ImageTk.PhotoImage(mic_image)

# Create the circular button
mic_button = customtkinter.CTkButton(app, image=mic_icon, text = "give command", command=button_callback)
mic_button.pack(padx=20, pady=20)

#--------button-----
# button = customtkinter.CTkButton(app, text="my button", command=button_callback)
# button.pack(padx=20, pady=20)
#------------------



app.mainloop()