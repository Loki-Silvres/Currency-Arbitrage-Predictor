from exchange_rates import get_exchange_rates
from datetime import datetime
import pandas as pd

# Hypothetical investment amount
INVESTMENT_AMOUNT = 1000000  # Example amount in EUR
INVESTED_CURRENCY = "EUR"

# Function to fetch live exchange rates
def get_rates_today(base: str, target_currencies: list[str]):
    try:
        today_date = str(datetime.now().date())
        rates = get_exchange_rates(base.upper(), target_currencies=target_currencies, on_date=today_date)
        return rates
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to analyze for triangular arbitrage
def analyze_arbitrage(rates, currency_triad):
    try:
        # Assuming rates are relative to EUR:
        rate1_eur = rates[currency_triad[0]]  # EUR to currency1
        rate2_eur = rates[currency_triad[1]]  # EUR to currency2
        rate3_eur = rates[currency_triad[2]]  # EUR to currency3

        # Calculate inferred cross-rates
        rate1_to_2 = rate2_eur / rate1_eur  # currency1 to currency2
        rate2_to_3 = rate3_eur / rate2_eur  # currency2 to currency3
        rate3_to_1 = rate1_eur / rate3_eur  # currency3 to currency1

        # Perform the conversions in sequence
        amount_in_currency2 = INVESTMENT_AMOUNT * rate1_to_2  # currency1 -> currency2
        amount_in_currency3 = amount_in_currency2 * rate2_to_3  # currency2 -> currency3
        final_amount_in_currency1 = amount_in_currency3 * rate3_to_1  # currency3 -> currency1

        # Calculate profit
        profit = final_amount_in_currency1 - INVESTMENT_AMOUNT

        # Return results if there's an arbitrage opportunity
        if profit > 0:  # A threshold for arbitrage opportunity
            return {
                'currencies': currency_triad,
                'profit': profit
            }
        else:
            return None
    except KeyError as e:
        print(f"Currency {e} not available in the API data.")
        return None



# Main function to check for arbitrage and save results to a notebook
def check_arbitrage_opportunities():
    # List of currencies to analyze
    currencies = [
        "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
        "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
        "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
        "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP",
        "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GGP", "GHS",
        "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF",
        "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD",
        "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT",
        "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD",
        "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN",
        "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK",
        "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR",
        "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP",
        "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD",
        "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND",
        "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"
    ]
    
    # Infinite loop to check for arbitrage opportunities
    
    # Fetch live rates
    live_rates:dict = {}
    for currency in currencies:
        live_rates[currency] = get_rates_today(base=currency, target_currencies=currencies)
    # print(live_rates['EUR'])

    # live_rates = {'AED': 3.994584, 'AFN': 72.841556, 'ALL': 98.261179, 'AMD': 420.443555, 'ANG': 1.957935, 'AOA': 991.859225, 'ARS': 1076.941719, 'AUD': 1.657849, 'AWG': 1.957618, 'AZN': 1.867257, 'BAM': 1.955037, 'BBD': 2.193533, 'BDT': 129.820501, 'BGN': 1.956258, 'BHD': 0.410008, 'BIF': 3156.238515, 'BMD': 1.087565, 'BND': 1.436026, 'BOB': 7.507034, 'BRL': 6.298099, 'BSD': 1.086371, 'BTC': 1.5741724e-05, 'BTN': 91.265201, 'BWP': 14.524328, 'BYN': 3.555295, 'BYR': 21316.280309, 'BZD': 2.189835, 'CAD': 1.516001, 'CDF': 3140.341889, 'CHF': 0.939885, 'CLF': 0.037895, 'CLP': 1045.629306, 'CNY': 7.746833, 'CNH': 7.742698, 'COP': 4808.99634, 'CRC': 556.682624, 'CUC': 1.087565, 'CUP': 28.820481, 'CVE': 110.222973, 'CZK': 25.328854, 'DJF': 193.45357, 'DKK': 7.459534, 'DOP': 65.424453, 'DZD': 144.746705, 'EGP': 53.239153, 'ERN': 16.31348, 'ETB': 133.439254, 'EUR': 1, 'FJD': 2.447894, 'FKP': 0.832171, 'GBP': 0.843271, 'GEL': 2.985344, 'GGP': 0.832171, 'GHS': 17.632277, 'GIP': 0.832171, 'GMD': 77.217699, 'GNF': 9369.341411, 'GTQ': 8.393877, 'GYD': 227.183377, 'HKD': 8.458284, 'HNL': 27.384929, 'HRK': 7.49227, 'HTG': 142.952865, 'HUF': 407.934449, 'IDR': 17106.26057, 'ILS': 4.071986, 'IMP': 0.832171, 'INR': 91.447938, 'IQD': 1423.150824, 'IRR': 45778.341963, 'ISK': 148.909415, 'JEP': 0.832171, 'JMD': 171.870517, 'JOD': 0.771303, 'JPY': 165.705839, 'KES': 140.143826, 'KGS': 93.328557, 'KHR': 4414.235718, 'KMF': 493.322512, 'KPW': 978.808544, 'KRW': 1498.697383, 'KWD': 0.333449, 'KYD': 0.905355, 'KZT': 530.427753, 'LAK': 23832.912742, 'LBP': 97285.664129, 'LKR': 318.258651, 'LRD': 208.588549, 'LSL': 19.179423, 'LTL': 3.211298, 'LVL': 0.657857, 'LYD': 5.235931, 'MAD': 10.689524, 'MDL': 19.446317, 'MGA': 5006.045214, 'MKD': 61.59095, 'MMK': 3532.369742, 'MNT': 3695.546994, 'MOP': 8.697584, 'MRU': 42.956226, 'MUR': 49.875215, 'MVR': 16.693738, 'MWK': 1883.764418, 'MXN': 21.822046, 'MYR': 4.766259, 'MZN': 69.500207, 'NAD': 19.179687, 'NGN': 1786.173969, 'NIO': 39.974391, 'NOK': 11.977727, 'NPR': 146.020967, 'NZD': 1.822798, 'OMR': 0.418694, 'PAB': 1.086471, 'PEN': 4.09104, 'PGK': 4.3523, 'PHP': 63.552424, 'PKR': 301.88012, 'PLN': 4.353731, 'PYG': 8588.606791, 'QAR': 3.961026, 'RON': 4.974849, 'RSD': 117.050323, 'RUB': 105.902682, 'RWF': 1479.222386, 'SAR': 4.084777, 'SBD': 9.044554, 'SCR': 14.811732, 'SDG': 654.173227, 'SEK': 11.599673, 'SGD': 1.439785, 'SHP': 0.832171, 'SLE': 24.63355, 'SLL': 22805.697539, 'SOS': 620.849005, 'SRD': 37.376332, 'STD': 22510.406377, 'SVC': 9.506375, 'SYP': 2732.54079, 'SZL': 19.188507, 'THB': 36.846838, 'TJS': 11.570135, 'TMT': 3.817354, 'TND': 3.357851, 'TOP': 2.547189, 'TRY': 37.324965, 'TTD': 7.372189, 'TWD': 34.704538, 'TZS': 2947.301743, 'UAH': 44.775516, 'UGX': 3977.483424, 'USD': 1.087565, 'UYU': 44.762932, 'UZS': 13884.578278, 'VEF': 3939762.513183, 'VES': 46.391734, 'VND': 27542.591777, 'VUV': 129.117972, 'WST': 3.046471, 'XAF': 655.700959, 'XAG': 0.032241, 'XAU': 0.0004, 'XCD': 2.9392, 'XDR': 0.816581, 'XOF': 655.697945, 'XPF': 119.331742, 'YER': 272.244803, 'ZAR': 19.186447, 'ZMK': 9789.395659, 'ZMW': 29.087508, 'ZWL': 350.19559}
    # breakpoint()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp
    results = []  # Temporary list to store results before appending to CSV

    if live_rates:
        # Analyze each possible triad combination
        
        for i in range(len(currencies)):
            for j in range(i + 1, len(currencies)):
                # Ensure all three currencies are in the live rates
                if currencies[i] not in live_rates[INVESTED_CURRENCY] or currencies[j] not in live_rates[INVESTED_CURRENCY]:
                    continue
                
                currency_triad = (INVESTED_CURRENCY, currencies[i], currencies[j], INVESTED_CURRENCY)
                gain = live_rates[currencies[i]][INVESTED_CURRENCY] * live_rates[currencies[j]][currencies[i]] * live_rates[INVESTED_CURRENCY][currencies[j]]
                print(gain)
                # breakpoint()
                result = {}
                result["currencies"] = currency_triad  
                result["profit"] = round((gain - 1) * INVESTMENT_AMOUNT, 5)  
                result["timestamp"] = timestamp  
                if result:
                    # Add result to temporary list
                    results.append(result)

        # Convert results list to a DataFrame and append to CSV
        if results:
            df = pd.DataFrame(results)
            df.to_csv('arbitrage_opportunities.csv', mode='w', header=not pd.io.common.file_exists('arbitrage_opportunities.csv'), index=False)
            print(f"{len(results)} arbitrage opportunities saved at {timestamp}")

    else:
        print("Failed to fetch live rates.")

check_arbitrage_opportunities()