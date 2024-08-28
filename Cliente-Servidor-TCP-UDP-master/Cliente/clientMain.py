import tkinter as tk
from tkinter import messagebox
from udpConfig import UDPConfig
from tcpConfig import TCPConfig

class ServerInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Server Communication Interface")
        self.master.geometry("400x400")  # Ajusta la altura de la ventana
        
        # Etiqueta para seleccionar el protocolo
        self.protocol_label = tk.Label(master, text="Seleccione el Protocolo:", font=("Arial", 12))
        self.protocol_label.pack(pady=10)
        
        # Botones de selección de protocolo
        self.protocol_var = tk.IntVar()
        self.tcp_radio = tk.Radiobutton(master, text="TCP", variable=self.protocol_var, value=1, font=("Arial", 12))
        self.udp_radio = tk.Radiobutton(master, text="UDP", variable=self.protocol_var, value=2, font=("Arial", 12))
        self.tcp_radio.pack(pady=5)
        self.udp_radio.pack(pady=5)
        
        # Etiqueta para el puerto
        self.port_label = tk.Label(master, text="Port:", font=("Arial", 12))
        self.port_label.pack(pady=10)
        
        # Entrada para el puerto
        self.port_entry = tk.Entry(master, font=("Arial", 12))
        self.port_entry.pack(pady=5)
        self.port_entry.insert(0, "12000")  # Valor por defecto
        
        # Etiqueta para seleccionar el tipo de dólar
        self.dollar_type_label = tk.Label(master, text="Seleccione el tipo de dólar:", font=("Arial", 12))
        self.dollar_type_label.pack(pady=10)
        
        # Variable para el tipo de dólar
        self.dollar_type_var = tk.StringVar()
        self.dollar_type_var.set("Dólar Oficial")  # Valor por defecto
        
        # Menú desplegable para seleccionar el tipo de dólar
        self.dollar_type_menu = tk.OptionMenu(master, self.dollar_type_var, "Dólar Oficial", "Dólar Blue", "Dólar Tarjeta", "Dólar Cripto")
        self.dollar_type_menu.pack(pady=5)
        
        # Botón para enviar el mensaje
        self.send_button = tk.Button(master, text="Send Request", font=("Arial", 12), command=self.send_message)
        self.send_button.pack(pady=20)
        
        # Área de texto para mostrar la respuesta del servidor
        self.response_area = tk.Text(master, height=5, width=40, font=("Arial", 12))
        self.response_area.pack(pady=20)
        
        # Inicializa el cliente como None
        self.client = None

    def send_message(self):
        try:
            protocol = self.protocol_var.get()
            port = int(self.port_entry.get())
            dollar_type = self.dollar_type_var.get()  # Obtiene el tipo de dólar seleccionado
            
            if protocol not in [1, 2]:
                messagebox.showwarning("Input Error", "Please select a protocol.")
                return
            
            # Crear la conexión TCP o UDP
            if protocol == 1:
                self.client = TCPConfig(port)
            else:
                self.client = UDPConfig(port)
            
            self.client.createSocket()
            
            # Enviar solo el tipo de dólar seleccionado
            self.client.sendMessage(dollar_type)
            
            # Recibir la respuesta
            response = self.client.receiveMessage()
            self.response_area.insert(tk.END, f"Server response: {response}\n")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def getDolarType(self):
        return self.dollar_type_var.get()
        


    
if __name__ == "__main__":
    root = tk.Tk()
    app = ServerInterface(root)
    root.mainloop()
