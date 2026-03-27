from pathlib import Path

import allure

from pages.registration_page import registration_page

file_path = Path(__file__).parent.parent / 'resources' / 'images.jpeg'


@allure.tag('web')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка успешной регистрации студента')
@allure.feature('Student Registration Form')
@allure.story('Пользователь может успешно заполнить и отправить форму')
def test_register_student():
    with allure.step('Открыть форму регистрации'):
        registration_page.open()

    with allure.step('Заполнить форму валидными данными'):
        (
            registration_page
            .fill_first_name('Иван')
            .fill_last_name('Петров')
            .fill_email('ivanov@example.com')
            .select_gender(1)
            .fill_phone('1234567890')
            .fill_birth_date(day='10', month_value='1', year='1995')
            .fill_subject('Maths')
            .select_hobby(1)
            .upload_picture(file_path.resolve())
            .fill_address('Москва, ул.Гоголя 10')
            .select_state('NCR')
            .select_city('Delhi')
            .submit()
        )

    with allure.step('Проверить данные в модальном окне результата'):
        registration_page.should_have_registered(
            ('Student Name', 'Иван Петров'),
            ('Student Email', 'ivanov@example.com'),
            ('Gender', 'Male'),
            ('Mobile', '1234567890'),
            ('Date of Birth', '10 February,1995'),
            ('Subjects', 'Maths'),
            ('Hobbies', 'Sports'),
            ('Picture', 'images.jpeg'),
            ('Address', 'Москва, ул.Гоголя 10'),
            ('State and City', 'NCR Delhi'),
        )
