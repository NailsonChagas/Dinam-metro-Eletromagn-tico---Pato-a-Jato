# Dinamômetro Eletromagnético - Pato a Jato

Um dinamômetro é um instrumento utilizado para medir força, torque (momento de força) e potência mecânica gerada ou absorvida por um sistema.

No tipo eletromagnético por correntes de Foucault, o funcionamento baseia-se na indução eletromagnética. Um campo magnético é criado por bobinas fixas próximas a um disco metálico condutor acoplado ao eixo do motor.

Quando o disco gira dentro desse campo, surgem correntes de Foucault (eddy currents) em sua superfície. Essas correntes geram campos magnéticos opostos ao campo original, produzindo uma força de frenagem que atua sobre o disco e, consequentemente, sobre o eixo do motor.

A intensidade dessa frenagem, que representa a carga aplicada ao sistema, é proporcional à velocidade de rotação e à intensidade do campo magnético, podendo ser controlada pela corrente nas bobinas.

O dinamômetro é acoplado ao eixo do motor ou do veículo, permitindo controlar a carga aplicada e simular diferentes condições de operação.


## Princípio de Funcionamento

O freio por correntes de Foucault (eddy current brake) opera com base na indução eletromagnética. Quando o disco condutor (geralmente de alumínio ou cobre) gira dentro de um campo magnético variável, correntes parasitas são induzidas em sua superfície. Essas correntes formam loops fechados dentro do material, conhecidos como eddy currents.

De acordo com a Lei de Faraday da Indução, a tensão induzida é proporcional à variação do fluxo magnético ao longo do tempo:

$$
\mathcal{E} = - \frac{d\Phi_B}{dt}
$$

Essas correntes induzidas interagem com o campo magnético aplicado, gerando uma força de Lorentz que se opõe ao movimento do disco, conforme a Lei de Lenz. Essa oposição resulta em uma força de frenagem (torque de frenagem), que é proporcional à velocidade angular do disco.

Em resumo:

- Quando o disco gira, correntes de Foucault são induzidas.
- Essas correntes criam campos magnéticos que se opõem ao movimento.
- O resultado é uma força de frenagem que cresce com a velocidade de rotação.

A relação entre o torque de frenagem ($\tau_b$) e a velocidade angular ($\omega$) pode ser expressa de forma simplificada como:

$$
\tau_b \propto B^2 \times \omega
$$

Onde:

- $B$ é a densidade do campo magnético;
- $\omega$ é a velocidade angular do disco.

Como o campo magnético $B$ depende da corrente nas bobinas eletromagnéticas, a força de frenagem pode ser controlada ajustando-se essa corrente.

[**Referência: Physics Forums — Eddy Current Braking Setup**](https://www.physicsforums.com/threads/how-to-find-the-braking-torque-of-an-eddy-current-braking-setup.976052/?utm_source=chatgpt.com)

[**Referência: Magnetomotive Force — Wikipedia**](https://en.wikipedia.org/wiki/Magnetomotive_force)


## Medição de Potência

Durante os testes, sensores integrados ao dinamômetro medem parâmetros como **torque** e **velocidade angular**, possibilitando calcular a **potência mecânica** pela relação:

$$
P = \tau \times \omega
$$

Onde:
- $P$ é a potência
- $\tau$ é o torque
- $\omega$ é a velocidade angular

[**Referência: Dynamometer — Wikipedia**](https://en.wikipedia.org/wiki/Dynamometer)

## O que está faltando?
- Sensores
    - Rotação
    - Torque
    - Temperatura -> Não sei
        - Disco do freio eletromagnético -> Não sei
        - Motor do carro -> Não sei
    - Corrente -> Não sei
- Controle da fonte de corrente
- Suporte para o carro
- Suporte para o dinamômetro

## Sensores

A medição precisa de rotação, torque e corrente é essencial para o cálculo do desempenho do motor e da potência dissipada pelo sistema. Esses sensores também permitem o controle e calibração do dinamômetro durante os testes.

### Rotação (Velocidade Angular e RPM)

Para medir a **velocidade de rotação** do eixo, podem ser utilizados sensores ópticos ou magnéticos.
Um método comum consiste no uso de um **photo interrupter sensor** (sensor óptico) acoplado a uma **roda codificadora (encoder wheel)** ou disco perfurado. Cada interrupção do feixe de luz gera um pulso digital, que é contabilizado por um microcontrolador.

**Exemplo de componentes:**

- **Sensor óptico:** OPB704, CNY70, ou módulos de encoder óptico prontos.
- **Alternativa magnética:** sensor de efeito Hall (A3144, SS49E) com ímã no eixo.

A **velocidade angular** é calculada a partir da frequência dos pulsos:

$$
\omega = 2\pi \times \frac{N}{t}
$$

Onde:

* $\omega$ = velocidade angular (rad/s);
* $N$ = número de rotações detectadas;
* $t$ = intervalo de tempo medido.

A **velocidade de rotação (RPM)** é obtida por:

$$
\text{RPM} = 60 \times \frac{N}{t}
$$

### Torque

O torque do motor é determinado indiretamente pela força de reação que o freio exerce sobre o seu suporte durante a execução dos testes.

Para isso, o conjunto fixo (estator ou suporte do freio) é conectado a um **braço de alavanca rígido** de comprimento conhecido $L$, medido a partir do **centro do eixo** até o ponto de aplicação da força.
Uma **célula de carga** mede a força $F$ aplicada na extremidade do braço.

O torque é então calculado por:

$$
\tau = F \times L \times \cos(\theta)
$$

Onde:

- $\tau$ = torque de frenagem (N·m);
- $F$ = força medida pela célula de carga (N);
- $L$ = comprimento do braço (m);
- $\theta$ = ângulo entre a direção da força e o braço (idealmente 90°).

**Cuidados de montagem:**

- O braço deve ser **rígido e sem folgas**, para manter $L$ constante.
- Utilize um **ponto de ancoragem fixo** ou estrutura rígida para referência.
- Evite **forças parasitas** (ex.: empuxo axial ou vibração lateral) com o uso de buchas ou guias.

### Temperatura

A temperatura é um parâmetro importante tanto para o **disco do freio** quanto para o **motor em teste**, pois o aquecimento influencia a resistência dos materiais e a dissipação térmica.

**Sensores recomendados:**

- **Disco do freio:** termopar tipo K ou sensor PT100 fixado próximo à superfície do disco.
- **Motor:** termistor NTC ou DS18B2 para leitura de temperatura de carcaça ou enrolamentos.

O monitoramento contínuo evita sobreaquecimento no disco e permite estimar o comportamento térmico do sistema durante ensaios prolongados.

### Corrente

A corrente elétrica aplicada às bobinas eletromagnéticas determina diretamente a intensidade do campo magnético e, portanto, a força de frenagem.

**Métodos de medição:**

- **Sensor de efeito Hall** (ex.: ACS712, INA219, INA226).
- **Shunt resistor** de precisão com amplificador diferencial.

A corrente medida deve ser usada tanto para **controle do campo** (via PWM ou fonte regulável) quanto para registro de dados e posterior análise de desempenho.

## Integração e Aquisição de Dados

Os sinais provenientes dos sensores podem ser processados por um **microcontrolador** (ex.: *STM32 Blue Pill* ou *ESP32*), que realiza:

- Leitura analógica/digital (ADC) dos sensores de torque e corrente;
- Contagem de pulsos do sensor de rotação (via interrupções);
- Cálculo em tempo real de torque, velocidade e potência;
- Envio dos dados para um computador via Bluetooth ou USB
