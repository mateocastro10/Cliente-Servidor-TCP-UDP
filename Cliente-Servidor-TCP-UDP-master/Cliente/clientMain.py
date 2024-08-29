import tkinter as tk
from tkinter import messagebox
from udpConfig import UDPConfig
from tcpConfig import TCPConfig

class ServerInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Server Communication Interface")
        self.master.geometry("600x600")  # Ajusta el tamaño de la ventana

        # Configurar la cuadrícula
        self.master.grid_rowconfigure(0, weight=2)
        self.master.grid_rowconfigure(1, weight=2)
        self.master.grid_rowconfigure(2, weight=2)
        self.master.grid_rowconfigure(3, weight=2)
        self.master.grid_rowconfigure(4, weight=2)
        self.master.grid_columnconfigure(0, weight=2)
        self.master.grid_columnconfigure(1, weight=4)
        
        # Etiqueta para seleccionar el protocolo
        self.protocol_label = tk.Label(master, text="Seleccione el Protocolo:", font=("Arial", 12))
        self.protocol_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Botones de selección de protocolo
        self.protocol_var = tk.IntVar()
        self.tcp_radio = tk.Radiobutton(master, text="TCP", variable=self.protocol_var, value=1, font=("Arial", 12))
        self.udp_radio = tk.Radiobutton(master, text="UDP", variable=self.protocol_var, value=2, font=("Arial", 12))
        self.tcp_radio.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.udp_radio.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        # Etiqueta para la dirección IP del servidor
        self.ip_label = tk.Label(master, text="Dirección IP del Servidor:", font=("Arial", 12))
        self.ip_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Entrada para la dirección IP del servidor
        self.ip_entry = tk.Entry(master, font=("Arial", 12))
        self.ip_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Etiqueta para el puerto
        self.port_label = tk.Label(master, text="Port:", font=("Arial", 12))
        self.port_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        # Entrada para el puerto
        self.port_entry = tk.Entry(master, font=("Arial", 12))
        self.port_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        self.port_entry.insert(0, "12000")  # Valor por defecto
        
        # Etiqueta para seleccionar el tipo de dólar
        self.dollar_type_label = tk.Label(master, text="Seleccione el tipo de dólar:", font=("Arial", 12))
        self.dollar_type_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        
        # Variable para el tipo de dólar
        self.dollar_type_var = tk.StringVar()
        self.dollar_type_var.set("Dólar Oficial")  # Valor por defecto
        
        # Menú desplegable para seleccionar el tipo de dólar
        self.dollar_type_menu = tk.OptionMenu(master, self.dollar_type_var, "Dólar Oficial", "Dólar Blue", "Dólar Tarjeta", "Dólar Cripto")
        self.dollar_type_menu.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        # Botón para enviar el mensaje
        self.send_button = tk.Button(master, text="Enviar", font=("Arial", 12), command=self.send_message)
        self.send_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)
        
        # Entradas para mostrar cada dato específico de la API
        self.create_data_entry(master, "Moneda:", "moneda", 6)
        self.create_data_entry(master, "Compra:", "compra", 7)
        self.create_data_entry(master, "Venta:", "venta", 8)
        self.create_data_entry(master, "Fecha de Actualización:", "fechaActualizacion", 9)
        
        # Inicializa el cliente como None
        self.client = None

    def create_data_entry(self, master, label_text, attr_name, row):
        """ Helper function to create label and entry for displaying data """
        label = tk.Label(master, text=label_text, font=("Arial", 12))
        label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(master, font=("Arial", 12), width=40)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        setattr(self, f"{attr_name}_entry", entry)

    def send_message(self):
        try:
            # Validar que se haya seleccionado un protocolo
            protocol = self.protocol_var.get()
            if protocol not in [1, 2]:
                messagebox.showwarning("Input Error", "Please select a protocol.")
                return

            # Validar que la dirección IP no esté vacía
            serverip = self.ip_entry.get()
            if not serverip or type(serverip) != "string":
                messagebox.showwarning("Input Error", "Please enter the server IP address.")
                return

            # Validar que el puerto no esté vacío y sea un número válido
            port = self.port_entry.get()
            if not port:
                messagebox.showwarning("Input Error", "Please enter the port number.")
                return
            try:
                port = int(port)
            except ValueError:
                messagebox.showwarning("Input Error", "Port number must be an integer.")
                return

            # Validar que se haya seleccionado un tipo de dólar
            dollar_type = self.dollar_type_var.get()
            if not dollar_type:
                messagebox.showwarning("Input Error", "Please select a dollar type.")
                return
    

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
            
            response = self.client.receiveMessage()
            
            # Imprime la respuesta para depuración
            print("Response received from server:", response)
            # Mostrar la información completa de cotización en los inputs
            if isinstance(response, dict):
                moneda = response.get('moneda', 'N/A')
                compra = response.get('compra', 'N/A')
                venta = response.get('venta', 'N/A')
                fecha = response.get('fechaActualizacion', 'N/A')

                # Mostrar información detallada en los inputs correspondientes
                self.moneda_entry.delete(0, tk.END)
                self.moneda_entry.insert(0, moneda)
                
                self.compra_entry.delete(0, tk.END)
                self.compra_entry.insert(0, compra)
                
                self.venta_entry.delete(0, tk.END)
                self.venta_entry.insert(0, venta)
                
                self.fechaActualizacion_entry.delete(0, tk.END)
                self.fechaActualizacion_entry.insert(0, fecha)

            else:
                messagebox.showerror("Error", "Response format is incorrect.")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def getDolarType(self):
        return self.dollar_type_var.get()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ServerInterface(root)
    root.mainloop()
