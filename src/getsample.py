
from selenium import webdriver

def get_detail_page(driver, url):
    try:
        driver.get(url)
        value = driver.find_element_by_id("pagenum").get_attribute("value")
        print value, url
        mobile_url = "http://image.58.com/showphone.aspx?t=v55&v=%s" % value
    except Exception as ex:
        print ex

def main():
    driver = webdriver.Firefox()
    for i in range(1):
        url = "http://sz.58.com/yewu/pn%s/" % i
        driver.get(url)
        elms = driver.find_elements_by_css_selector("#infolist > dl")
        detail_hrefs = []
        for elm in elms:
            detail_hrefs.append(elm.find_element_by_css_selector("dt > a").get_attribute("href"))
    
        for href in detail_hrefs:
            get_detail_page(driver, href)
            
    driver.close()
    
main()