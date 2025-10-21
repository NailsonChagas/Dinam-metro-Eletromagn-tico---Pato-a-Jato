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
    - Rotação -> Photo Interrupter Sensor + Encoder Wheel
    - Torque -> Não sei
    - Temperatura -> Não sei
        - Disco do freio eletromagnético -> Não sei
        - Motor do carro -> Não sei
    - Corrente -> Não sei
- Controle da fonte de corrente
- Suporte para o carro
- Suporte para o dinamômetro
