import requests, io, os
import matplotlib.pyplot as plt
from PIL import Image
# Source - https://stackoverflow.com/a/3964691
# Posted by ghostdog74, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-30, License - CC BY-SA 4.0
files = []
txt_file_name = None
for file in os.listdir(os.getcwd() + "\\python_code"): # Could need to change depending on path <-------------
    if file.endswith(".txt"):
        files.append(file)
        print(file)
print("Write which txt file you want to use of the above or 'q' to quit. Example: 'example.txt'")
while txt_file_name not in files:
    if txt_file_name != None:
        print("invalid input")
    txt_file_name = input()
    if txt_file_name == "q":
        exit()
txt_dir = os.getcwd() + "\\python_code\\" + txt_file_name # Could need to change depending on path <-------------

with open(txt_dir) as f:
    txt_arr = f.read().split()

value_arr = []
for str in txt_arr:
    value_arr.append(str.split(";"))

cansat_t = [float(x[1]) for x in value_arr]
cansat_p = [float(x[2]) for x in value_arr]
cansat_h = [int(x[-1]) for x in value_arr]

def get_data(lat, lon):
    r = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,pressure_msl')
    json_code = r.json()
    temperature = json_code["current"]["temperature_2m"]
    pressure = json_code["current"]["pressure_msl"]
    return {"temperature":temperature, "pressure":pressure}


# Argument_1: float representing temperature at 0 meters height above sea-level
# Argument_2: float representing pressure at 0 meters height above sea-level

def plot_graf(p0, t0):
    # Calculate height from pressure at sea level
    y = [1000 - n for n in range(0,1001, 10)]
    # calculate temperature from temperature at sea level as a function of height
    x_temp = [round(t0 - 0.0065*h, 2) for h in y]
    # calculate the temperature at sea level in Kelvin
    k0 = t0 + 273.15
    # calculate the pressure from pressure and temperature at sea level as a function of height
    x_pres = [round(p0*((k0 - 0.0065*h)/k0)**5.256, 1) for h in y]
    fig, ax = plt.subplots(1, 2, figsize = (10,8))
    ax[0].plot(x_temp,y, color = 'red', linestyle = '--'); ax[0].set_title("Predicted temperature")
    ax[0].plot(cansat_t,cansat_h, color = 'green')
    ax[1].plot(x_pres,y, color = 'red', linestyle = '--'); ax[1].set_title("Predicted pressure")
    ax[1].plot(cansat_p,cansat_h, color = 'green')
    print(max(cansat_h))
    print(cansat_h)
    #Download figure as img

    def fig2img(fig):
        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        img = Image.open(buf)
        return img

    # Save return image in a variable by passing
    # plot in the created function for Converting a plot to a PIL Image.
    img = fig2img(fig)

    # Save image with the help of save() Function.
    img.save('Plot image.png')
    pass

tem_pre_data = get_data(57.718323, 11.787872)

plot_graf(tem_pre_data["pressure"], tem_pre_data["temperature"])