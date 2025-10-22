import matplotlib
matplotlib.use('TkAgg')  # Forçar backend TkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import struct
import time
from collections import deque

# ==============================
# Configurações principais
# ==============================
MAX_POINTS = 50
WINDOW_TIME = 10  # Janela deslizante (segundos)

time_data = deque(maxlen=MAX_POINTS)
weight_data = deque(maxlen=MAX_POINTS)
rpm_data = deque(maxlen=MAX_POINTS)

# ==============================
# Configuração do gráfico
# ==============================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('Dados do Sensor em Tempo Real')

line_weight, = ax1.plot([], [], 'b-', linewidth=2, label='Weight (kg)')
line_rpm, = ax2.plot([], [], 'r-', linewidth=2, label='RPM')

ax1.set_ylabel('Weight (kg)')
ax1.set_ylim(0, 10)
ax1.set_xlim(0, WINDOW_TIME)
ax1.grid(True)
ax1.legend()

ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('RPM')
ax2.set_ylim(0, 100)
ax2.set_xlim(0, WINDOW_TIME)
ax2.grid(True)
ax2.legend()

ser = None
start_time = None

# ==============================
# Função para iniciar serial
# ==============================
def init_serial():
    global ser, start_time
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        time.sleep(2)  # Aguarda inicialização da porta
        ser.reset_input_buffer()
        start_time = time.time()
        print("Conectado à porta serial!")
        print("Tempo(s) | Weight(kg) | RPM")
        print("-" * 30)
        return True
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return False

# ==============================
# Atualização em tempo real
# ==============================
def update(frame):
    global ser, start_time
    
    if ser and ser.in_waiting >= 8:
        try:
            data = ser.read(8)
            if len(data) == 8:
                weight = struct.unpack('f', data[0:4])[0]
                rpm = struct.unpack('f', data[4:8])[0]
                
                weight = max(0.0, weight)
                rpm = max(0.0, rpm)
                current_time = max(0.0, time.time() - start_time)
                
                print(f"{current_time:7.2f}s | {weight:9.3f}kg | {rpm:7.1f}RPM")
                
                # Adicionar dados
                time_data.append(current_time)
                weight_data.append(weight)
                rpm_data.append(rpm)

                # Não atualizar eixos se poucos pontos
                if len(time_data) < 2:
                    return line_weight, line_rpm

                # Atualizar dados das linhas
                line_weight.set_data(time_data, weight_data)
                line_rpm.set_data(time_data, rpm_data)

                # ======================
                # Atualização dinâmica dos eixos
                # ======================

                # Eixo do tempo — janela deslizante
                time_max = max(time_data)
                time_min = max(0, time_max - WINDOW_TIME)
                ax1.set_xlim(time_min, time_max)
                ax2.set_xlim(time_min, time_max)

                # Peso
                weight_max = max(weight_data)
                weight_margin = weight_max * 0.2 if weight_max > 0 else 0.1
                ax1.set_ylim(0, max(1.0, weight_max + weight_margin))

                # RPM
                rpm_max = max(rpm_data)
                rpm_margin = rpm_max * 0.2 if rpm_max > 0 else 10
                ax2.set_ylim(0, max(50, rpm_max + rpm_margin))

                # Atualizar título dinâmico
                fig.suptitle(f'Weight: {weight:.3f} kg | RPM: {rpm:.1f} | Tempo: {current_time:.1f}s')
        
        except Exception as e:
            print(f"Erro na leitura: {e}")
    
    return line_weight, line_rpm

# ==============================
# Execução principal
# ==============================
if init_serial():
    try:
        ani = animation.FuncAnimation(
            fig, update,
            interval=100,   # Atualiza a cada 100 ms
            blit=True,
            cache_frame_data=False
        )
        plt.tight_layout()
        plt.show()
        
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro no gráfico: {e}")
    finally:
        if ser and ser.is_open:
            ser.close()
            print("Porta serial fechada.")
else:
    print("Não foi possível conectar à porta serial.")
