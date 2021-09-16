from repos.doctors import Doctors
from models.doctor import Doctor
from repos.hospitals import Hospitals

if __name__ == '__main__':
    # print('OK-1')
    # try:
    #     data_manager1 = Hospitals(Hospital())
    #     data_manager1.display_all_hospitals()
    # except RuntimeError as rte:
    #     print(rte)
    doctor = Doctors(Doctor())
    doctor.add_doctor_dialog()






