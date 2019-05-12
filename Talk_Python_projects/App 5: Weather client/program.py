import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond,temp,scale,loc')



def main():

    print_the_header()

    code = input('What zipcode do you want the weather for(95051)? ')

    html = get_html_from_web(code)

    report = get_weather_from_html(html)
    #display the forecast
    print('The temp in {} is {} {} and {}'.format(report.loc,report.temp,report.scale,report.cond))


def print_the_header():
    print("============================")
    print("        Weather App         ")
    print("============================")
    print("")



def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/us/ca/santa-clara/zmw:{}.1.99999'.format(zipcode)

    response = requests.get(url)
    #print(response.status_code)
    #print(response.text[0:250])
    return response

def get_weather_from_html(html):
    #cityCss = 'div#location h1'
    #weatherConditionCss = 'div#curCond span.wx-value'
    #weatherTempCss = 'div#curTemp span.wx-data span.wx-value'
    #weatherScaleCss = 'div#curTemp span.wx-data span.wx-unit'

    soup = bs4.BeautifulSoup(html.text,"html.parser")
    loc = soup.find(id ='location').find('h1').get_text()
    condition = soup.find(id = 'curCond').find(class_='wx-value').get_text()
    temp = soup.find(id = 'curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id = 'curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    temp = cleanup_text(temp)
    condition = cleanup_text(condition)
    scale = cleanup_text(scale)

    report = WeatherReport(cond = condition,temp = temp,scale = scale, loc = loc)
    return report
    #return (condition,temp,scale,loc)

    #print (condition,temp,scale,loc)


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text

def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()



if __name__ == '__main__':
    main()