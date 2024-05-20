from datetime import  datetime

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]
l=list(map(lambda x: datetime.strptime(x[1], '%H:%M') - datetime.strptime(x[0], '%H:%M'), data))
print(sum(list(map(lambda x: x.seconds,l))) //60)

