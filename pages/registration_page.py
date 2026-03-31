from selene import browser, have, by


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def select_gender(self, value):
        browser.element(f'label[for="gender-radio-{value}"]').click()
        return self

    def fill_phone(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_birth_date(self, day, month_value, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(
            f'.react-datepicker__month-select'
        ).element(f'option[value="{month_value}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(
            '.react-datepicker__year-select'
        ).element(f'option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def select_hobby(self, number):
        browser.element(f'label[for="hobbies-checkbox-{number}"]').click()
        return self

    def upload_picture(self, path):
        browser.element('#uploadPicture').send_keys(str(path))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        browser.element('#state').click()
        browser.element('#state').element(by.text(value)).click()
        return self

    def select_city(self, value):
        browser.element('#city').click()
        browser.element('#city').element(by.text(value)).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_registered(self, *expected_pairs):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text('Thanks for submitting the form')
        )
        browser.element('.table-responsive').all('tr').should(
            have.exact_texts(
                'Label Values',
                *[f'{label} {value}' for label, value in expected_pairs]
            )
        )
        return self


registration_page = RegistrationPage()
