#  1. ENTRADA DE DADOS
# CRIAÇÃO DAS LISTAS
tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

quantidade = int(input("Digite a quantidade de eventos registrados: "))

# LOOP DE ARMAZENAMENTO DOS DADOS
for i in range(quantidade):
    print(f"\n--- Evento {i + 1} ---")

    tipos_eventos.append(input("Tipo de evento: "))
    paises.append(input("País: "))
    regioes.append(input("Região: "))
    cidades.append(input("Cidade: "))
    
    while True:
        area = float(input("Área afetada (km²): "))
        
        if area > 0:
            areas_afetadas.append(area)
            break
        else:
            print("Erro: a área deve ser maior que zero.")

    while True:
        intensidade = int(input("Intensidade (1 a 10): "))
        
        if 1 <= intensidade <= 10:
            intensidades.append(intensidade)
            break
        else:
            print("Erro: a intensidade deve estar entre 1 e 10.")
            
    ocorrencias.append(
        int(input("Número de ocorrências: "))
    )
    
# EXIBIÇÃO DOS DADOS
print("\n=== DADOS REGISTRADOS ===")

for i in range(quantidade):
    print(f"\nEvento {i + 1}")
    print("Tipo:", tipos_eventos[i])
    print("País:", paises[i])
    print("Região:", regioes[i])
    print("Cidade:", cidades[i])
    print("Área afetada:", areas_afetadas[i], "km²")
    print("Intensidade:", intensidades[i])
    print("Ocorrências:", ocorrencias[i])
    
# 2. ANALISE DOS DADOS
total_eventos = quantidade
soma_areas = sum(areas_afetadas)
media_intensidade = sum(intensidades) / quantidade
indice_maior_area = areas_afetadas.index(max(areas_afetadas))
maior_ocorrencia = max(ocorrencias)
indice_maior_ocorrencia = ocorrencias.index(maior_ocorrencia)

densidade_total = 0

for i in range(quantidade):
    densidade_total += ocorrencias[i] / areas_afetadas[i]

densidade_media = densidade_total / quantidade

acima_media = 0

for intensidade in intensidades:
    if intensidade > media_intensidade:
        acima_media += 1

indice_critico = 0
maior_pontuacao = 0

for i in range(quantidade):
    pontuacao = intensidades[i] + areas_afetadas[i]

    if pontuacao > maior_pontuacao:
        maior_pontuacao = pontuacao
        indice_critico = i
        
# EXIBIÇÃO DOS DADOS
print("\n=== ANÁLISE DOS DADOS ===")
print("Total de eventos:", total_eventos)
print("Soma das áreas afetadas:", soma_areas)
print("Média das intensidades:", media_intensidade)
print("Evento com maior área afetada:",
      tipos_eventos[indice_maior_area])
print("Região com maior número de ocorrências:",
      regioes[indice_maior_ocorrencia])
print("Densidade média:", densidade_media)
print("Quantidade de eventos acima da média:",
      acima_media)
print("Evento mais crítico:",
      tipos_eventos[indice_critico])