from faker import Faker
from faker.providers.phone_number import Provider


class IndiaPhoneNumberProvider(Provider):
    """
    A Provider for phone number.
    """

    def india_phone_number(self):
        phone_number = self.msisdn()[3:]
        # Ensure that the first digit is not zero
        if phone_number[0] == '0':
            phone_number = '1' + phone_number[1:]
        return phone_number


fake = Faker()
fake.add_provider(IndiaPhoneNumberProvider)
phone = fake.india_phone_number()

other_phone = phone

if int(other_phone[-1]) == 9:
    lens = len(other_phone)
    other_phone = other_phone.replace(other_phone[lens - 1], str(9 - 1))
else:
    lens = len(other_phone)
    other_phone = other_phone.replace(other_phone[lens - 1], str(int(other_phone[-1]) + 1))


def name():
    l = []
    firstname = fake.first_name()
    lastname = fake.last_name()
    l.append(firstname)
    l.append(lastname)
    return l


c = name()
opportunity_name = name()
opportunity_mail = fake.email()
opportunity_phone = fake.india_phone_number()
# print(c[0], c[1], c[0] + " " + c[1])
email = fake.email()

partner_name=name()
partner_mail = fake.email()
partner_phone = fake.india_phone_number()
partner_other_phone = fake.india_phone_number()
partner_other_mail = fake.email()

update_phone = partner_phone

if int(update_phone[-1]) == 9:
    lens = len(update_phone)
    update_phone = update_phone.replace(update_phone[lens - 1], str(9 - 1))
else:
    lens = len(update_phone)
    update_phone = update_phone.replace(update_phone[lens - 1], str(int(update_phone[-1]) + 1))


# ----------------------below code to update csv file values-----------------------------------
CSV_name = name()
CSV_mail = fake.email()
CSV_phone = fake.india_phone_number()
# Read the existing CSV file
file_name = "features/steps/leads_sample.csv"
data = []

with open(file_name, mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Read the existing data into a list
    for row in csv_reader:
        data.append(row)

# Check if row 2 exists (0-based index)
if len(data) >= 2:
    # Update the cell values in row 2
    data[1] = [CSV_name[0], CSV_name[1], CSV_mail, 91, CSV_phone, "Digital", "Facebook", "Campaign Name", "Warm",
               "Any Description"]  # Modify these values as needed

    # Write the updated data back to the same CSV file
    with open(file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the updated data
        for row in data:
            csv_writer.writerow(row)