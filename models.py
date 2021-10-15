import datetime
import DataSender
import sys

sys.setrecursionlimit(1000000000)

# Класс, описывающий сущность последователя в проекте
class Follower:
    connector_id = -1
    follower_connect = ''
    predecessor_connect = ''
    time_lag = 0

    def __init__(self, data_string):
        if data_string != '':
            parts = data_string.split('+')
            coeff = 1
            if len(parts) != 2:
                parts = data_string.split('-')
                coeff = -1

            if parts[0] != None:
                id_str = ''

                for el in parts[0]:
                    if el.isdigit():
                        id_str += el
                parts[0] = parts[0].replace(id_str, '')
                self.connector_id = int(id_str)
                parts[0] = parts[0].replace(id_str, '')

                if len(parts[0]) == 2:
                    self.follower_connect = parts[0][0]
                    self.predecessor_connect = parts[0][1]
                elif len(parts[0]) == 1:
                    self.follower_connect = parts[0][0]

            if len(parts) > 1:
                self.time_lag = coeff * int(parts[1].replace(parts[1][-1], ''))




# Класс, описывающий сущность предшественника в проекте

class Predecessor:
    connector_id = 0
    follower_connect = ''
    predeccor_connect = ''
    time_lag = 0

    def __init__(self, data_string):
        if data_string != '':
            parts = data_string.split('+')
            coeff = 1
            if len(parts) != 2:
                parts = data_string.split('-')
                coeff = -1

            if parts[0] != None:
                id_str = ''

                for el in parts[0]:
                    if el.isdigit():
                        id_str += el
                parts[0] = parts[0].replace(id_str, '')
                self.connector_id = int(id_str)
                parts[0] = parts[0].replace(id_str, '')

                if len(parts[0]) == 2:
                    self.follower_connect = parts[0][0]
                    self.predecessor_connect = parts[0][1]
                elif len(parts[0]) == 1:
                    self.follower_connect = parts[0][0]

            if len(parts) > 1:
                self.time_lag = coeff * int(parts[1].replace(parts[1][-1], ''))

# Класс, описывающий сущность события в проекте
class Event:
    id = 0
    start = datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0)
    end = datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0)
    duration = 0
    followers_strings = []
    predecessor_strings = []

    price = 1
    recommendations = ''
    folloving_level = 0
    CRP = 0
    already_have_down_map = False
    already_have_up_map = False
    down_map = []
    up_map = []

    is_checked = False

    def __init__(self, data):
        self.id = int(data[0])

        self.start = dateConvert(data[1])
        self.end = dateConvert(data[3])

        self.duration = int(data[2].replace('д', ''))

        if str(data[4]) != None:
            self.followers_strings = str(data[4]).split(';')

        follovings = list(
            map(lambda x: '' if '...' in x else x, self.followers_strings))

        for item in follovings:
            if item == None:
                self.followers_strings.remove(item)

        if self.duration == 0:
            self.price = 1000

    def __init__(self, id, followers, start, end, predecessors, duty):
        self.id = int(id)

        if str(followers) != None:
            self.followers_strings = str(followers).split(';')

        follovings = list(
            map(lambda x: '' if '...' in x else x, self.followers_strings))

        for item in follovings:
            if item == None:
                self.followers_strings.remove(item)

        if str(predecessors) != None:
            self.predecessor_strings = str(predecessors).split(';')

        predecessors = list(
            map(lambda x: '' if '...' in x else x, self.predecessor_strings))

        for item in predecessors:
            if item == None:
                self.predecessor_strings.remove(item)

        self.start = dateConvert(start)
        self.end = dateConvert(end)

        self.duration = float(duty.replace('д', '').replace(',', '.'))

        if self.duration == 0:
            self.price = 1000

    # Функция установки рекомендательного сообщения в соответсвии с параметром критичности сдвига и количеству зависимых событий
    def set_recommend_message(self):
        if self.CRP < 0:
            self.recommendations = f"Мы не рекомендуем как-либо переносить это событие #{self.id}, оно имеет" \
                                   f" {self.folloving_level} зависимых событий и отрицательный CRP = {self.CRP}."
        elif self.CRP == 0 and self.folloving_level == 0:
            self.recommendations = f"Данное событие #{self.id} можно двигать без каких-либо опасений, оно не" \
                                   f" имеет зависимых событий и имеет CRP равный нулю."
        elif self.CRP == 0 and self.folloving_level != 0:
            self.recommendations = f"Данное событие #{self.id} можно двигать, не смотря на то, что оно имеет {self.folloving_level} зависимых событий, " \
                                   f"показатель CRP равен нулю."
        elif self.CRP == 0 and self.folloving_level > 0:
            self.recommendations = f"Данное событие #{self.id} можно двигать с осторожностью, их сдвиг не повлечёт за собой критических последствий благодаря" \
                                   f"нулевому CRP, оно имеет {self.folloving_level} зависимых событий, которые несмоненно пострадают из-за переноса #{self.id}"
        elif self.CRP > 0 and self.folloving_level > 0:
            self.recommendations = f"Данное событие #{self.id} можно передвигать, так как его параметр CRP = {self.CRP} положителен, однако оно имеет " \
                                   f"{self.folloving_level} зависимых событий, что может повлечь за собой определённую череду переносов."


# Функция конвертации даты из формата 1 Январь 2020 8:00  в формат 2020-01-01 8:00
def dateConvert(date_string):
    date_elements = date_string.split()

    date_comparison = {"Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6, "Июль": 7,
                       "Август": 8,
                       "Сентябрь": 9, "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12}

    return datetime.datetime(year=int(date_elements[2]), month=int(date_comparison[date_elements[1]]),
                             day=int(date_elements[0]), hour=int(date_elements[3].split(':')[0]),
                             minute=int(date_elements[3].split(':')[1]))
