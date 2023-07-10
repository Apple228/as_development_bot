from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [
                                                KeyboardButton(text="Запустить анкету"),
                                            ]
                                        ])

location_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [
                                                KeyboardButton(text="Москва"),
                                                KeyboardButton(text="область/регион")
                                            ]
                                        ])

interesting_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                           keyboard=[
                                               [
                                                   KeyboardButton(text="Готовый дом")
                                               ],
                                               [
                                                   KeyboardButton(text="Стройка, своя земля"),
                                                   KeyboardButton(text="Стройка, нет земли"),
                                               ]
                                           ])

target_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [
                                              KeyboardButton(text="ПМЖ"),
                                              KeyboardButton(text="Дача"),
                                          ]
                                      ])

square_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [
                                              KeyboardButton(text="до 100м2"),
                                              KeyboardButton(text="до 200м2"),
                                              KeyboardButton(text="до 300м2"),
                                          ]
                                      ])

count_room_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                          keyboard=[
                                              [
                                                  KeyboardButton(text="1"),
                                                  KeyboardButton(text="2"),
                                                  KeyboardButton(text="3"),
                                              ],
                                              [
                                                  KeyboardButton(text="4"),
                                                  KeyboardButton(text="5"),
                                                  KeyboardButton(text="6"),
                                              ],
                                              [
                                                  KeyboardButton(text="7"),
                                                  KeyboardButton(text="8"),
                                                  KeyboardButton(text="9"),
                                              ]
                                          ])
equipment_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                         keyboard=[
                                             [
                                                 KeyboardButton(text="Теплый контур"),
                                                 KeyboardButton(text="Под ключ"),
                                             ]
                                         ])

project_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [
                                               KeyboardButton(text="Барнхаус XL>"),
                                               KeyboardButton(text="Барнхаус L"),
                                               KeyboardButton(text="Прованс XL"),
                                           ],
                                           [
                                               KeyboardButton(text="Норвегия L"),
                                               KeyboardButton(text="Норвегия XL"),
                                           ],
                                           [
                                               KeyboardButton(text="Финляндия М"),
                                               KeyboardButton(text="Финляндия L"),
                                               KeyboardButton(text="Финляндия XL"),
                                           ],
                                           [
                                               KeyboardButton(text="Модульный 25"),
                                               KeyboardButton(text="Модульный 38"),
                                               KeyboardButton(text="Модульный 49"),
                                           ],
                                           [
                                               KeyboardButton(text="Шведский L"),
                                               KeyboardButton(text="Шведский M"),
                                               KeyboardButton(text="Пропустить"),
                                           ],

                                       ])

budget_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [
                                              KeyboardButton(text="до 30 млн"),
                                              KeyboardButton(text="до 20 млн"),
                                          ],
                                          [
                                              KeyboardButton(text="до 10 млн"),
                                          ]

                                      ])
payment_method_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [
                                              KeyboardButton(text="Наличные"),
                                              KeyboardButton(text="Ипотека"),
                                          ],
                                      ])

mortgage_advice_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [
                                              KeyboardButton(text="Да"),
                                              KeyboardButton(text="Нет"),
                                          ],
                                      ])