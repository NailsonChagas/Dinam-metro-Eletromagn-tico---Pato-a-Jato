# Dinamômetro Eletromagnético - Pato a Jato

Um dinamômetro é um instrumento utilizado para medir força, torque (momento de força) e potência mecânica gerada ou absorvida por um sistema.

No tipo eletromagnético, o funcionamento baseia-se em duas bobinas que produzem um campo magnético. Esse campo, ao interagir com o disco metálico acoplado ao eixo, atua como um freio eletromagnético, gerando uma força de frenagem que representa a carga aplicada ao sistema.

O dinamômetro é acoplado ao eixo do motor ou do veículo, possibilitando controlar a carga aplicada e simular diferentes condições de operação.

## Princípio de Funcionamento

A **força eletromagnética** produzida por uma bobina é proporcional à **força magnetomotriz (mmf)**, dada por:

$$
\text{mmf} = N \times I
$$

Onde:
- $N$ é o número de espiras da bobina
- $I$ é a corrente elétrica

[**Referência: Magnetomotive Force — Wikipedia**](https://en.wikipedia.org/wiki/Magnetomotive_force)

Assim, a **carga aplicada pelo dinamômetro** pode ser **controlada variando-se a corrente fornecida** às bobinas.

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
