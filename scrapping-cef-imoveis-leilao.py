from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = ChromeDriverManager().install()
driver = webdriver.Chrome()

options = Options()
options.add_experimental_option("detach", True)
# options.add_argument("--disable-gpu")
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Navega até a página do formulário web
driver.get("https://venda-imoveis.caixa.gov.br/sistema/download-lista.asp")

# Localiza select pelo id
select = driver.find_element(by=By.ID, value="cmb_estado")

# Localiza o botao download
botao_download = driver.find_element(by=By.ID, value="btn_next1")

# Retorna todas as opções do select
options = select.find_elements(by=By.TAG_NAME, value="option")

# Faz laco para capturar todas opcoes de download
for option in options[1:]:
    print(option.text)

    # Clica no select e seleciona o estado
    select.click()
    select.send_keys(option.text)

    # Clica no botao para download
    botao_download.click()

    # Aguarda 5 segundos
    driver.implicitly_wait(5)

    # log
    print(f"Download do estado {option.text} concluído")

    # Sai do for na terceira iteracao
    if option.text == "AP":
        break


# Fecha o navegador
driver.quit()