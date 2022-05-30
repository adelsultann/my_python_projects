import requests, json
from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree
from requests_html import HTMLSession

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

urls = {}

urls[
    "Balance Sheet"] = "https://www.saudiexchange.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/pZBLb4JAFIV_iwvWcxgQsDsKChQkpRSKszGDD0rCa4Ea--s7PjYmLdb07m7yfefmHsJIRljD92XB-7JteCX2BdOWoRtYLgzqO9N3BaZmz6230KMAyMcZoNQy5ImKAIEuC8CBF81VBZFC2EO-44U6zMh001kqUIP-z4f6Nx-_jIl7_gthRdXml6o--757kiCh52t-2FWS0Fdt3fHmGB_rvBWQDvl0lN3mwqW2yJ36vm2NKZ7HV2Co11vgh-IGgVMzZ2Dg9XjTkK5OkiT7CraxV74Wo9E3u3t8eg!!/p0/IZ7_NHLCH082KGET30A6DMCRNI2086=CZ6_NHLCH082KGET30A6DMCRNI2000=NJstatementsTabData=/?statementType=0&reportType=0&symbol=7010"
urls[
    "Statement of Income"] = "https://www.saudiexchange.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/pZBLb4JAFIV_iwvWcxgQsDsKChQkpRSKszGDD0rCa4Ea--s7PjYmLdb07m7yfefmHsJIRljD92XB-7JteCX2BdOWoRtYLgzqO9N3BaZmz6230KMAyMcZoNQy5ImKAIEuC8CBF81VBZFC2EO-44U6zMh001kqUIP-z4f6Nx-_jIl7_gthRdXml6o--757kiCh52t-2FWS0Fdt3fHmGB_rvBWQDvl0lN3mwqW2yJ36vm2NKZ7HV2Co11vgh-IGgVMzZ2Dg9XjTkK5OkiT7CraxV74Wo9E3u3t8eg!!/p0/IZ7_NHLCH082KGET30A6DMCRNI2086=CZ6_NHLCH082KGET30A6DMCRNI2000=NJstatementsTabData=/?statementType=1&reportType=0&symbol=7010"
urls[
    "Cash Flow"] = "https://www.saudiexchange.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/pZBLb4JAFIV_iwvWcxgQsDsKChQkpRSKszGDD0rCa4Ea--s7PjYmLdb07m7yfefmHsJIRljD92XB-7JteCX2BdOWoRtYLgzqO9N3BaZmz6230KMAyMcZoNQy5ImKAIEuC8CBF81VBZFC2EO-44U6zMh001kqUIP-z4f6Nx-_jIl7_gthRdXml6o--757kiCh52t-2FWS0Fdt3fHmGB_rvBWQDvl0lN3mwqW2yJ36vm2NKZ7HV2Co11vgh-IGgVMzZ2Dg9XjTkK5OkiT7CraxV74Wo9E3u3t8eg!!/p0/IZ7_NHLCH082KGET30A6DMCRNI2086=CZ6_NHLCH082KGET30A6DMCRNI2000=NJstatementsTabData=/?statementType=2&reportType=0&symbol=7010"
xlwriter = pd.ExcelWriter("STC.xlsx", engine='xlsxwriter')

n = 0
for key in urls.keys():
    response = requests.get(urls[key], headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    a = soup.find(id=f"statementsTable{n}")

    df = pd.read_html(str(soup), attrs={"id": f"statementsTable{n}"})[0]
    df.to_excel(xlwriter, sheet_name=key, index=False)
    n += 1
    print(df)
xlwriter.save()


