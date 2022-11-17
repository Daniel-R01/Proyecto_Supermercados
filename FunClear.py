def EliminarInusuales(producto):
    import re
    #Primero se remplaza valores de str que son inusuales
    producto = producto.replace('con vita', '')
    producto = producto.replace('van camps', '')
    producto = producto.replace('el rey', '')
    producto = producto.replace('97 /3', '')
    producto = producto.replace('05 balanc ', '')
    producto = producto.replace('0 %', '')
    producto = producto.replace('proleche', '')
    producto = producto.replace('neto', '')
    producto = producto.replace('santa reyes', '')
    producto = producto.replace('cu', 'c/u')
    producto = producto.replace('gallina feliz 10 natural', '')
    producto = producto.replace('sipack parmalat', '')
    producto = producto.replace('alquería', '')
    producto = producto.replace('alpina', '')
    producto = producto.replace('providencia', '')
    producto = producto.replace('unidades', 'und')
    producto = producto.replace('tubipa', 'und')
    producto = producto.replace('bolsa', '')
    producto = producto.replace('mirringo', '')
    producto = producto.replace('marca', 'und')
    producto = producto.replace('rojo', 'und')
    producto = producto.replace('unidad', 'und')
    producto = producto.replace('gr', 'g')
    producto = producto.replace('precio especial', '')
    producto = producto.replace('repuesto', '')
    producto = producto.replace('comarrico', '')

    #Luego normalizamos las medidas 
    producto = producto.replace('1000 g', '1 kg')
    producto = producto.replace('2000 g', '2 kg')
    producto = producto.replace('3000 g', '3 kg')
    producto = producto.replace('4000 g', '4 kg')
    producto = producto.replace('5000 g', '5 kg')
    producto = producto.replace('10000 g', '10 kg')
    producto = producto.replace('1000 mlb', '500 g')

    #Para unidades liquidas

    producto = producto.replace('lt', 'l')
    producto = producto.replace('cc', 'ml')
    producto = producto.replace('cm3', 'ml')
    producto = producto.replace('cm3', 'ml')
    producto = producto.replace('1000 ml', '1 l')
    producto = producto.replace('1800 ml', '1.8 l')
    producto = producto.replace('3000 ml', '3 l')

    producto = producto.replace('kilo', 'kg')
    producto = producto.replace('kgs', 'kg')
    producto = producto.replace('2500 g', '2.5 kg')

    producto = re.sub(r"gratis.\w{1,5}.\w{1,20}","",producto)

    return producto.strip()



#Funcion para agrupar categorias mediante dicionario
def Agrupar(Producto):
    C ='CARNE'
    F = 'FRUTAS Y VERDURAS'
    A = 'ASEO'
    clasificador ={'HAMBURGUESA':C,'ABERDEEN':C,'ASADO':C,'BOLA':C,'BEEF':C,'BIFE':C,'BOLA':C,'BROCHETA':C,'CADERA':C,'CHATAS':C,'COLITA':C,'CENTRO':C,'COSTILLA':C,'ENTRECOT':C,'LOMO':C,'MATAMBRE':C,'MOLIDA':C,'MUCHACHO':C,'MURILLO':C,'NEW':C,'SOBREBARRIGA':C,'VACIO':C,'PUNTA':C,'CAPSULASCAFE': 'CAFE','CAPSULAS': 'CAFE','BLANQUEADORBLANCOXDESINFEC.PODER': 'BLANQUEADOR','FRIJOLES': 'FRIJOL','HUEVO': 'HUEVOS','ALIMENTO': 'LECHE','PASTA':'PASTAS','LASAGNA':'PASTAS','AGUACATE':F,'ARANDANO':F,'BANANO':F,'CEBOLLA':F,'CILANTRO':F,'FRUTA':F,'GOULASH':C,'MANZANA':F,'PAPA':F,'PAPAYA':F,'PEPINO':F,'PIMENTONES':F,'PIÑA':F,'PLATANO':F,'SPAGUETTI':'PASTAS','VERDURA':F,'ZANAHORIA':F,'TOMATE':F,'FIDEO':'PASTAS','ALPIN':'VARIOS','CAVA':'VARIOS','AROMATIZANTE':A,'BLANQUEADOR':A,'DESENGRASANTE':A,'DESINFECTANTE':A,'LIMON':F,'LIMPIA':A,'LIMPIADOR':A,'LIMPIAPISOS':A,'LIMPIAVIDRIOS':A,'QUITAGRASA':A,'QUITAGSAMR':A,'BLANQUEADOR':A,'ARENA':'VARIOS','MILO':'VARIOS'}

    if clasificador.get(Producto) != None:

        Producto = clasificador.get(Producto)

    return Producto

print("Se importo correctamente la funcion EliminarInusuales y Agrupar")