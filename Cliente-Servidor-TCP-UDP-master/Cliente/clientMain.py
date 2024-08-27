import tkinter as tk
from tkinter import messagebox
from udpConfig import UDPConfig
from tcpConfig import TCPConfig

class ServerInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Server Communication Interface")
        self.master.geometry("400x350")
        
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
        
        # Etiqueta para el mensaje
        self.message_label = tk.Label(master, text="Message:", font=("Arial", 12))
        self.message_label.pack(pady=10)
        
        # Entrada para el mensaje
        self.message_entry = tk.Entry(master, font=("Arial", 12))
        self.message_entry.pack(pady=5)
        
        # Botón para enviar el mensaje
        self.send_button = tk.Button(master, text="Send Message", font=("Arial", 12), command=self.send_message)
        self.send_button.pack(pady=20)
        
        # Área de texto para mostrar la respuesta del servidor
        self.response_area = tk.Text(master, height=5, width=40, font=("Arial", 12))
        self.response_area.pack(pady=10)
        
        # Inicializa el cliente como None
        self.client = None

    def send_message(self):
        try:
            protocol = self.protocol_var.get()
            port = int(self.port_entry.get())
            message = self.message_entry.get()
            
            if protocol not in [1, 2]:
                messagebox.showwarning("Input Error", "Please select a protocol.")
                return
            
            if not message:
                messagebox.showwarning("Input Error", "Please enter a message.")
                return
            
            # Crear la conexión TCP o UDP
            if protocol == 1:
                self.client = TCPConfig(port)
            else:
                self.client = UDPConfig(port)
            
            self.client.createSocket()
            
            # Enviar el mensaje
            self.client.sendMessage(message)
            
            # Recibir la respuesta
            response = self.client.receiveMessage()
            self.response_area.insert(tk.END, f"Server response: {response}\n")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            if self.client:
                self.client.closeSocket()

def main():
    root = tk.Tk()
    app = ServerInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    
