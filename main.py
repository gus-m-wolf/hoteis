from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

@app.route("/buscar-hoteis", methods=["POST"])
def buscar_hoteis():
    dados = request.json
    checkin_data = dados.get("checkin_data")
    checkout_data = dados.get("checkout_data")
    pessoas = str(dados.get("pessoas"))

    # Divide as datas
    checkin_dia, checkin_mes, checkin_ano = checkin_data.split("/")
    checkout_dia, checkout_mes, checkout_ano = checkout_data.split("/")

    # Monta a URL
    url = (
        f"https://www.booking.com/searchresults.html?ss=Gramado%2C+Rio+Grande+do+Sul%2C+Brasil"
        f"&checkin_year=20{checkin_ano}&checkin_month={int(checkin_mes)}&checkin_monthday={int(checkin_dia)}"
        f"&checkout_year=20{checkout_ano}&checkout_month={int(checkout_mes)}&checkout_monthday={int(checkout_dia)}"
        f"&group_adults={pessoas}&group_children=0&no_rooms=1&nflt=mealplan%3D1&order=price"
    )

    # Configurações para rodar no ambiente da Render
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.binary_location = "/opt/render/project/.render/chrome/opt/google/chrome"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)

    wait = WebDriverWait(driver, 20)
    time.sleep(8)
    time.sleep(3)

    try:
        total_acomodacoes = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.b87c397a13.cacb5ff522')))
        total_texto = total_acomodacoes.text
    except:
        total_texto = "Número total de acomodações não encontrado."

    nomes = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="title"]')
    precos = driver.find_elements(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]')

    resultados = []
    for i in range(min(len(nomes), len(precos))):
        resultados.append(f"{nomes[i].text} - {precos[i].text}")

    driver.quit()

    return jsonify({
        "total": total_texto,
        "resultados": resultados
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
