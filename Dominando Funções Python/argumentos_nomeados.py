def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}, {modelo}, {ano}, {placa}")

salvar_carro("Fiat", "Palio", "1999", "ABC-1234")
salvar_carro(marca= "Wolksvagen", modelo= "Gol", ano= "2010", placa= "BCD-2345")
salvar_carro(**{"marca": "Fiat", "modelo": "Uno", "ano": "1995", "placa": "CDE=3456"})