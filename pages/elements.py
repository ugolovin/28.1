from selenium.webdriver.common.by import By


class AuthLocators:
    auth_username = (By.ID, "username")
    auth_password = (By.ID, "password")
    auth_button = (By.ID, "kc-login")
    placeholder = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    forget_pass_link = (By.ID, "forgot_password")
    reg_link = (By.ID, 'kc-register')
    vk_button = (By.ID, "oidc_vk")
    ok_button = (By.ID, 'oidc_ok')
    mailru_button = (By.ID, 'oidc_mail')
    google_button = (By.ID, 'oidc_google')
    ya_button = (By.ID, 'oidc_ya')


res_pass_text = (By.XPATH, '//*[@id="page-right"]/div/div/h1')
internal_error_message_text = (By.XPATH, '/html/body')
wrong_log_pass_message = (By.XPATH, '//*[@id="page-right"]/div/div/p')
reg_page_text = (By.XPATH, '//*[@id="page-right"]/div/div/h1')

