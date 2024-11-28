def set_temperature(name, temp=28):
    print(name, "將冷氣設定在", temp, "度。")

set_temperature("Mike")
set_temperature(temp=25, name="Mike")
# set_temperature(temp=100)