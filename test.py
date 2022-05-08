from download_image_and_read_captcha import download_image_and_read_captcha

tests = {
    'https://raw.githubusercontent.com/pierreminiggio/speechelo-captcha-reader-test-data/main/1.png': '96426806'
}

all_tests_ok = True

for image_url in tests:
    expected_result = tests[image_url]
    actual_result = download_image_and_read_captcha(image_url)

    test_ok = expected_result == actual_result

    print(image_url.split('/')[-1] + ' -> Expected : ' + expected_result + ' Actual : ' + actual_result + ' ' + (
        'Ok' if test_ok else 'Pas Ok'
    ))

    if test_ok == False:
        all_tests_ok = False

if all_tests_ok:
    print('Le programme fonctionne parfaitement !')
else:
    print('Le programme a des erreurs !')
