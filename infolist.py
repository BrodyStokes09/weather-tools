import customtkinter as ctk

#Setup
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Storms of Interest")
app.geometry("600x500")

#Data list
storm_data = []  # This will store (location, windspeed) tuples

#Functions
def add_data():
    location = entry_location.get()
    windspeed = entry_windspeed.get()

    if location and windspeed:
        try:
            windspeed = float(windspeed)
            storm_data.append((location, windspeed))
            update_display()
            entry_location.delete(0, ctk.END)
            entry_windspeed.delete(0, ctk.END)
        except ValueError:
            result_label.configure(text="Please enter a valid number for windspeed.")
    else:
        result_label.configure(text="Please fill in both fields.")

def save_to_file():
    if not storm_data:
        result_label.configure(text="No data to save.")
        return
    try:
        with open("storm_data.txt", "w") as f:
            for location, windspeed in storm_data:
                f.write(f"{location} - {windspeed} mph\n")
        result_label.configure(text="Data saved to storm_data.txt")
    except Exception as e:
        result_label.configure(text=f"Error saving file: {e}")

def clear_data():
    storm_data.clear()
    update_display()
    result_label.configure(text="Data cleared.")

def update_display():
    display_text = "\n".join([f"{loc} - {spd} mph" for loc, spd in storm_data])
    result_label.configure(text=display_text or "No data added yet.")

#Format
title_label = ctk.CTkLabel(app, text="Storms of Interest", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=10)

entry_location = ctk.CTkEntry(app, placeholder_text="Enter Location of Storm")
entry_location.pack(pady=10)

entry_windspeed = ctk.CTkEntry(app, placeholder_text="Enter Estimated Windspeed (mph)")
entry_windspeed.pack(pady=10)

button_add = ctk.CTkButton(app, text="Add Storm Data", command=add_data)
button_add.pack(pady=10)

button_save = ctk.CTkButton(app, text="Save to File", command=save_to_file)
button_save.pack(pady=10)

button_clear = ctk.CTkButton(app, text="Clear All Data", command=clear_data)
button_clear.pack(pady=10)

result_label = ctk.CTkLabel(app, text="No data added yet.", font=ctk.CTkFont(size=14), justify="left")
result_label.pack(pady=20)

app.mainloop()