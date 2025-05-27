from playwright.sync_api import Page, expect, sync_playwright
import pytest

# ověření, že engeto umí ověřit platnost emailové adresy a vrací chybu

@pytest.mark.parametrize("invalid_email", [
    "neplatny-email",
    "test@",
    "@domena.cz",
    "abc@abc",
    "prdel123"
])
def test_invalid_email_subscription(page: Page, invalid_email):
    page.goto("https://engeto.cz")

    email_input = page.locator('body > footer > div > div.block-footer-newsletter.flex.flex-mobile-column.gap-8.gap-mobile-24 > div.newsletter-form.flex.flex-mobile-column.gap-8.gap-mobile-16 > label > input.has-text-md-regular-font-size')


    email_input.fill(invalid_email)

    submit_button = page.locator('body > footer > div > div.block-footer-newsletter.flex.flex-mobile-column.gap-8.gap-mobile-24 > div.newsletter-form.flex.flex-mobile-column.gap-8.gap-mobile-16 > a')
    submit_button.click()


    error_message = page.locator(
        "footer .newsletter-form.has-error label > span"
    )
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Prosím zadejte validní emailovou adresu")


#ověření, že mě engeto nenechá registrovat stejný email 2x (nechá ;))

def test_doubled_email(page: Page):
    page.goto("https://engeto.cz")

    email_input = page.locator('body > footer > div > div.block-footer-newsletter.flex.flex-mobile-column.gap-8.gap-mobile-24 > div.newsletter-form.flex.flex-mobile-column.gap-8.gap-mobile-16 > label > input.has-text-md-regular-font-size')


    email_input.fill("test@test.cz")


    submit_button = page.locator('body > footer > div > div.block-footer-newsletter.flex.flex-mobile-column.gap-8.gap-mobile-24 > div.newsletter-form.flex.flex-mobile-column.gap-8.gap-mobile-16 > a')
    submit_button.click()

    email_input = page.locator('body > footer > div > div.block-footer-newsletter.flex.flex-mobile-column.gap-8.gap-mobile-24 > div.newsletter-form.flex.flex-mobile-column.gap-8.gap-mobile-16 > label > input.has-text-md-regular-font-size')


    email_input.fill("test@test.cz")


    submit_button = page.locator('body > footer > div > div.block-footer-newsletter.flex.flex-mobile-column.gap-8.gap-mobile-24 > div.newsletter-form.flex.flex-mobile-column.gap-8.gap-mobile-16 > a')
    submit_button.click()

    error_message = page.locator(
        "footer .newsletter-form.has-error label > span"
    )
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Prosím zadejte emailovou adresu, která v systému ještě není")



#Ověření, že social odkazy fungují (u youtube odklikne data consent)

@pytest.mark.parametrize("social, expected_url", [
    ("facebook", "https://www.facebook.com/engetocom/"),
    ("youtube", "https://www.youtube.com/channel/UCZ5B-ZhfonFTmFH13KUhFNA"),
    ("instagram", "https://www.instagram.com/engeto_academy/?hl=cs"),
    ("linkedin", "https://www.linkedin.com/company/engeto/"),
    ("discord", "https://discord.com/invite/MnGxSHVPW9")
])
def test_social_links_open_correctly(page: Page, social, expected_url):
    page.goto("https://engeto.cz")

    button = page.locator(f'footer .ci-{social}')

    with page.expect_popup() as popup_info:
        button.click()

    new_page = popup_info.value

    new_page.wait_for_timeout(3000)

    if social == "youtube":
        consent = new_page.locator('#yDmH0d > c-wiz > div > div > div > div.v2Yske > div.CqMh6b > div.qqtRac > div.KZ9vpc > form:nth-child(3) > div > div > button > span')
        consent.click()
        new_page.wait_for_timeout(2000)

    expect(new_page).to_have_url(expected_url)