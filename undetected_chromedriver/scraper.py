# import the required modules
import undetected_chromedriver as uc
from multiprocessing import freeze_support

if __name__ == '__main__':

    # call freeze support to ensure the creation of an executable
    freeze_support()

    # create a ChromeDriver instance
    driver = uc.Chrome(headless=False, use_subprocess=False)
    
    # quit the driver
    driver.quit()
