import pandas as pd
import requests
import zipfile
import io

def scrape_macro_economic_factors():
    """
    Scrapes macro economic factors data from the World Bank.
    """
    # URL for the World Bank's GDP growth data (annual %)
    url = "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=csv"

    response = requests.get(url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))

    # Find the correct file in the zip archive
    for file in zip_file.namelist():
        if "API_NY.GDP.MKTP.KD.ZG" in file and not file.startswith("Metadata"):
            csv_file = file
            break

    df = pd.read_csv(zip_file.open(csv_file), header=2)

    # Get the latest GDP growth for the world
    world_gdp_growth = df[df['Country Name'] == 'World'].iloc[0, -2]

    return {
        "global_gdp_growth_percent": float(world_gdp_growth)
    }

if __name__ == '__main__':
    data = scrape_macro_economic_factors()
    import json
    print(json.dumps(data, indent=2))
