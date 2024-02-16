# Description: Este script preenche um formulário web e imprime a mensagem de resultado.
# Ref: https://www.selenium.dev/documentation/
# Importa as bibliotecas necessárias
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Instala o ChromeDriver compatível com a versão do Chrome
driver = ChromeDriverManager().install()

# Cria uma instância do navegador Chrome
driver = webdriver.Chrome()

# Cria um objeto de opções para personalizar o navegador
options = Options()

# Options

# Maximiza a janela do navegador
options.add_argument("start-maximized")

# Mantém o navegador aberto após o script terminar (recurso experimental)
options.add_experimental_option("detach", True)

# Cria um novo WebDriver com as opções configuradas
driver = webdriver.Chrome(options=options)

# Navega até a página do formulário web
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Localiza a caixa de texto pelo nome "my-text"
text_box = driver.find_element(by=By.NAME, value="my-text")

# Localiza o botão de envio pelo seletor CSS "button"
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# Digita "Selenium" na caixa de texto
text_box.send_keys("Selenium")

# Clica no botão de envio
submit_button.click()

# Localiza o elemento que exibe a mensagem de resultado
message = driver.find_element(by=By.ID, value="message")

# Obtém o texto da mensagem de resultado
text = message.text

# Imprime a mensagem de resultado
print(f"Text: {text}")
