import json
import random
import string
from pathlib import Path

class Hms:
    database = "hospital_data.json"
    data = []

    # Load data on class initialization
    if Path(database).exists():
        with open(database) as fs:
            content = fs.read().strip()
            data = json.loads(content) if content else {"patients": [], "doctors": [], "appointments": [], "bills": []}
    else :
        data = {"patients": [], "doctors": [], "appointments": [], "bills": []}

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(cls.data, indent=4))

    # ID Generators
    @staticmethod
    def id_gen_p():
        return "".join(random.choices(string.ascii_letters, k=2) + random.choices(string.digits, k=4))

    @staticmethod
    def id_gen_d():
        return "".join(random.choices("@#$%^&*", k=1) + random.choices(string.ascii_letters, k=2) + random.choices(string.digits, k=4))

    @staticmethod
    def appointment_no():
        return "".join(random.choices("@#$%^&*", k=1) + random.choices(string.ascii_letters, k=1) + random.choices(string.digits, k=3))

    # Utility for printing records
    @staticmethod
    def print_record(title, records):
        if not records:
            print(f"\nNo {title} records found.")
        else:
            print(f"\n--- {title} Records ---")
            for record in records:
                print("-" * 40)
                for k, v in record.items():
                    print(f"{k}: {v}")
                print("-" * 40)

    # Manage Patients
    def create_account(self):
        print("\n--- Manage Patients ---")
        print("1. Add Patient")
        print("2. View Patients")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Patient Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender (male/female): ")
            contact = input("Enter Contact: ")
            disease = input("Enter Disease: ")

            patient_info = {
                "name": name,
                "age": age,
                "gender": gender,
                "contact": contact,
                "disease": disease,
                "id_no": self.id_gen_p(),
                "patient_no": "P" + str(101 + len(Hms.data["patients"]))
            }

            Hms.data["patients"].append(patient_info)
            Hms.__update()
            print("\nPatient has been created successfully!")
            self.print_record("Patient", [patient_info])

        elif choice == "2":
            print("\n1. Search by ID or Patient No")
            print("2. View All Patients")
            sub_choice = input("Enter your choice: ")

            patients = Hms.data.get("patients", [])
            if sub_choice == "1":
                pid = input("Enter Patient ID (leave blank if unknown): ").strip()
                pno = input("Enter Patient No (leave blank if unknown): ").strip()
                result = [p for p in patients if (pid and p["id_no"] == pid) or (pno and p["patient_no"] == pno)]
                self.print_record("Patient", result)
            elif sub_choice == "2":
                self.print_record("Patient", patients)
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")

    # Manage Doctors
    def manage_doctors(self):
        print("\n--- Manage Doctors ---")
        print("1. Add Doctor")
        print("2. View Doctors")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Doctor Name: ")
            specialization = input("Enter Specialization: ")
            fees = input("Enter Fees: ")

            doctor_info = {
                "name": name,
                "specialization": specialization,
                "fees": fees,
                "id_no": self.id_gen_d()
            }

            Hms.data["doctors"].append(doctor_info)
            Hms.__update()
            print("\nDoctor has been added successfully!")
            self.print_record("Doctor", [doctor_info])

        elif choice == "2":
            doctors = Hms.data.get("doctors", [])
            self.print_record("Doctor", doctors)
        else:
            print("Invalid choice.")

    # Book Appointment
    def book_appointment(self):
        print("\n--- Book Appointment ---")
        print("1. Add Appointment")
        print("2. View Appointments")
        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = input("Enter Patient ID: ")
            doctor_id = input("Enter Doctor ID: ")
            appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
            time = input("Enter Time (HH:MM): ")

            is_patient = any(p["id_no"] == patient_id for p in Hms.data.get("patients", []))
            is_doctor = any(d["id_no"] == doctor_id for d in Hms.data.get("doctors", []))

            if is_patient and is_doctor:
                appointment_info = {
                    "patient_id": patient_id,
                    "doctor_id": doctor_id,
                    "appointment_date": appointment_date,
                    "time": time,
                    "appointment_no": self.appointment_no()
                }
                Hms.data["appointments"].append(appointment_info)
                Hms.__update()
                print("\nAppointment booked successfully!")
                self.print_record("Appointment", [appointment_info])
            else:
                print("Invalid patient ID or doctor ID.")

        elif choice == "2":
            appointments = Hms.data.get("appointments", [])
            self.print_record("Appointment", appointments)
        else:
            print("Invalid choice.")

    # Generate Bill
    def generate_bill(self):
        print("\n--- Generate Bill ---")
        patient_id = input("Enter Patient ID: ")
        consultation_fee = input("Enter Consultation Fee: ")
        medicine_charges = input("Enter Medicine Charges: ")
        other_charges = input("Enter Other Charges: ")

        bill_info = {
            "patient_id": patient_id,
            "consultation_fee": consultation_fee,
            "medicine_charges": medicine_charges,
            "other_charges": other_charges
        }

        Hms.data["bills"].append(bill_info)
        Hms.__update()
        print("\nBill generated successfully!")
        self.print_record("Bill", [bill_info])
    
    def __init__(self):
        self.patients1 = Hms.data.get("patients", [])
        self.doctors1 = Hms.data.get("doctors", [])
        self.appointments1 = Hms.data.get("appointments", [])
        self.bills1 = Hms.data.get("bills", [])
        
               
# ------------------- Main Menu -------------------

obj = Hms()
# print(obj.bills1)

a = True
while a:
    print("--------desi davakhana-------- ")
    print("1. Manage Patients")
    print("2. Manage Doctors")
    print("3. Book Appointment")
    print("4. Generate Bill")
    print("5. exit")


    try :
        choice = input("Enter your choice: ")
    except Exception as err:
        print("Invalid input.", err)
        choice = '0'

    if choice == '1':
        obj.create_account()
    elif choice == '2':
        obj.manage_doctors()
    elif choice == '3':
        obj.book_appointment()
    elif choice == '4':
        obj.generate_bill()
    elif choice == '5':
        a = False
    else:
        print("invalid choice or exiting...")