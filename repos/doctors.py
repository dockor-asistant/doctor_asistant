from models.doctor import Doctor


class Doctors(object):

    def __init__(self, doctor_model: Doctor):
        self._doctor_model = doctor_model

    def add_doctor_dialog(self) -> None:
        """ Консольный диалог добавления доктора в базу """
        print('Введите параметры для добавления в базу нового доктора;')
        name = input('Имя доктора: ')
        phone = input('Телефон: ')
        hospital_name = input('Поликлиника: ')
        hospital_id = self._doctor_model.get_id_hospital(hospital_name)
        self._doctor_model.add_doctor(name, phone, hospital_id)
        print('Поликлиника успешно добавлена в базу')

    def display_all_hospitals(self) -> None:
        """ Вывод в консоль список докторов """
        doctors_list = self._doctors_model.get_all_hospitals()
        count = 0
        for h in hospitals_list:
            count += 1
            print(f'{count}. {h[1]}')
