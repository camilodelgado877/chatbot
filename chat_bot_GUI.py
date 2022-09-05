from tkinter import*
import tkinter
import re
import random
if __name__ == '__main__':
    raiz=Tk()
    raiz.configure(bg="#FFDEAD") #color del fondo
    raiz.title("CHAT BOT") #nombre ventana
    bot_ms = ""
    lista=[]
    nombre=""
    
    def send(event=None): # Enviamos el mensaje
        global nombre 
        mensaje = mi_ms.get() #recepción mensaje

        mensaje = "" + mensaje
        lista = mensaje.split()
        #en caso de colocar el nombre de la persona, escribirlo como nombre de contacto
        if (("mi" ==lista[0]) and("nombre"==lista[1])):
            nombre = lista[-1]
            mensaje =nombre +": "+mensaje
        else:    
            if(len(nombre)>1):
                mensaje = nombre +": "+mensaje
            else:
                mensaje ="Tú:" +mensaje
        mensaje_you=mensaje
        bot_ms = "" + get_response(mensaje_you) #recepción mensaje del bot
        bot_ms = bot_ms.split('/') #en caso de que el texto sea largo se divide en dos lineas 
        mensaje_bot = bot_ms
        bot_ms=""
        mi_ms.set("") #limpia despues de enviar el mensaje
        mensaje_list.insert(tkinter.END, mensaje) #Insertamos el mensaje que escribimos en relación al Gui
        mensaje_list.itemconfigure(END,fg="brown") #color texto del mensaje de la persona
        mensaje_list.insert(tkinter.END, "Anastacio:") #nombre del bot
        if(len(mensaje)>1): #en caso de que el texto sea largo se divide en varias lineas de código
            for dato in mensaje_bot:
                mensaje_list.insert(tkinter.END, dato)
        else:
            mensaje_list.insert(tkinter.END, mensaje_bot)#si el texto es corto se envia en una sola linea de código

    messages_frame = tkinter.Frame(raiz, height=10, width=10,padx=5,pady=5) #insertar en el area de texto
    messages_frame.grid(row=11,column=1,columnspan=2)
    messages_frame.grid_propagate(False)
    mi_ms = tkinter.StringVar() #Espera mensaje
    mi_ms.set("")
    Scrollbar = tkinter.Scrollbar(messages_frame) # Barra deslisable

    #contenido del area de mensaje
    mensaje_list = tkinter.Listbox(messages_frame, font=("Calibri", 15),height=20, width=80,bg="#FFF5EE",  yscrollcommand=Scrollbar) #campo de texto donde se muestran los mensajes
    Scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y) #la barra deslizable se ubica en el lado derecho
    mensaje_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH) #el texto se organiza en la zona izquierda
    mensaje_list.pack()
    messages_frame.pack()
    
    mensaje_list.insert(tkinter.END, "Bienvenido/a, soy Anastacio junto a mi aprenderás cultura general")
    mensaje_list.insert(tkinter.END, "Anastacio: ¿En qué puedo ayudarte?")
    #Area o campo para escribir y boton de enviar

    entry_field = tkinter.Entry(raiz, font=("Calibri", 12), textvariable=mi_ms,width=60) #campo de escritura
    entry_field.bind("<Return>", send) #si se oprime enter en el teclado lo entendera como enviar
    entry_field.pack()
    send_button = tkinter.Button(raiz, text="ENVIAR", command=send,bg="#CD853F",width=20)#boton enviar
    send_button.pack()

    def get_response(respuesta):#función donde se procesa el mensaje del usuario para que el bot pueda responder 
        split_message = re.split(r'\s|[,:;.?!-_]\s*', respuesta.lower()) #se eliminan signos de la cadena de texto
        #print(split_message)
        response =check_all_messages(split_message)#se llama a la función donde se encuentra la información para devolver una respuesta
        return response

    def message_probability(user_message, recognized_words, single_response=False, required_words=[]):#función donde se realiza el calculo la probabilidad comparando la información
        message_certainty = 0
        has_requires_words = True
        
        for word in user_message: #se calcula la probabilidad en base a las respuestas que se encuentran y el mensaje
            if word in recognized_words:
                message_certainty +=1
        percentage = float(message_certainty) / float (len(recognized_words))
        
        for word in required_words:
            if word not in user_message:
                has_requires_words = False
                break
        if has_requires_words or single_response:
            return int(percentage * 100)
        else:
            return 0
    def check_all_messages(message):#función donde se procesa el mensaje del usuario y se regresa una respuesta
            highest_prob = {}
            
            def response(bot_response, list_of_words, single_response = False, required_words = []):
                nonlocal highest_prob
                highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)
                
            #posibles respuesta según la pregunta del usuario
            
            #SALUDOS
            
            response('hola', ['hola', 'hl', 'saludos', 'buenas'], single_response = True)

            response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])

            response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response = True)
            
            #MATEMATICAS

            response('Es un número natural mayor que 1 que tiene únicamente dos divisores positivos distintos:/ él mismo y el 1.', ['número','numero','numeros','primo','primos','números'],single_response=True)

            response('suma o total', ['resultado','suma','sumas'], required_words=['resultado'])

            response('diferencia resta',['resultado', 'resta', 'restas'], required_words=['resultado'])

            response('cociente',['resultado', 'división', 'divisiones'], required_words=['resultado'])

            response('producto',['resultado', 'multiplicación', 'multiplicaciones'], required_words=['resultado','multiplicación'])
            
            response('Las partes son multiplicando, multiplicador, producto',['partes','parte', 'multiplicación'], required_words=['multiplicación'])

            response('Las partes son sumados y resultado o suma', ['partes', 'suma'], required_words=['suma'])

            response('Las partes son minuendo, sustraendo y resta o diferencia', ['partes', 'resta', 'restas'], required_words=['resta'])

            response('Las partes son dividendo, resto, divisor y cociente', ['partes', 'división', 'divisiones' ], required_words=['división'])

            response('Las partes son el numerador y el denominador ',['partes', 'fracción', 'fracciones'], required_words=['fracción'])

            response('Los operadores son para: suma= +, resta= -, multiplicación= *, división= , mayor que= >,/ menor que= <, igual= =, mayor o igual que= >=, menor o igual que= <= y distinto que= <> ', ['operadores'], single_response=True)

            response('Las partes son índice, radical, raíz y radicando',['partes', 'raíz', 'raices'], required_words=['raíz'])

            response('Los números reales son cualquier número que corresponda a un punto en la recta real,/ y pueden clasificarse en números naturales, enteros, racionales e irracionales',['números','número','numero','numeros', 'reales','real'], single_response=True)
            
            response('Los números naturales son los que utilizamos en la vida cotidiana para contar u ordenar/ y pertenecen al conjunto de números enteros positivos.',['números','número','numero','numeros','natural', 'naturales'], single_response=True)
            
            response('Los números enteros se dividen en tres partes, los Enteros positivos o números naturales, /Enteros negativos y cero',['números','numero','número','numeros','entero', 'enteros'], single_response=True)
            
            response('Los números racionales son las fracciones que pueden formarse a partir de números enteros /y pertenecen a la recta real. ',['números','número','numeros','numero','racional' 'racionales'], single_response=True)
            
            response('Los números irracionales son números reales que no pueden expresarse ni de manera exacta /ni de manera periódica ',['números','numero','número','numeros','irracional' 'irracionales'], single_response=True)  
            
            #CIENCIAS SOCIALES

            response('Estudio del comportamiento del hombre en la sociedad y su organizacion', ['sociales','ciencia','social''ciencias'], single_response=True)

            response('El Rio Amazonas es el mas grande con aprox. 6.800 km',['rio','mas','largo','grande','caudaloso','mundo','del'],required_words=['rio','mundo'])

            response('El Everest es la montaña más alta del mundo con 8848 metros',['montaña','mas','alta','del','mundo','planeta'],required_words=['montaña','mundo'])

            response('Existen 6 continentes: Europa, África, Asia, América, Oceanía y Antártida',['cuantos','continentes','existen','hay'],required_words=['continentes'])

            response('Las ramas de la politica son 3: legislativa, judicial y ejecutiva',['cuales','son','ramas','politica','las'],required_words=['ramas','politica'])

            response('Existen 5 grandes reinos: Animal, vetegal, hongos, protoctistas y moneras',['cuales','son','reinos','de','seres','vivos'],required_words=['reinos','seres'])

            #ESPAÑOL

            response('un cuento es un tipo de narración breve basada en hechos reales o ficticios',['que','cuento'],required_words=['cuento'])

            response('los tipos de cuentos que existen son fantásticos,realistas,misteriosos,históricos,cómicos,terror',['tipos','cuento','cuentos','existen'],single_response=True)

            response('un punto es un signo de puntuacion cuyo uso principal es señalar graficamente la pausa que marca el final / de un enunciado',['uso','punto'],required_words=['punto'])

            response('Describir es explicar de manera detallada y ordenada como son las personas,animales, lugares y objetos',['descripcion'],single_response=True)

            response('un sustantivo se divide en dos grupos principales comunes y propios, a su vez los /comunes se dividen en concretos y abstractos y al mismo tiempo los concretos se dividen en colectivos e individuales',['sustantivo'],single_response=True)

            response('La coma es un signo ortografico que se usa para hacer una pausa breve en la lectura',['coma'],single_response=True)

            response('Se denomina oracion a un conjunto ordenado y lineal de palabras',['oracion'],single_response=True)

            response('La fabula es una narracion donde los personajes son animales que dialogan y pie san como si fueran humanos',['fabula'],single_response=True)


            response('El acento es la mayor intencidad con que se pronuncia una de las silabas de la palabra',['acento'],single_response=True)


            response('El pronombre es una categoria gramatical variable cuyos accidentes son: genero, numero y persona',['pronombre'],single_response=True)

            #CIENCIAS NATURALES

            response('es un proceso que las plantas realizan para fabricar sus propios alimentos y así poder crecer y desarrollarse',['fotosintesis'],single_response=True)
            
            response('La luz que llega del Sol ingresa en la atmósfera y se dispersa en todas las direcciones. ',['cielo','azul'], required_words=['cielo','azul'])

            response('El Sol brilla debido a que la enorme presión en su centro hace que los átomos de hidrógeno se transformen en helio.',['brilla','sol'],required_words=['brilla','sol'])
            
            response('La leche proviene de la ubre de las vacas',['leche'],required_words=['leche'])
            
            response('La distancia de la tierra a la luna es: 384.400 km',['distancia','tierra','luna'],required_words=['tierra','luna'])

            response('Colapsaron bajo su propia gravedad desde las grandes nubes de gas que dejó el Big Bang.',['llegaron','estrellas','estrella','cielo'],single_response=True)
            
            response('Cuando las gotas de agua en las nubes crecen y miden más de 0,1 milímetro caen en forma de lluvia.',['porque','llueve','lluvia','llovizna'],required_words=['llueve'])
            
            response('No es un planeta',['sol','planeta'],required_words=['sol','planeta'])

            response('Un planeta es un cuerpo celeste que gira alrededor de una estrella. Tiene una forma semejante a una esfera /y no emite luz propia',['planeta'],required_words=['planeta'])

            response('Es todo aquello que nos rodea, el cielo, el suelo, el agua, las plantas, los animales y el resto de las /personas que se encuentran donde vivimos conforman el medio ambiente.',['medio','ambiente'],required_words=['medio','ambiente'])
            
            best_match = max(highest_prob,key=highest_prob.get )
            
            #print(highest_prob)
            split_mensa = highest_prob
            
            
            return unknow() if highest_prob[best_match] < 1 else best_match
        
    def unknow():
        response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
        return response 
    raiz.mainloop()    

