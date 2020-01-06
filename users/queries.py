from django.db import connection

def get_award_year(self):
    years = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT YEAR(award_date) FROM achivements_award WHERE fid_id=%s",[self.id])
        res = cursor.fetchall()
        for r in res:
            years.append(r[0])
    return years

def get_conference_year(self):
    years = []
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT DISTINCT YEAR(date) FROM achivements_conference WHERE fid_id=%s", [self.id])
        res = cursor.fetchall()
        for r in res:
            years.append(r[0])
    return years

def get_journal_year(self):
    years = []
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT DISTINCT YEAR(date) FROM achivements_journal WHERE fid_id=%s", [self.id])
        res = cursor.fetchall()
        for r in res:
            years.append(r[0])
    return years

def get_workshop_year(self):
    years = []
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT DISTINCT YEAR(date) FROM achivements_workshop WHERE fid_id=%s", [self.id])
        res = cursor.fetchall()
        for r in res:
            years.append(r[0])
    return years
    
