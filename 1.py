import tkinter as tk

root = tk.Tk()
root.title("Знаки зодиака")
root.geometry("420x620")

canvas = tk.Canvas(root, width=420, height=620, highlightthickness=0)
canvas.pack(fill="both", expand=True)

def draw_gradient(canvas, color1, color2):
    steps = 100
    r1, g1, b1 = root.winfo_rgb(color1)
    r2, g2, b2 = root.winfo_rgb(color2)
    for i in range(steps):
        r = int(r1 + (r2 - r1) * i / steps)
        g = int(g1 + (g2 - g1) * i / steps)
        b = int(b1 + (b2 - b1) * i / steps)
        color = f"#{r >> 8:02x}{g >> 8:02x}{b >> 8:02x}"
        canvas.create_rectangle(0, i * 620 / steps, 420, (i + 1) * 620 / steps, outline="", fill=color)

draw_gradient(canvas, "#a1c4fd", "#c2e9fb")  # Нежно-голубой градиент

frame = tk.Frame(canvas, bg="#ffffff", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=370, height=550)

zodiac_traits = {
    "aquarius": "Водолей — независимый, оригинальный, дружелюбный и мечтательный.",
    "fish": "Рыбы — добрые, чувствительные, творческие и немного загадочные.",
    "aries": "Овен — энергичный, решительный, активный и смелый.",
    "taurus": "Телец — надёжный, спокойный, любит комфорт и стабильность.",
    "twins": "Близнецы — общительные, любопытные, быстро адаптируются.",
    "cancer": "Рак — заботливый, эмоциональный, ценит уют и семью.",
    "lion": "Лев — уверенный, щедрый, любит быть в центре внимания.",
    "virgo": "Дева — аккуратная, трудолюбивая, внимательная к деталям.",
    "scales": "Весы — вежливые, уравновешенные, стремятся к гармонии.",
    "scorpion": "Скорпион — страстный, решительный, обладает сильной интуицией.",
    "sagittarius": "Стрелец — оптимистичный, свободолюбивый, любит приключения.",
    "capricorn": "Козерог — ответственный, целеустремлённый, настойчивый."
}

def get_zodiac(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "aquarius", "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "fish", "Рыбы"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "aries", "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "taurus", "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "twins", "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "cancer", "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "lion", "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "virgo", "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "scales", "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "scorpion", "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "sagittarius", "Стрелец"
    else:
        return "capricorn", "Козерог"

def show_zodiac():
    try:
        d = int(entry_day.get())
        m = int(entry_month.get())
        y = int(entry_year.get())
    except ValueError:
        label_result.config(text="Ошибка: введите числа!", fg="red")
        label_img.config(image="")
        label_traits.config(text="")
        return

    if not (1 <= m <= 12 and 1 <= d <= 31):
        label_result.config(text="Ошибка: некорректная дата!", fg="red")
        label_img.config(image="")
        label_traits.config(text="")
        return

    file_name, zodiac_name = get_zodiac(d, m)
    label_result.config(text=f"Ваш знак зодиака: {zodiac_name}", fg="#222222")

    try:
        img = tk.PhotoImage(file=f"./image/{file_name}.png")
        label_img.config(image=img)
        label_img.image = img
    except Exception:
        label_result.config(text="Изображение не найдено!", fg="red")
        label_img.config(image="")
        label_traits.config(text="")
        return

    label_traits.config(text=zodiac_traits[file_name], fg="#333333")

title = tk.Label(frame, text="Узнай свой знак зодиака", bg="#ffffff", font=("Arial", 14, "bold"))
title.pack(pady=10)

input_frame = tk.Frame(frame, bg="#ffffff")
input_frame.pack(pady=5)

tk.Label(input_frame, text="День:", bg="#ffffff").grid(row=0, column=0)
entry_day = tk.Entry(input_frame, width=5)
entry_day.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Месяц:", bg="#ffffff").grid(row=0, column=2)
entry_month = tk.Entry(input_frame, width=5)
entry_month.grid(row=0, column=3, padx=5)

tk.Label(input_frame, text="Год:", bg="#ffffff").grid(row=0, column=4)
entry_year = tk.Entry(input_frame, width=7)
entry_year.grid(row=0, column=5, padx=5)

btn = tk.Button(frame, text="🔮 Узнать знак", command=show_zodiac, bg="#a1c4fd", fg="#000", font=("Arial", 11, "bold"))
btn.pack(pady=10, ipadx=10, ipady=4)

label_result = tk.Label(frame, text="", bg="#ffffff", font=("Arial", 12))
label_result.pack(pady=5)

label_img = tk.Label(frame, bg="#ffffff", bd=1, relief="solid")
label_img.pack(pady=10)

label_traits = tk.Label(frame, text="", bg="#ffffff", wraplength=320, justify="center", font=("Arial", 11))
label_traits.pack(pady=10)

root.mainloop()
