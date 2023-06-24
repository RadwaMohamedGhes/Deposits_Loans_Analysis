import random

data = open('Date.csv', 'w')


def load_customers(file):
    file = open(file, encoding='utf-8')
    customers = []
    file.readline()
    for i in file:
        cust = i.split(",")[0]
        customers.append(int(cust))
    file.close()
    return customers


def populate_date():
    header = 'Date_ID,minute,hour,day,week,month,quarter,year\n'
    data.write(header)
    for i in range(50000):
        minute = random.randint(0, 59)
        hour = random.randint(0, 23)
        day = random.randint(1, 30)
        week = random.randint(1, 51)
        month = random.randint(1, 12)
        if month < 4:
            quarter = 1
        elif month < 7:
            quarter = 2
        elif month < 10:
            quarter = 3
        else:
            quarter = 4
        year = random.randint(2018, 2023)
        row = f"{i},{minute},{hour},{day},{week},{month},{quarter},{year}\n"
        data.write(row)


def populate_services():
    services = ["Personal Loan", "Housing Loan",
                "Gold Loan", "Home Loan", "Vehicle Loan",
                "Recurring Deposit", "Fixed Deposit",
                "Callable Deposit", "Bullet deposit",
                "Flexi deposit"]
    header = 'Transaction_ID,Category,Transaction_type,Rate,amount,Duration,Year,Month\n'
    data.write(header)
    for i in range(100):
        category = random.choice(services)
        transaction_type = 'Loan' if "Loan" in category else "Deposit"
        amount = random.randint(20, 1000)
        if amount > 800:
            interest_rate = random.gauss(20, 2)
        elif amount > 600:
            interest_rate = random.gauss(18, 2)
        elif amount > 400:
            interest_rate = random.gauss(16, 2)
        elif amount > 200:
            interest_rate = random.gauss(14, 2)
        else:
            interest_rate = random.gauss(12, 2)
        interest_rate = round(interest_rate)
        amount *= 1000
        duration = random.randint(1, 5)
        year = random.randint(2018, 2023)
        month = random.randint(1, 12)
        row = f"{i},{category},{transaction_type},{interest_rate},{amount},{duration},{year},{month}\n"
        data.write(row)


def customer_services():
    customers = load_customers('Customers.csv')
    channels = ["In Person", "Phone", "Online"]
    actions = ["Inquiry", "Complaint", "Feedback"]
    header = 'ID,Member_ID,Action,Chanel,Customer_ID,Service_ID,Branch_ID,Date_ID,Severity\n'
    data.write(header)
    for i in range(5000):
        member = random.randint(1, 1000)
        action = random.choice(actions)
        chanel = random.choice(channels)
        customer = random.choice(customers)
        service = random.randint(0, 99)
        branch = random.randint(1, 53)
        date = random.randint(0, 49999)
        severity = random.randint(1, 10)
        row = f"{i},{member},{action},{chanel},{customer},{service},{branch},{date},{severity}\n"
        data.write(row)


def load_services(file):
    file = open(file, encoding='utf-8')
    services = {}
    file.readline()
    for i in file:
        row = i.split(",")
        services[int(row[0])] = row[2]
    file.close()
    return services


def populate_transactions():
    customers = load_customers("Customers.csv")
    header = 'ID,Customer_ID,Service_ID,Branch_ID,Date_ID,Renewed,Cancelled,Expenses,Approved\n'
    data.write(header)
    choices = [1, 1, 1, 0]
    services = load_services("Services.csv")
    for i in range(300001):
        customer = random.choice(customers)
        service = random.randint(0, 99)
        branch = random.randint(1, 53)
        date = random.randint(0, 49999)
        type_ = services[service]
        if type_ == "Loan":
            expenses = random.randint(1, 5)
            expenses *= 1000
            approved = random.choice(choices)
            if approved:
                renewed = random.choice(choices)
                cancelled = 0 if renewed else random.randint(0, 1)
            else:
                renewed = "Null"
                cancelled = "Null"
        else:
            expenses, approved = "Null", "Null"
            renewed = random.choice(choices)
            cancelled = 0 if renewed else random.randint(0, 1)
        row = f"{i},{customer},{service},{branch},{date},{renewed},{cancelled},{expenses},{approved}\n"
        data.write(row)


def populate_marketing():
    header = 'Service_ID,Date_ID\n'
    data.write(header)
    for i in range(31647):
        service = random.randint(0, 99)
        date = random.randint(0, 49999)
        raw = f"{service},{date}\n"
        data.write(raw)


data.close()
