
from telesign.messaging import MessagingClient


def sendSms(name_st, name_tr, phone, grade, name_cs):
    customer_id = "62458497-A044-4CBF-A3D4-001E3EF8BA15"
    api_key = "Z1a3lUoG6ybnZyUaGpaJGlbtDw+BS1ngsV+RNdMFQbnEuwdBPeemDP3ho71QrjBwldK+p4xJvwRBevPMylre6A=="

    phone_number = "77000252001"
    message = '\n' + "Name of student: " + name_st + '\n' + "Name of teacher: " + name_tr + '\n' + "Name of course: " + name_cs + '\n' + "Grade in lesson: " + grade
    message_type = "ARN"

    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)