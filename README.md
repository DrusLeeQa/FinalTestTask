# FinalTestTask
Test Task for Alex Smit Course
Описание проделанной работы:
Покупаемый продукт: Xiaomi Телевизор Mi LED TV 4S 50

Шаги теста:

1) Открываем в браузере "https://www.wildberries.ru/" (сделано)

2) Вводим в поиск "Телевизоры" и нажимаем Enter на клавиатуре (сделано)
	Локатор: "//input[@id='searchInput']"
	
3) Выбираем бренд: (сделано)
	а) Нажимаем по фильтру бренда, локатор выбора брендов "(//button[@class='dropdown-filter__btn'])[2]"
	б) Нажимаем "Показать все", локатор "//button[@class='filter__show-all j-show-whole-filters']"
	в) Вбиваем в поиск название бренда "Xiaomi", локатор "//input[@class='j-search-filter']"
	г) Среди всего нашедшегося, выбираем именно "Xiaomi", локатор "//span[text()='Xiaomi']"
	д) Нажимаем "Готово", локатор "//*[contains(text(), 'Готово')]"

4) Выбираем цену: (сделано)
	а) Нажимаем по фильтру цены, локатор фильтра цены "(//button[@class='dropdown-filter__btn'])[4]"
	б) Вводим в поле от сумму 30 000, локатор "//input[@name='startN']"
	в) Вводим в поле до сумму 50 000, локатор "//input[@name='endN']"
	г) Нажимаем "Готово", локатор "//*[contains(text(), 'Готово')]"
	
5) Выбираем остальные фильтры: (сделано)
	а) Нажимаем "Показать все фильтры", локатор "//button[@class='dropdown-filter__btn dropdown-filter__btn--all']"
	б) Листаем до диагонали 55"
	в) Выбираем диагональ 55", локатор "//span[text()='55"']"
	г) Листаем до Wi-Fi
	д) Выбираем Smart TV, локатор "//span[text()='Smart TV']"
	е) Выбираем Wi-Fi, локатор "//span[text()='Wi-Fi']"

6) Щёлкаем по нашему телевизоу, локатор "//span[text()='Телевизор Mi LED TV 4S 50']" (сделано)

7) Находимся на странице с выбранным телевизором: (сделано)
	а) Запоминаем название товара, локатор "//h1[@data-link='text{:selectedNomenclature^goodsName || product^goodsName}']"
	б) Запоминаем цену товара, локатор "//ins[@class='price-block__final-price']"
	в) Нажимаем "Добавить в корзину", локатор "(//span[@class='price-block__price'])[2]"
	г) Нажимаем "Перейти в козину", локатор "(//a[@class='btn-base j-go-to-basket'])[2]"
	
8) Находимся в корзине: (сделано)
	а) Проверить что совпало название, локатор названия в корзине "//span[@class='good-info__good-name']"
	б) Проверить что совпала цена, локатор цены в корзине "//div[@class='list-item__price-new']"
		Дополнительно: нужно обрезать у цены 2 последних символа
