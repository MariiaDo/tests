
"""
https://www.booking.com/index.ru.html?label=gen173nr-1FCAEoggI46AdIM1gEaDuIAQGYASG4ARfIARXYAQHoAQH4AQyIAgGoAgO4AuPgtakGwAIB0gIkZGJmY2JmMWMtODQ5NS00OWMzLWIxMWUtZGE4YWM1Nzc4NTRm2AIG4AIB&sid=422c91b3c4220e7072d1c26e67e5ef00&aid=304142

//input[@name="ss"]
//button[@data-testid="date-display-field-start"]
//button[@data-testid="date-display-field-end"]
//button[@data-testid="occupancy-config"]
//button[@type="submit"]
//div[@data-testid="searchbox-footer"]//input[@name="sb_entire_place"]
//div[@data-testid="searchbox-footer"]//input[@name="sb_flight_search"]
//a[@id="accommodations"]
//a[@id="flights"]
(//div[@data-qmab-component-id="1"]//a)[1]
(//div[@data-testid="webcore-carousel"]//a)[1]
//button[@data-testid="webcore-filter-carousel-tab-trigger" and @aria-controls="CITY"]
//button[@data-testid="webcore-filter-carousel-tab-trigger" and @aria-controls="NATURE_ACTIVE"]
//button[@data-testid="header-language-picker-trigger"]
//button[@data-testid="header-currency-picker-trigger"]
//a[@data-testid="header-custom-action-button"]
//a[@data-testid="header-booking-logo"]
//div[@id="footertopnav"]//a[contains(text(), "Мобильная")]    # знаю, что так лучше не делать, но написала для тренировки contains
//div[@id="footertopnav"]//a[contains(text(), "Ваш аккаунт")]
//a[@data-testid="header-help-center"]


!!!!!Эта группа работает только при открытом календаре, не знаю как с помощью Xpath подступиться к ней с закрытого календаря

//input[@type="checkbox" and @value="exact"]
//input[@type="checkbox" and @value="exact"]/ancestor::li/following-sibling::li//input[@value="1"]
//input[@type="checkbox" and @value="exact"]/ancestor::li/following-sibling::li//input[@value="2"]
//input[@type="checkbox" and @value="exact"]/ancestor::li/following-sibling::li//input[@value="3"]
//input[@type="checkbox" and @value="exact"]/ancestor::li/following-sibling::li//input[@value="7"]
//button[@aria-controls="flexible-searchboxdatepicker"]
//button[@aria-controls="calendar-searchboxdatepicker"]
(//*[@id="calendar-searchboxdatepicker"]//*[@data-testid="searchbox-datepicker-calendar"]//button[@type="button"])[1]
(//*[@id="calendar-searchboxdatepicker"]//*[@data-testid="searchbox-datepicker-calendar"]//button[@type="button"])[2]



CSS-selectors

[name="ss"]
#accommodations
#flights
[data-testid="date-display-field-start"]
[data-testid="date-display-field-end"]
[type="submit"]
[data-testid="searchbox-footer"] [name="sb_entire_place"]
[aria-controls^="CIT"]
[aria-controls="NATURE_ACTIVE"]
[data-testid="destination-postcards-firstrow"] a:first-of-type

"""