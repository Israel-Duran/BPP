import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename
from tkinter import ttk, messagebox

"""
Libreria tkinter. Es una libreria la cual hay que importar y que sin ella es imposible crear la aplicación de escritorio.
"""


class Aplicacion_editor(tk.Tk):
    """
        Aplicaciones_editar. Es una clase la cual hereda de (tk.Tk) la cual se encarga de crear la aplicación de escritorio para
        editar archivos de texto .txt.

        Metodos:
        =======

        init: Este metodo tiene como objetivo fundamental inicializar los atributos del objeto que se ha creado

        abrir_archivo: Abre el archivo que se seleccionado para poder editarlo posteriormente

        editar: Edita el archivo ya seleccionado y escrito.

        guardar: Este metodo guarda el un archivo seleccionado como otro archivo nuevo, también crea un nuevo archi y lo guarda.

        salir: Se utiliza este metodo para cerrar y salir de la aplicacion

        componentes: Este metodo tiene todos los componentes que forman la aplicacion de escritorio

        Sentencias:
        ==========
        if __name__ == '__main__': Esta sentencia se utiliza para ejecutar el Script como programa principal



    def __init__(self):

        Método init. Es el método que crea la aplicacion. Tiene las caracteristicas principales de la aplicacion,tales como:

        super().__init__(): Hace referencia con super a la clase init para poder crear la aplicacion que se suele crear con tk

         self.title: el titulo que tendra nuestra aplicacion

         self.geometry: las dimensiones, es decir el tamaño de la aplicacion

         self.resizable: el ajuste de la aplicacion

         self.iconbitmap: cambia el icono de la aplicacion a uno personalizado

         self.columnconfigure: configuracion de las columnas de la aplicacion

         self.texto: atributo que crea el campo de texto para escribir

         self.archivo: atributo que hace referencia al archivo que se va a abrir

         self.archivoA: atributo que se utiliza para saber si tenemos ya un archivo abierto

         self._componentes(): Metodo que llama al resto de componentes de la aplicacion, tales como botones



    def _abrir_archivo(self):

        Metodo abrir_archivo: Este metodo es el encargado de abrir el archivo a editar

        self.iconbitmap: establece un icono a la ventana que se abre al apretar el boton de abrir

        self.archivoA = (askopenfile) es una funcion de tkinter que sirve para preguntar por el archivo que deseamos abrir y con mode = 'r+'

        especificamos como queremos abrir el archivo exactamente.

        self.texto.delete: se utiliza para eliminar el texto que se ha escrito en la caja de texto utilizando el metodo delete()

        if not self.archivoA: se utiliza para revisar si hay un archivo abierto

        with open: se utiliza para abrir y cerrar el archivo

        guardar_texto: lee la informacion del archivo

        self.texto.insert: inserta el contenido del archivo en el campo de texto utilizando el metodo insert()

        self.title: se utiliza para editar el titulo de la aplicacion una vez que el archivo se ha abierto


    def _editar(self):

        Metodo _editar: Este metodo se encarga de editar el archivo

         if self.archivoA: si se ha escrito ya un archivo este se sobreescribe

         messagebox.showinfo: en el caso que se seleccione editar y no se haya seleccionado un archivo con

         anterioridad el programa dara una informacion especificando que hay que seleccionar un archivo antes
         para poder llevar a cabo la edicion


    def _guardar(self):

        Metodo _guardar: Este metodo se encarga de guardar el archivo que se ha editado o de crear en nuevo archivo .txt
        en caso de que no exista ninguno.

         self.iconbitmap: cambia el icono de la aplicacion

        self.archivo: (asksaveasfilename) -> salva el archivo el archivo actual que este en la aplicaion en un nuevo archivo

        if not self.archivo: se utiliza para comprobar el archivo

        with open: si hay un archivo que es valido se abre en modo escritura.

        texto: Se utiliza para leer el contenido de la caja de texto


    def _salir(self):

        Metodo _salir. Este metodo se utiliza para cerrar la aplicacion y salir de ella
        self.quit(): es uno de los codigos de tkinter que se usan para cerrar la aplicacion de escritorio




    def _componentes(self):

        Metodo _componentes. Este metodo contiene los componentes de la aplicacion

        botones: crea el marco donde estaran los botones de la aplicacion

        abrir_archivo: boton que se utiliza para abrir el archivo que se desea editar

        editar_archivo: boton que se utiliza para editar el archivo ya seleccionado y ya escrito

        guradar_como: boton que se utiliza para guardar el archivo

        salir: boton que se utiliza para salir de la aplicacion

        abrir_archivo.grid: caracteristicas del boton abrir_archivo

        editar_archivo.grid: caracteristicas del boton editar_archivo

        guradar_como.grid: caracteristicas del boton guradar_como

        salir.grid: caracteristicas del boton salir

        botones.grid: caracteristicas del marco donde estan los botones

        self.texto.grid: caracteristicas del campo de texto para escribir


if __name__ == '__main__':

    Esta sentencia se utiliza para ejecutar el Script.

    aplicacion: este es un objeto de la clase

    aplicacion.mainloop(): esta es la principal sentencia que se utiliza para que arranque la aplicacion, sin ella
    la aplicacion no funciona.
    """
