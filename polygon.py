class Car:
    """"Характеризует машину"""

    def __init__(self, engine_power: int, color: str, drive_unit: str = None, model_name: str = None):
        self.engine_power = engine_power
        self.color = color
        self.drive_unit = drive_unit
        self.model_name = model_name

    def __str__(self):
        """Выводит информацию об авто"""
        return f'Auto: {self.model_name}\n'\
               f'Color: {self.color}\n'\
               f'Engine power: {self.engine_power}\n'\
               f'Drive unit: {self.drive_unit}\n'


new_car = Car(model_name='Audi A9', color='red', engine_power=300)
new_car.drive_unit = "full"
print(new_car)
