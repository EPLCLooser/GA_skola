import requests
import matplotlib.pyplot as plt
import io
from PIL import Image

def get_data(lat, lon):
    r = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,pressure_msl')
    json_code = r.json()
    print(json_code)
    temperature = json_code["current"]["temperature_2m"]
    pressure = json_code["current"]["pressure_msl"]
    return {"temperature":temperature, "pressure":pressure}

print(get_data(57.718323, 11.787872))

def plot_graf(p0, t0):
    # Calculate height from pressure at sea level
    y = [1000 - n for n in range(0,1001, 10)]
    print(y)
    # calculate temperature from temperature at sea level as a function of height
    x_temp = [round(t0 - 0.0065*h, 2) for h in y]
    print(x_temp)
    # calculate the temperature at sea level in Kelvin
    k0 = t0 + 273.15
    # calculate the pressure from pressure and temperature at sea level as a function of height
    x_pres = [round(p0*((k0 - 0.0065*h)/k0)**5.256, 1) for h in y]
    print(x_pres)

    fig, ax = plt.subplots(1, 2, figsize = (10,8))
    ax[0].plot(x_temp,y, color = 'red', linestyle = '--'); ax[0].set_title("Predicted temperature")
    ax[1].plot(x_pres,y, color = 'red', linestyle = '--'); ax[1].set_title("Predicted pressure")
    #plt.plot(x, y)
    #plt.show()

    #Download figure as img
    """
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
    """
    pass

tem_pre_data = get_data(57.718323, 11.787872)

plot_graf(tem_pre_data["pressure"], tem_pre_data["temperature"])
