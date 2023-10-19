lineas_dic = {}
i = 0
with open("rockyou.txt", "r", encoding="latin1") as entrada:
    for linea in entrada:
        linea = linea.strip()
        if linea and linea[0].isalpha():
            primera_letra = linea[0].upper()
            nueva_linea = primera_letra + linea[1:] + "0"
            lineas_dic[linea] = nueva_linea

with open("rockyou_mod.dic", "w", encoding="latin1") as salida:
    for linea_original in lineas_dic:
        linea_modificada = lineas_dic[linea_original]
        salida.write(f"{linea_modificada}\n")
        i += 1

print("Listo")
