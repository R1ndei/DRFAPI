from incomeExpenseDRFApi.celery import app


@app.task
def email_sender(data):
    data.send()
