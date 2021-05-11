import requests
from bs4 import BeautifulSoup
import pandas as pd

def parse_table():  # Функция разбора таблицы с вопросом
    result = pd.DataFrame()
    url = 'https://dominos.by/'
    res = requests.get(url)  # подключаюсь по указанному урлу


    soup = BeautifulSoup(res.text, "html.parser")
    table = soup.find('div', {'class': 'product-grid__content'})

    pizza = table.find('div', {'data-code': 'RIV'}).find('div', {'class': 'product-card__content'}).find('div', {'class': 'product-card__title'}).text.strip()[0:7]
    pizza2 = table.find('div', {'data-code': 'CB'}).find('div', {'class': 'product-card__content'}).find('div', {'class': 'product-card__title'}).text.strip()[0:8]
    pizza3 = table.find('div', {'data-code': 'PESTO'}).find('div', {'class': 'product-card__content'}).find('div', {'class': 'product-card__title'}).text.strip()[0:12]
    pizza4 = table.find('div', {'data-code': 'CHRN'}).find('div', {'class': 'product-card__content'}).find('div', {'class': 'product-card__title'}).text.strip()
    pizza5 = table.find('div', {'data-code': 'PZBURG'}).find('div', {'class': 'product-card__content'}).find('div', {'class': 'product-card__title'}).text.strip()
    pizza6 = table.find('div', {'data-code': '5CHS'}).find('div', {'class': 'product-card__content'}).find('div', {'class': 'product-card__title'}).text.strip()
    pizza7 = table.find('div', {'data-code': 'DOMINOS'}).find('div', {'class': 'product-card__content'}).find('div', {'class': 'product-card__title'}).text.strip()[0:17]
    pizza8 = table.find('div', {'data-code': '_PRVNS'}).find('div', {'class': 'product-card__content'}).find('div', {'class': 'product-card__title'}).text.strip()
    pizza9 = table.find('div', {'data-code': 'MUNH'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza10 = table.find('div', {'data-code': 'ALSK'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza11 = table.find('div', {'data-code': 'FARM'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza12 = table.find('div', {'data-code': '_BBQDL'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza13 = table.find('div', {'data-code': 'GRIB'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza14 = table.find('div', {'data-code': 'SPS'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza15 = table.find('div', {'data-code': 'CHIKD'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza16 = table.find('div', {'data-code': 'EX22'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza17 = table.find('div', {'data-code': 'SUPREME'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza18 = table.find('div', {'data-code': 'BBQ'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza19 = table.find('div', {'data-code': 'KTR'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza20 = table.find('div', {'data-code': 'GIPN'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza21 = table.find('div', {'data-code': 'PPBL'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza22 = table.find('div', {'data-code': 'TSKN'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza23 = table.find('div', {'data-code': 'CHKR'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza24 = table.find('div', {'data-code': 'KRVTA'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza25 = table.find('div', {'data-code': 'VE'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza26 = table.find('div', {'data-code': 'MTZ'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza27 = table.find('div', {'data-code': 'BAV'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza28 = table.find('div', {'data-code': 'SYTN'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza29 = table.find('div', {'data-code': 'KIA'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza30 = table.find('div', {'data-code': 'HATN'}).find('div', {'class': 'product-card__content'}).find('div', {   'class': 'product-card__title'}).text.strip()
    pizza31 = table.find('div', {'data-code': 'MGRC'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza32 = table.find('div', {'data-code': 'TP'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza33 = table.find('div', {'data-code': 'VG'}).find('div', {'class': 'product-card__content'}).find('div', {    'class': 'product-card__title'}).text.strip()
    pizza34 = table.find('div', {'data-code': 'LES'}).find('div', {'class': 'product-card__content'}).find('div', {   'class': 'product-card__title'}).text.strip()


    price1 = table.find('div', {'data-code': 'RIV'}).find('p', {'class': 'product-card__modification-info-price'}).text.strip()
    price2 = table.find('div', {'data-code': 'CB'}).find('p', {'class': 'product-card__modification-info-price'}).text.strip()
    price3 = table.find('div', {'data-code': 'PESTO'}).find('p', {'class': 'product-card__modification-info-price'}).text.strip()
    price4 = table.find('div', {'data-code': 'CHRN'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price5 = table.find('div', {'data-code': 'PZBURG'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price6 = table.find('div', {'data-code': '5CHS'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price7 = table.find('div', {'data-code': 'DOMINOS'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price8 = table.find('div', {'data-code': '_PRVNS'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price9 = table.find('div', {'data-code': 'MUNH'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price10 = table.find('div', {'data-code': 'ALSK'}).find('p', {'class': 'product-card__modification-info-price'}).text.strip()
    price11 = table.find('div', {'data-code': 'FARM'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price12 = table.find('div', {'data-code': '_BBQDL'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price13 = table.find('div', {'data-code': 'GRIB'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price14 = table.find('div', {'data-code': 'SPS'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price15 = table.find('div', {'data-code': 'CHIKD'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price16 = table.find('div', {'data-code': 'EX22'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price17 = table.find('div', {'data-code': 'SUPREME'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price18 = table.find('div', {'data-code': 'BBQ'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price19 = table.find('div', {'data-code': 'KTR'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price20 = table.find('div', {'data-code': 'GIPN'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price21 = table.find('div', {'data-code': 'PPBL'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price22 = table.find('div', {'data-code': 'TSKN'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price23 = table.find('div', {'data-code': 'CHKR'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price24 = table.find('div', {'data-code': 'KRVTA'}).find('p', { 'class': 'product-card__modification-info-price'}).text.strip()
    price25 = table.find('div', {'data-code': 'VE'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price26 = table.find('div', {'data-code': 'MTZ'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price27 = table.find('div', {'data-code': 'BAV'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price28 = table.find('div', {'data-code': 'SYTN'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price29 = table.find('div', {'data-code': 'KIA'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price30 = table.find('div', {'data-code': 'HATN'}).find('p', {   'class': 'product-card__modification-info-price'}).text.strip()
    price31 = table.find('div', {'data-code': 'MGRC'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price32 = table.find('div', {'data-code': 'TP'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price33 = table.find('div', {'data-code': 'VG'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()
    price34 = table.find('div', {'data-code': 'LES'}).find('p', {    'class': 'product-card__modification-info-price'}).text.strip()




    link1 = 'https://dominos.by/pizza/' + 'RIV'
    link2 = 'https://dominos.by/pizza/' + 'CB'
    link3 = 'https://dominos.by/pizza/' + 'PESTO'
    link4 = 'https://dominos.by/pizza/' + 'CHRN'
    link5 = 'https://dominos.by/pizza/' + 'PZBURG'
    link6 = 'https://dominos.by/pizza/' + '5CHS'
    link7 = 'https://dominos.by/pizza/' + 'DOMINOS'
    link8 = 'https://dominos.by/pizza/' + '_PRVNS'
    link9 = 'https://dominos.by/pizza/' + 'MUNH'
    link10 = 'https://dominos.by/pizza/' + 'ALSK'
    link11 = 'https://dominos.by/pizza/' + 'FARM'
    link12 = 'https://dominos.by/pizza/' + '_BBQDL'
    link13 = 'https://dominos.by/pizza/' + 'GRIB'
    link14 = 'https://dominos.by/pizza/' + 'SPS'
    link15 = 'https://dominos.by/pizza/' + 'CHIKD'
    link15 = 'https://dominos.by/pizza/' + 'EX22'
    link16 = 'https://dominos.by/pizza/' + 'SUPREME'
    link17 = 'https://dominos.by/pizza/' + 'BBQ'
    link18 = 'https://dominos.by/pizza/' + 'KTR'
    link19 = 'https://dominos.by/pizza/' + 'GIPN'
    link20 = 'https://dominos.by/pizza/' + 'PPBL'
    link21 = 'https://dominos.by/pizza/' + 'TSKN'
    link22 = 'https://dominos.by/pizza/' + 'CHKR'
    link23 = 'https://dominos.by/pizza/' + 'KRVTA'
    link24 = 'https://dominos.by/pizza/' + 'VE'
    link25 = 'https://dominos.by/pizza/' + 'MTZ'
    link26 = 'https://dominos.by/pizza/' + 'BAV'
    link27 = 'https://dominos.by/pizza/' + 'SYTN'
    link28 = 'https://dominos.by/pizza/' + 'KIA'
    link29 = 'https://dominos.by/pizza/' + 'HATN'
    link30 = 'https://dominos.by/pizza/' + 'MGRC'
    link31 = 'https://dominos.by/pizza/' + 'TP'
    link32 = 'https://dominos.by/pizza/' + 'VG'
    link33 = 'https://dominos.by/pizza/' + 'LES'


    resultik = result.append(pd.DataFrame([[pizza,pizza2,pizza3,pizza4,pizza5,pizza6,pizza7,pizza8,pizza9,pizza10,pizza11,
                                            pizza12,pizza13,pizza14,pizza15,pizza16,pizza17,pizza18,pizza19,pizza20,pizza21,pizza22,pizza23,pizza24,
                                            pizza25,pizza26,pizza27,pizza28,pizza29,pizza30,pizza31,pizza32,pizza33,pizza34,
                                            price1,price2,price3,price4,price5,price6,price7,price8,price9,price10,price11,price12,price13,
                                            price14,price15,price16,price17, price18,price19,price20,price21,price22,price23,price24,price25,price26,
                                           price27,price28,price29,price30,price31,price32,price33,price34,link1,link2,link3,link4,link5,link6,link7,link8,link9,
                                            link10,link11,link12,link13,link14,link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,link28,
                                            link29,link30,link31,link32,link33]],
                                  columns=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24',
                                           '25','26','27','28','29','30','31','32','33','34',

                                           'price1', 'price2', 'price3', 'price4', 'price5', 'price6', 'price7', 'price8', 'price9', 'price10', 'price11', 'price12',
                                           'price13', 'price14', 'price15', 'price16', 'price17', 'price18', 'price19', 'price20', 'price21', 'price22', 'price23', 'price24',
                                           'price2', 'price26', 'price27', 'price28', 'price29', 'price30', 'price31', 'price32', 'price33', 'price34',

                                           'link1','link2','link3','link4','link5','link6','link7','link8','link9','link10','link11','link12','link13','link14','link15','link16','link17',
                                           'link18','link19','link20','link21','link22','link23','link24',' link25','link26','link27','link28','link29','lin30','link31','link32','link33'

                                           ]),
                     ignore_index=True)

    resultik.to_excel('res.xlsx')
    return(resultik)

parse_table()