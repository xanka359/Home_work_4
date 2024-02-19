from selene import browser, by, have, command, be
import os


def test_registration_form():
    browser.open('/')
    browser.element('#firstName').should(be.blank).type("NewFirst name")
    browser.element('#lastName').should(be.blank).type("NewLast name")
    browser.element('#userEmail').should(be.blank).type("example@mail.com")
    browser.element('[value="Female"]').perform(command.js.click)
    browser.element('#userNumber').should(be.blank).type(1023456789)
    browser.element('#dateOfBirth').click()
    browser.element(".react-datepicker__month-select").click().element(by.text('June')).click()
    browser.element(".react-datepicker__year-select").click().element(by.text('1995')).click()
    browser.element(".react-datepicker__week .react-datepicker__day--018").click()
    browser.element('#subjectsInput').type("English").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click().should(have.text("Sports"))
    browser.element('#uploadPicture').send_keys(os.path.abspath('photo_1.jpg'))
    browser.element('#currentAddress').should(be.blank).type("Russian Federation, Penza")
    browser.element('#state').element('.css-1wy0on6').click()
    browser.element('#react-select-3-option-0').should(have.text("NCR")).click()
    browser.element('#city').element('.css-1wy0on6').click()
    browser.element('#react-select-4-option-2').should(have.text("Noida")).click()
    browser.element('#submit').click()


    #модальное окно
    browser.element('#example-modal-sizes-title-lg').should(have.text("Thanks for submitting the form"))
    browser.element('.table').should(have.text('NewFirst name NewLast name'))
    browser.element('.table').should(have.text('example@mail.com'))
    browser.element('.table').should(have.text('1023456789'))
    browser.element('.table').should(have.text('18 June,1995'))
    browser.element('.table').should(have.text('English'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('photo_1.jpg'))
    browser.element('.table').should(have.text('NCR'))
    browser.element('.table').should(have.text('Noida'))
    browser.element('#closeLargeModal').click()
