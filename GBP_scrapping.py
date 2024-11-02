from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
from selenium.webdriver.chrome.options import Options


options = Options()
# options.add_argument("--headless")  # Run Chrome in headless mode


def get_exchange_rates(base_currency = "USD", target_currencies = ["EUR", "GBP", "USD"], on_date = "2023-10-02"):

    month_names = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    driver = webdriver.Chrome(options=options)

    currency_codes = {
        "Australian Dollar": "AUD",
        "Canadian Dollar": "CAD",
        "Euro": "EUR",
        "Sterling": "GBP",
        "Pound Sterling": "GBP",
        "United States Dollar": "USD",
        "US Dollar": "USD",
        "British Pound Sterling": "GBP",
        "Japanese Yen": "JPY",
        "Chinese Yuan Renminbi": "CNY",
        "Swiss Franc": "CHF",
        "Swedish Krona": "SEK",
        "Norwegian Krone": "NOK",
        "Danish Krone": "DKK",
        "Hong Kong Dollar": "HKD",
        "Singapore Dollar": "SGD",
        "New Zealand Dollar": "NZD",
        "South African Rand": "ZAR",
        "Malaysian ringgit": "MYR",
        "Thai Baht": "THB",
        "Indonesian Rupiah": "IDR",
        "Philippine Peso": "PHP",
        "Vietnamese Dong": "VND",
        "Russian Ruble": "RUB",
        "South Korean Won": "KRW",
        "UAE Dirham": "AED",
        "Swazi Lilangeni": "SZL",
        "Czech Koruna": "CZK",
        "Hungarian Forint": "HUF",
        "Romanian Leu": "RON",
        "Croatian Kuna": "HRK",
        "Indian Rupee": "INR",
        "Brazilian Real": "BRL",
        "Argentine Peso": "ARS",
        "Colombian Peso": "COP",
        "Mexican Peso": "MXN",
        "Chinese Yuan": "CNY",
        "Israeli Shekel": "ILS",
        "Polish Zloty": "PLN",
        "Saudi Riyal": "SAR",
        "Taiwan Dollar": "TWD",
        "Turkish Lira": "TRY",
        "Bulgarian Lev": "BGN",
        "Icelandic Krona": "ISK",
        "Egyptian Pound": "EGP",
        "Pakistani Rupee": "PKR",
        "Bangladeshi Taka": "BDT",
        "Chilean Peso": "CLP",
        "Peruvian Sol": "PEN",
        "Ukrainian Hryvnia": "UAH",
        "Jordanian Dinar": "JOD",
        "Lebanese Pound": "LBP",
        "Iraqi Dinar": "IQD",
        "Qatari Riyal": "QAR",
        "Kuwaiti Dinar": "KWD",
        "Bahraini Dinar": "BHD",
        "Omani Rial": "OMR",
        "Ghanaian Cedi": "GHS",
        "Nigerian Naira": "NGN",
        "Kenyan Shilling": "KES",
        "Tanzanian Shilling": "TZS",
        "Ugandan Shilling": "UGX",
        "Sri Lankan Rupee": "LKR",
        "Mongolian Tugrik": "MNT",
        "Uzbekistani Som": "UZS",
        "Kazakhstani Tenge": "KZT",
        "Georgian Lari": "GEL",
        "Armenian Dram": "AMD",
        "Azerbaijani Manat": "AZN",
        "Algerian Dinar": "DZD",
        "Moroccan Dirham": "MAD",
        "Tunisian Dinar": "TND",
        "Libyan Dinar": "LYD",
        "Angolan Kwanza": "AOA",
        "Botswana Pula": "BWP",
        "Mozambican Metical": "MZN",
        "Zambian Kwacha": "ZMW",
        "Zimbabwean Dollar": "ZWL",
        "Malawian Kwacha": "MWK",
        "Seychellois Rupee": "SCR",
        "Mauritian Rupee": "MUR",
        "Cuban Peso": "CUP",
        "Dominican Peso": "DOP",
        "Costa Rican Colón": "CRC",
        "Panamanian Balboa": "PAB",
        "Paraguayan Guarani": "PYG",
        "Uruguayan Peso": "UYU",
        "Bolivian Boliviano": "BOB",
        "Venezuelan Bolivar": "VES"
    }
    base_url = "https://www.bankofengland.co.uk/boeapps/database/Rates.asp?"

    postfix = f"TD={(on_date[8:10]).lstrip('0')}&TM={month_names[on_date[5:7]]}&TY={on_date[0:4]}&into={base_currency}"
    # print(postfix)

    url = base_url + postfix
    driver.get(url)

    driver.implicitly_wait(10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    table = soup.find('table')
    # print(table)
    tbody = table.find('tbody')
    results = {}
    if tbody:
        for row in tbody.find_all('tr'):
            cells = row.find_all('td')
            cell_values = [cell.get_text(strip=True) for cell in cells]
            # print(cell_values)
            currency_code = currency_codes[cell_values[0]]
            if currency_code in target_currencies:
                results[currency_codes[cell_values[0]]] = float(cell_values[1])
    if not results:
        print("Invalid business date.")
    return results

today_date = str(datetime.now().date())

base_currencies = ["USD", "EUR", "GBP"]
target_currencies = ["GBP", "EUR", "USD"]
rates = {}
for base_currency in base_currencies:
    rates[base_currency] = get_exchange_rates(base_currency, target_currencies)

print(rates)

# usd_rates = get_exchange_rates(base_currency = "USD")
# print(usd_rates)
# eur_rates = get_exchange_rates(base_currency = "EUR")
# print(eur_rates)
# gbp_rates = get_exchange_rates(base_currency = "GBP")
# print(gbp_rates)