from download_image_and_read_captcha import download_image_and_read_captcha

pierre_repo = 'https://raw.githubusercontent.com/pierreminiggio/speechelo-captcha-reader-test-data/main/'
png = '.png'

tests = {
    pierre_repo + '1' + png: '96426806',
    pierre_repo + '2' + png: '06382105',
    pierre_repo + '3' + png: '34370923',
    pierre_repo + '4' + png: '91895293',
    pierre_repo + '5' + png: '38326032',
    pierre_repo + '6' + png: '31513634',
    pierre_repo + '7' + png: '21789966',
    pierre_repo + '8' + png: '13173183',
    pierre_repo + '9' + png: '95297053',
    pierre_repo + '10' + png: '02855510',
    pierre_repo + '11' + png: '10967584'
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
