import customtkinter as ctk


ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("Velocity Calculator")
app.geometry("600x500")


def calculate_velocity():
    try:
        out = float(entry_maxout.get())
        inn = float(entry_maxin.get())
        velo = out - inn
        rovelo = velo / 2
        result_label.configure(text=f"Estimated Velocity: {velo:.2f} mph\n"
                                    f"Rotational Velocity: {rovelo:.2f} mph", text_color="green")
    except ValueError:
        result_label.configure(text="Invalid input. Enter valid numbers.", text_color="red")

# GUI Elements
title_label = ctk.CTkLabel(app, text="Tornado Velocity Estimate", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=10)

entry_maxout = ctk.CTkEntry(app, placeholder_text="Enter Max-out Velocity")
entry_maxout.pack(pady=10)

entry_maxin = ctk.CTkEntry(app, placeholder_text="Enter Max-in Velocity")
entry_maxin.pack(pady=20)

calculate_button = ctk.CTkButton(app, text="Calculate", command=calculate_velocity)
calculate_button.pack(pady=30)

result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
result_label.pack(pady=10)


app.mainloop()