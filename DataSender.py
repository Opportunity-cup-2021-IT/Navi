import openpyxl
import models
import datetime

#path = 'C:\\Users\\olga_\\Desktop\\кейс main\\OC2021_IT_Data_ASE.xlsx'

file = openpyxl.open('OC2021_IT_Data_ASE.xlsx', read_only=True)

currentList = file.active
# Выделение дипазона всех ячеек для скачивания из них данных
ranges = currentList[f"A1:F{currentList.max_row}"]

# Глобальньные переменные для взаимодействия с интерефейсом
events_for_table = []
main_events = []
events_for_dia = []


def init():
    # Инициализация глобальных переменнных
    global events_for_table
    global main_events

    main_events = get_crp_events()
    events_for_table = get_data_for_CRP_risc_table(main_events)


def get_all_events_majordata():
    data = []
    for row in range(1, currentList.max_row):
        # Выбор ячеек таблицы, содержащие самые важные данные для обработки
        line = [ranges[row][0].value, ranges[row][4].value, ranges[row][1].value, ranges[row][3].value,
                ranges[row][5].value, ranges[row][2].value]

        # Для последующей обработки данных тип None недопустим, поэтому меняем его на пустую строку
        if line[1] == None:
            line[1] = ''
        # Фильтрация данных на предмет пустых строк
        if line[0] != None and line[2] != None:
            ev = models.Event(id=line[0], followers=line[1], start=line[2], end=line[3], predecessors=line[4],
                              duty=line[5])
            data.append(ev)
    return data


# Функция бинарного поиска элемента в массиве событий по его id
def get_event_by_id(target, events):
    mid = len(events) // 2
    low = 0
    high = len(events) - 1

    while events[mid].id != target and low <= high:
        if target > events[mid].id:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return None
    else:
        return events[mid]
    pass


# Функция бинарного поиска индекса элемента в массиве событий по его id
# Это необходимо, потому что id в файле не последовательны
def get_indexof_event_by_id(target, events):
    mid = len(events) // 2
    low = 0
    high = len(events) - 1

    while events[mid].id != target and low <= high:
        if target > events[mid].id:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return None
    else:
        return mid


# Рекурсивная функция, используется для получения всех последователей заданного события
# Параметры
# event = событие, для которого мы строим полную карту последователей
# main_events = массив всех событий, полученных из файла
#
# black_list = список id тех событий для которых уже построенны карты зависимостей в текущей итерации рекурсии
# это допустимо так как многие элементы имеют общие связи, соотвественно, если мы имеем уже построенную карту зависимых событий
# мы можем не просчитывать её заново
# event_map= объект для накопления всех зависимых событий для заданного события
def get_down_maps(event, main_events, black_list, event_map):
    # массив для хранения зависимых событий для данного уровня рекурсии
    followers = []

    if event != 0:
        # проверка данных на валидность и наличие уже построенной карты зависимых событий в общем массиве событий
        # это допустимо так как события имеют общие ссвязи не только на локальном уровене между зависимыми событиями одного элемента
        if event != None and main_events[get_indexof_event_by_id(event.id, main_events)].already_have_down_map == False:
            for item in event.followers_strings:
                if item != None:
                    followers.append(models.Follower(item))

            follower_ids = []
            for follower in followers:
                # мы добавляем в массив не только id зависимого события, но и его тайм лаг, это необходимо для дальнейших вычислений
                follower_ids.append([follower.connector_id, follower.time_lag])

            event_map.append([event.id, follower_ids])

            # условие выхода из рекурсии, она идёт до тех пор, пока у события не окажется зависимых событий
            if len(followers) == 0:
                pass

            for follower in followers:
                if not follower.connector_id in black_list:
                    ev = get_event_by_id(follower.connector_id, main_events)
                    # если мы попали в этот блок значит, карта зависимостей ещё не построена для данного события,
                    # но так же, если мы попали в этот блок, значит что следующий рекрсивный вызов построит эту карту
                    black_list.append(follower.connector_id)

                    # вызываем функцию рекурсивного для каждого из зависимых событий
                    get_down_maps(ev, main_events, black_list, event_map)

        else:
            pass


# Функция для составления критического параметра сдвига
# событие тем критичнее для переноса, чем больше у него зависимых событий
# и чем меньше суммарный тайм-лаг всех зависимых событий
# мы можем учитывать суммарный тайм-лаг так как, если сдвиг произошёл в одном из событий он отразится и на последующих
# однако если между зависимыми событиями есть буффер в виде тайм-лага, это можем остановить череду сдвигов
def set_crp_and_follovnigs(events):
    for event in events:
        for map in event.down_map:
            # [[-1, 0]] - это условное обозначчение, того что у события нет зависимых событий
            # map - это подмассив в общей карте зависимых событий, в котором хранится id зависимого события и его зависимые события
            # map[1] - это список зависисых событий для текущего зависимого элемента
            if map[1] != [[-1, 0]]:
                event.CRP += len(map[1])
                event.folloving_level += len(map[1])
                # map_item[1] - тайм-лаг для зависимого события
                for map_item in map[1]:
                    event.CRP += map_item[1]


# Функция привязки карты зависимых событий ко всех элементам в массиве событий
def set_down_map(events):
    for ev in events:
        event_map = []
        get_down_maps(ev, events, [], event_map)
        # Устанавливаем что мы уже имеем полную карту зависимостей для данного события
        events[get_indexof_event_by_id(ev.id, events)].already_have_down_map = True
        ev.down_map = event_map


# Функция установки рекомендательных сообщений для каждого события в общем массиве событий
# в зависимости от кол-ва зависимых событий и уровня критического параметра сдвига
def set_recommendations(events):
    for event in events:
        event.set_recommend_message()


# Функция объекдиняющая в себе скачивание данных, получений карт зависимостей, установки параметра критичности сдвига
# и рекомендаций для всех событий
def get_crp_events():
    events = get_all_events_majordata()

    set_down_map(events)
    set_crp_and_follovnigs(events)
    set_recommendations(events)

    return events


# Функция сортировки массива событий по парметру критичности сдвига
def get_sorted_events_by_CRP(events):
    sorted_events = events[:]

    sorted_events.sort(key=lambda x: x.CRP)

    return sorted_events


# Функция адаптирования данных под формат, необходимый для построения таблицы рисков (фронт энд)
def get_data_for_CRP_risc_table(events):
    data_for_table = []
    sorted_events = get_sorted_events_by_CRP(events)
    for event in sorted_events:
        start = str(event.start)
        end = str(event.end)

        temp_item = [str(event.id), str(start), str(end), str(event.duration), str(event.CRP),
                     str(event.recommendations), str(event.folloving_level)]
        data_for_table.append(temp_item)
    return data_for_table


# Функция для подсчёта стоимости переноса, работает аналогично функции "get_down_maps"
# time_for_transfer = параметр, отвечающий за срок переноса конкретного события
# first_event= ссылка на изначальное событие, необходимо для суммирования в зависимости от кол-ва сдвигов
def calculate_transfer_price(event, main_events, black_list, event_map, time_for_transfer, first_event):
    followers = []

    if event != 0:
        if event != None and main_events[get_indexof_event_by_id(event.id, main_events)].already_have_down_map == False:
            for item in event.followers_strings:
                if item != None:
                    followers.append(models.Follower(item))

            follower_ids = []
            for follower in followers:
                follower_ids.append([follower.connector_id, follower.time_lag])

            for follower in followers:
                # если тай-лаг для данного события не покрывает срок переноса, значит событие будет перенесено
                # и надо начинать сдвиг события на тайм-лайне
                if follower.time_lag - time_for_transfer < 0:
                    temp_event = get_event_by_id(follower.connector_id, main_events)
                    if temp_event != None:
                        # к общей стоимости прибавляем стоимость переноса конкретного события
                        temp_price = 1
                        # если длительность события равна нулю, значит это веха, и стоимость переноса равна 1000
                        if temp_event.duration == 0:
                            temp_price = 1000
                        first_event.price += temp_price

                        # если длительность события не покрывает возможный сдвиг, значит даты начала и конца события надо изменить
                        if temp_event.duration - time_for_transfer < 0:
                            delta = datetime.timedelta(days=time_for_transfer)
                            temp_event.start += delta
                            temp_event.end += delta
                            main_events[get_indexof_event_by_id(temp_event.id, main_events)].start += delta
                            main_events[get_indexof_event_by_id(temp_event.id, main_events)].end += delta

            event_map.append([event.id, follower_ids])

            if len(followers) == 0:
                pass

            for follower in followers:
                if not follower.connector_id in black_list:
                    ev = get_event_by_id(follower.connector_id, main_events)
                    black_list.append(follower.connector_id)

                    calculate_transfer_price(ev, main_events, black_list, event_map, time_for_transfer,
                                             first_event)

        else:
            pass

# Функция форматирования данных для построения диаграммы ганта (фронт энд)
def get_data_for_dia(id, event_map):
    temp_array = []

    parent_event = get_event_by_id(id, main_events)
    paretn_start = str(parent_event.start)
    paretn_end = str(parent_event.end)

    temp_array.append([parent_event.id, paretn_start.split(' ')[0], paretn_end.split(' ')[0]])

    for map_item in event_map:

        for item in map_item[1]:

            folloving_event = get_event_by_id(item[0], main_events)
            if folloving_event != None:
                start = str(folloving_event.start)
                end = str(folloving_event.end)
                temp_array.append([folloving_event.id, start.split(' ')[0], end.split(' ')[0]])

    return temp_array
